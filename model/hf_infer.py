# -*- coding: utf-8 -*-
# Copyright 2024 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import torch
from utils import BATCH_SIZE, DEVICE_MAP, MAX_NEW_TOKENS, RETURN_FULL_TEXT, TEMPERATURE
from utils import save_images_and_return_path
from .base_infer import Infer
from transformers import pipeline
from datetime import datetime
from datasets import Dataset
from diffusers import DiffusionPipeline


class HFTxt2TxtInfer(Infer):

    def __init__(self, model_name: str, device_map: str = DEVICE_MAP, **kwargs):
        super().__init__(model_name)
        self.model = pipeline(
            "text-generation", model=model_name, device_map=device_map, **kwargs
        )

    def infer_dataset(
        self,
        dataset: Dataset,
        batch_size: int = BATCH_SIZE,
        max_new_tokens: int = MAX_NEW_TOKENS,
        return_full_text: bool = RETURN_FULL_TEXT,
        temperature: float = TEMPERATURE,
        **kwargs,
    ) -> Dataset:
        response_texts = []
        dataset_len = len(dataset)
        i = 0
        while i * batch_size < dataset_len:
            response_texts.extend(
                [
                    r[0]["generated_text"]
                    for r in self.model(
                        dataset["prompt_text"][i * batch_size : (i + 1) * batch_size],
                        max_new_tokens=max_new_tokens,
                        return_full_text=return_full_text,
                        temperature=temperature,
                        **kwargs,
                    )
                ]
            )
            i += 1
        return dataset.add_column("response_text", response_texts)


class HFTxt2ImgInfer(Infer):

    def __init__(self, model_name: str, **kwargs):
        super().__init__(model_name)
        self.model = DiffusionPipeline.from_pretrained(model_name, **kwargs)
        if torch.cuda.is_available():
            self.model.to("cuda")

    def infer_dataset(
        self,
        dataset: Dataset,
        batch_size: int = BATCH_SIZE,
        temperature: float = TEMPERATURE,
        **kwargs,
    ) -> Dataset:
        image_save_path = os.path.join(
            os.getcwd(), "images_txt2img_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        )
        os.makedirs(image_save_path, exist_ok=True)

        response_images = []
        dataset_len = len(dataset)
        i = 0
        while i * batch_size < dataset_len:
            prompt_texts = dataset["prompt_text"][i * batch_size : (i + 1) * batch_size]
            images = self.model(
                prompt_texts,
                temperature=temperature,
                **kwargs,
            ).images
            response_images.extend(
                [
                    save_images_and_return_path(
                        image_save_path, self.model_name, prompt_text, image
                    )
                    for image, prompt_text in zip(images, prompt_texts)
                ]
            )
            i += 1
        return dataset.add_column("response_image", response_images)
