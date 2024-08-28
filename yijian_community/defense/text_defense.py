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


from datasets import Dataset
import torch
from yijian_community.model.base_infer import Infer
from transformers import AutoTokenizer, AutoModelForCausalLM

from yijian_community.utils.constants import DEVICE_MAP


class ThuCoaiShieldLM(Infer):
    # code adapted from [thu-coai/ShieldLM](https://github.com/thu-coai/ShieldLM)

    def __init__(self, model_path: str):
        super().__init__(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, padding_side="left", trust_remote_code=True
        )
        self.infer = AutoModelForCausalLM.from_pretrained(
            model_path,
            load_in_8bit=False,
            torch_dtype=torch.float16,
            device_map=DEVICE_MAP,
            trust_remote_code=True,
        )
        self.infer.eval()

        if not self.tokenizer.eos_token:
            self.tokenizer.eos_token = '<|endoftext|>'
        if not self.tokenizer.pad_token:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def infer_data(self, data: str):
        return super().infer_data(data)

    def infer_dataset(self, dataset: Dataset) -> Dataset:
        return super().infer_dataset(dataset)
