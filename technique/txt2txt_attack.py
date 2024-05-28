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
from .base_attack import PromptAttack
from .txt2txt_seeds import *


class Txt2TxtAttack(PromptAttack):

    def __init__(self, model_path: str, lang: str = "zh") -> None:
        super().__init__(model_path, lang)
        self.attacks = {
            "introduction": introduction,
            "writing_assistant": writing_assistant,
            "reverse_induction": reverse_induction,
            "step_by_step": step_by_step,
            "forced_consent": forced_consent,
            "sentence_overflow": sentence_overflow,
            "fallacious_premise": fallacious_premise,
            "virtualization": virtualization,
            "repetition": repetition,
            "code_attack": code_attack,
            "implicit_knowledge": implicit_knowledge,
            "pros_and_cons": pros_and_cons,
            "text_summarization": text_summarization,
        }
        if self.lang == "zh":
            print("当前支持的文生文攻击手法如下：")
            print(
                "介绍了解，帮忙写作，反向诱导，循序渐进，强制同意，长句溢出，错误前提，虚拟化，口令复述，代码攻击，隐晦知识，正反介绍，文本摘要"
            )
        else:
            print(
                "The currently supported text to text adversarial techniques are as follows:"
            )
            print(
                "introduction, writing_assistant, reverse_induction, step_by_step, forced_consent, sentence_overflow, fallacious_premise, virtualization, repetition, code_attack, implicit_knowledge, pros_and_cons, text_summarization"
            )

    def attack_data(self, data: str, techniques: List[str] = None) -> Dict[str, str]:
        if not techniques:
            techniques = list(self.attacks.keys())
        aug_data = {}
        for attack_name in techniques:
            if attack_name not in self.attacks.keys():
                raise ValueError(
                    f"Unsupported attacks! The currently supported text to text adversarial techniques should be in the list of {list(self.attacks.keys())}"
                )
            aug_data[attack_name] = self.attacker.infer_data(
                self.attacks[attack_name](data, self.lang),
                do_sample=True,
            )
            print(attack_name, self.attacks[attack_name](data, self.lang))
        return aug_data

    def attack_dataset(self, dataset: Dataset, techniques: List[str]) -> Dataset:
        return super().attack_dataset(dataset, techniques)
