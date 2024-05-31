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
from datasets import Dataset, concatenate_datasets
from typing import List, Dict
from model import Infer
from pprint import pprint
from .txt2txt_seeds import (
    txt2txt_attacks,
    txt2txt_attack_names_zh,
    txt2txt_attack_names_en,
    template_based_attacks,
)
from .txt2img_seeds import (
    txt2img_attacks,
    txt2img_attack_names_zh,
    txt2img_attack_names_en,
)
import pandas as pd
import time


class BasePromptAttack(ABC):

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


class TextPromptAttack(BasePromptAttack):

    def __init__(self, model: Infer, lang: str = "zh", target: str = "txt2txt") -> None:
        super().__init__(model, lang)
        self.target = target
        if self.target == "txt2txt":
            self.attacks = txt2txt_attacks
            print("当前支持的文生文攻击手法如下：")
            print(
                "The currently supported text to text adversarial techniques are as follows:"
            )
            pprint(
                [
                    zh + "/" + en
                    for zh, en in zip(txt2txt_attack_names_zh, txt2txt_attack_names_en)
                ]
            )
        elif self.target == "txt2img":
            self.attacks = txt2img_attacks
            print("当前支持的文生图攻击手法如下：")
            print(
                "The currently supported text to image adversarial techniques are as follows:"
            )
            pprint(
                [
                    zh + "/" + en
                    for zh, en in zip(txt2img_attack_names_zh, txt2img_attack_names_en)
                ]
            )
        else:
            raise ValueError(
                f"Attack target can only be 'txt2txt' or 'txt2img', but {self.target} found!"
            )

    def attack_data(
        self, data: str, techniques: List[str] = None, **kwargs
    ) -> Dict[str, str]:
        if not techniques:
            techniques = list(self.attacks.keys())
        aug_data = {}
        for attack_name in techniques:
            if attack_name not in self.attacks.keys():
                raise ValueError(
                    f"Unsupported attacks! The prompt attack techniques should be in the list of {list(self.attacks.keys())}"
                )
            print(f"Using {attack_name} to augment prompt texts ...")
            attack_seed = self.attacks[attack_name](data, lang=self.lang)
            if attack_name in template_based_attacks:
                aug_data[attack_name] = attack_seed
            else:
                aug_data[attack_name] = self.attacker.infer_data(attack_seed, **kwargs)
        return aug_data

    def attack_dataset(
        self, dataset: Dataset, techniques: List[str] = None, **kwargs
    ) -> Dataset:
        if not techniques:
            techniques = list(self.attacks.keys())

        seeds_list = []

        for attack_name in techniques:
            if attack_name not in self.attacks.keys():
                raise ValueError(
                    f"Unsupported attacks! The prompt attack techniques should be in the list of {list(self.attacks.keys())}"
                )

            print(f"Using {attack_name} to augment prompt texts ...")
            start = time.time()
            dataset_with_seeds = dataset.map(
                lambda row: {
                    "aug_prompt": self.attacks[attack_name](
                        row["prompt_text"], lang=self.lang
                    ),
                    "technique": attack_name,
                }
            ).select_columns(["prompt_text", "aug_prompt", "technique"])
            print(f"Map lasting {time.time() - start} seconds ...")

            start2 = time.time()
            if attack_name in template_based_attacks:
                seeds_list.append(dataset_with_seeds)
            else:
                seeds_list.append(
                    self.attacker.infer_dataset(
                        dataset_with_seeds, target_column="aug_prompt", **kwargs
                    )
                    .select_columns(["prompt_text", "response_text", "technique"])
                    .rename_column("response_text", "aug_prompt")
                )
            print(f"aug lasting {time.time() - start2} seconds ...")
        return concatenate_datasets(seeds_list)
