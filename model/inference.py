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


import torch
from abc import ABC, abstractmethod
from datasets import Dataset
from .model import txt2txt_model, txt2img_model, imgtxt2txt_model
from utils import HF, API, CUSTOM, BATCH_SIZE
from typing import Dict


# Base class for inference
class Infer(ABC):

    def __init__(self, model_name, model_type=HF):
        self.model_name = model_name
        self.model_type = model_type

    @abstractmethod
    def infer_dataset(self, dataset, batch_size=1):
        """inference on one datasets.Dataset

        Args:
            dataset (datasets.Dataset): evaluation dataset
            batch_size (int, optional): _description_. Defaults to 1.
        """
        pass


# text to text inference
class Txt2TxtInfer(Infer):

    def __init__(self, model_name: str, model_type: str = HF, **kwargs):
        super().__init__(model_name, model_type)
        self.model = txt2txt_model(
            model_name=self.model_name, model_type=self.model_type, **kwargs
        )

    def infer_dataset(self, dataset: Dataset, batch_size: int = 1, **kwargs) -> Dataset:

        def _map(batch: Dict) -> Dict:
            if self.model_type == HF:
                response_texts = self.model(batch["prompt_text"], **kwargs)
                batch["response_text"] = [
                    r[0]["generated_text"] for r in response_texts
                ]
            elif self.model_type == API:
                pass
            elif self.model_type == CUSTOM:
                pass
            return batch

        return dataset.map(_map, batched=True, batch_size=batch_size)


# text to image inference
class Txt2ImgInfer(Infer):

    def __init__(self, model_name: str, model_type: str = HF, **kwargs):
        super().__init__(model_name, model_type)
        self.model = txt2img_model(
            model_name=self.model_name, model_type=self.model_type, **kwargs
        )
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def infer_dataset(self, dataset: Dataset, batch_size: int = 1, **kwargs) -> Dataset:
        prompt_texts = dataset["prompt_text"]
        if self.model_type == HF:
            response_images = []
            data_num = dataset.shape[0]
            i = 0
            while i * batch_size < data_num:
                start = i * batch_size
                end = (i + 1) * batch_size
                response_images.extend(self.model())
            response_images = self.model(dataset["prompt_text"], **kwargs).images
            return response_images
        if self.model_type == API:
            pass
        if self.model_type == CUSTOM:
            pass


# image text to text inference
class ImgTxt2TxtInfer(Infer):

    def __init__(self, model_name, model_type=HF):
        super().__init__(model_name, model_type)
        self.model = imgtxt2txt_model(
            model_name=self.model_name, model_type=self.model_type
        )

    def infer_dataset(self, dataset, batch_size=BATCH_SIZE):
        pass
