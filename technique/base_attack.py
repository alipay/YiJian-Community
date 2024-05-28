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
from typing import List, Dict
from model import Infer


class PromptAttack(ABC):

    def __init__(self, model: Infer, lang: str = "zh") -> None:
        """

        Args:
            model (Infer): model instance for generating risky prompts
            lang (str, optional): the language of the prompt, can be 'zh' or 'en'. Defaults to "zh".
        """
        if lang not in ("zh", "en"):
            raise ValueError(
                "the language of the prompt can only be Chinese, i.e., 'zh', or English, i.e., 'en'."
            )
        self.lang = lang
        self.attacker = model

    @abstractmethod
    def attack_data(self, data: str, techniques: List[str], **kwargs) -> Dict[str, str]:
        """attack against one data

        Args:
            data (str): plain text
            techniques (List[str]): list of attack techniques

        Returns:
            str: attack enhanced text
        """

    @abstractmethod
    def attack_dataset(
        self, dataset: Dataset, techniques: List[str], **kwargs
    ) -> Dataset:
        """attack against one datasets.Dataset

        Args:
            dataset (Dataset): plain dataset
            techniques (List[str]): list of attack techniques

        Returns:
            Dataset: result dataset
        """
        pass
