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
from abc import ABC, abstractmethod
from datasets import Dataset
from .model import txt2txt_model, txt2img_model, imgtxt2txt_model
from utils import HF, API, CUSTOM, BATCH_SIZE
from typing import Dict, Union
from transformers import pipeline
from diffusers import DiffusionPipeline


# Base class for inference
class Infer(ABC):

    def __init__(self, model_name, model_type=HF):
        self.model_name = model_name
        self.model_type = model_type

    @abstractmethod
    def infer_dataset(self, dataset):
        """inference on one datasets.Dataset

        Args:
            dataset (datasets.Dataset): evaluation dataset
        """
        pass


# text to text inference
class Txt2TxtInfer(Infer):

    def __init__(self, model_name: str, model_type: str = HF, **kwargs):
        super().__init__(model_name, model_type)

        if model_type == HF:
            self.model = pipeline("text-generation", model=model_name, **kwargs)
        elif model_type == API:
            pass
        elif model_type == CUSTOM:
            pass
        else:
            raise ValueError(
                f"Unsupported model type: {model_type}! Model type can only be {HF}, {API} or {CUSTOM}."
            )

    def infer_dataset(self, dataset: Dataset, **kwargs) -> Dataset:
        if self.model_type == HF:
            response_texts = self.model(dataset["prompt_text"], **kwargs)
            return dataset.add_column(
                "response_text", [r[0]["generated_text"] for r in response_texts]
            )
        elif self.model_type == API:
            pass
        elif self.model_type == CUSTOM:
            pass


# text to image inference
class Txt2ImgInfer(Infer):

    def __init__(self, model_name: str, model_type: str = HF, **kwargs):
        super().__init__(model_name, model_type)

        if model_type == HF:
            self.model = DiffusionPipeline.from_pretrained(model_name, **kwargs)
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.model.to(self.device)
        elif model_type == API:
            pass
        elif model_type == CUSTOM:
            pass
        else:
            raise ValueError(
                f"Unsupported model type: {model_type}! Model type can only be {HF}, {API} or {CUSTOM}."
            )

    def infer_dataset(self, dataset: Dataset, batch_size: int = 1, **kwargs) -> Dataset:
        if self.model_type == HF:
            return dataset.add_column(
                "response_image", self.model(dataset["prompt_text"], **kwargs).images
            )
        elif self.model_type == API:
            pass
        elif self.model_type == CUSTOM:
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
