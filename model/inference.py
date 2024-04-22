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


from abc import ABC, abstractmethod
from datasets import Dataset
from .model import txt2txt_model, txt2img_model, imgtxt2txt_model
from utils import HF, API, CUSTOM, MAX_NEW_TOKENS, RETURN_FULL_TEXT, BATCH_SIZE


# Base class for inference
class Infer(ABC):

    def __init__(self, model_name, model_type=HF):
        self.model_name = model_name
        self.model_type = model_type

    @abstractmethod
    def infer_sample(self, sample):
        """inference on one sample

        Args:
            sample (_type_): one input sample, usually a string
        """
        pass

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
        self.model = txt2txt_model(
            model_name=self.model_name, model_type=self.model_type, **kwargs
        )

    def infer_sample(self, prompt_text: str, **kwargs) -> str:
        if self.model_type == HF:
            return self.model(prompt_text, **kwargs)[0]["generated_text"]
        if self.model_type == API:
            return
        if self.model_type == CUSTOM:
            return

    def infer_dataset(self, dataset: Dataset, **kwargs) -> Dataset:
        if self.model_type == HF:
            response_texts = self.model(dataset["prompt_text"], **kwargs)
            return dataset.add_column(
                "response_text", [r[0]["generated_text"] for r in response_texts]
            )
        if self.model_type == API:
            return
        if self.model_type == CUSTOM:
            return


# text to image inference
class Txt2ImgInfer(Infer):

    def __init__(self, model_name: str, model_type: str = HF, **kwargs):
        super().__init__(model_name, model_type)
        self.model = txt2img_model(
            model_name=self.model_name, model_type=self.model_type, **kwargs
        )

    def infer_sample(self, prompt_text: str, **kwargs):
        if self.model_type == HF:
            ans = self.model(prompt_text, **kwargs)
            print(type(ans), ans)
            print(type(ans.images), ans.images)
            print(type(ans.images[0]), ans.images[0])
            return self.model(prompt_text).images[0]
        if self.model_type == API:
            pass
        if self.model_type == CUSTOM:
            pass

    def infer_dataset(self, dataset: Dataset, **kwargs) -> Dataset:
        if self.model_type == HF:
            pass
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

    def infer_sample(self, prompt_image, prompt_text):
        pass

    def infer_dataset(self, dataset, batch_size=BATCH_SIZE):
        pass
