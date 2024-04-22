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
from datasets import load_dataset

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_dataset_from_csv(filename):
    full_path = os.path.join(CURRENT_DIR, filename)
    print(f"Loading {full_path}")
    return load_dataset("csv", data_files=full_path)["train"]


txt2txt_set = get_dataset_from_csv("txt2txt/txt2txt.csv")

txt2img_set = get_dataset_from_csv("txt2img/txt2img.csv")

imgtxt2txt_set = get_dataset_from_csv("imgtxt2txt/imgtxt2txt.csv")
