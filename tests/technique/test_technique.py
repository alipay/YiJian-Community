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


import pytest
from yijian.model.base_infer import Infer
from yijian.technique.prompt_attack import BasePromptAttack, TextPromptAttack
from datasets import Dataset


def test_BasePromptAttack_init_unsupported_lang():
    with pytest.raises(ValueError):
        BasePromptAttack(None, lang="fr")


def test_BasePromptAttack_attack_dataset_NotImplementedError():
    with pytest.raises(NotImplementedError):
        BasePromptAttack(None).attack_dataset(Dataset.from_dict({"prompt": [1]}))


def test_TextPromptAttack_init_unsupported_lang():
    with pytest.raises(ValueError):
        TextPromptAttack(None, lang="fr")


def test_TextPromptAttack_init_unsupported_target():
    with pytest.raises(ValueError):
        TextPromptAttack(None, target="img2txt")


def test_TextPromptAttack_txt2txt_invalid_techniques():
    attacker = TextPromptAttack(None, target="txt2txt")
    with pytest.raises(ValueError):
        attacker.attack_data("", techniques=["info_compression"])


def test_TextPromptAttack_txt2img_invalid_techniques():
    attacker = TextPromptAttack(None, target="txt2img")
    with pytest.raises(ValueError):
        attacker.attack_data("", techniques=["introduction"])
