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

from typing import List, Dict
from pprint import pprint
from datasets import Dataset
from model import Infer
from .base_attack import PromptAttack
from .txt2txt_seeds import (
    txt2txt_attacks,
    txt2txt_attack_names_zh,
    txt2txt_attack_names_en,
)


class Txt2TxtAttack(PromptAttack):

    def __init__(self, model: Infer, lang: str = "zh") -> None:
        super().__init__(model, lang)
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

    def attack_data(
        self, data: str, techniques: List[str] = None, **kwargs
    ) -> Dict[str, str]:
        if not techniques:
            techniques = list(self.attacks.keys())
        aug_data = {}
        for attack_name in techniques:
            if attack_name not in self.attacks.keys():
                raise ValueError(
                    f"Unsupported attacks! The currently supported text to text adversarial techniques should be in the list of {list(self.attacks.keys())}"
                )
            aug_data[attack_name] = self.attacker.infer_data(
                self.attacks[attack_name](data, lang=self.lang), **kwargs
            )
        return aug_data

    def attack_dataset(
        self, dataset: Dataset, techniques: List[str], **kwargs
    ) -> Dataset:
        return super().attack_dataset(dataset, techniques)
