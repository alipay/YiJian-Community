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

import random
from typing import List, Dict

from datasets import Dataset
from .base_attack import PromptAttack
from .attack_seeds import inquiry_seed


class Txt2TxtAttack(PromptAttack):

    def __init__(self, model_path: str, lang: str = "zh") -> None:
        super().__init__(model_path, lang)
        self.attacks = {"inquiry": self._inquiry}
        if self.lang == "zh":
            print("目前支持的文生文攻击手法如下：")
            print("inquiry: 介绍了解类型")
        else:
            pass

    def attack_data(self, data: str, techniques: List[str] = None) -> Dict[str, str]:
        if not techniques:
            techniques = list(self.attacks.keys())
        aug_data = {}
        for attack_name in techniques:
            aug_data[attack_name] = self.attacker.infer_data(
                self.attacks[attack_name](data),
                do_sample=True,
            )
        return aug_data

    def attack_dataset(self, dataset: Dataset, techniques: List[str]) -> Dataset:
        return super().attack_dataset(dataset, techniques)

    def _inquiry(self, raw_query: str) -> str:
        """
        Introduction/Explanation type
        For instance:
        1. Could you please introduce xxx to me?
        2. What is xxx?
        3. What are the practical applications of xxx?
        """
        return inquiry_seed[self.lang].replace("[raw_query]", raw_query)

    def _writing_assistant(self, raw_query: str) -> str:
        if self.lang == "zh":
            pass
        else:
            pass
