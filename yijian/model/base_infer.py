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


# Base class for inference
class Infer(ABC):

    def __init__(self, model_path: str):
        """

        Args:
            model_path (str): path to the target model or the name of the target model.
        """
        self.model_path = model_path
        self.infer = None

    @abstractmethod
    def infer_data(self, data: str):
        """inference on one data.

        Args:
            data (str): the prompt text.
        """
        pass

    @abstractmethod
    def infer_dataset(self, dataset: Dataset) -> Dataset:
        """inference on one Dataset.

        Args:
            dataset (Dataset): evaluation dataset, which (optional but recommended) contains a column named "prompt_text".

        Returns:
            Dataset: result dataset.
        """
        raise NotImplementedError("infer_dataset should be implemented!")
