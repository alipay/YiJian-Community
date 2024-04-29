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
import pytest
from dataset import get_dataset_from_csv
from datasets import Dataset
from pathlib import Path


@pytest.mark.parametrize(
    "csv_file",
    [
        "dataset/txt2txt/txt2txt.csv",
        "dataset/txt2img/txt2img.csv",
        "dataset/imgtxt2txt/imgtxt2txt.csv",
    ],
)
def test_dataset_valid(csv_file):
    csv_path = os.path.join(Path(__file__).resolve().parent.parent, csv_file)
    dataset = get_dataset_from_csv(csv_path)
    assert dataset is not None and isinstance(dataset, Dataset)
