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
from datasets import load_dataset, Dataset


def load_local_files(local_path: str) -> Dataset:
    """get Dataset object from local dir or local files

    Args:
        local_path (str): path to a directory contains multiple data files or to a csv file

    Returns:
        Dataset: for evaluating the safety of target large models, should contains at least the following features:
                - prompt_text: prompt text
                - risk_type: what kind of risk the prompt text may incur, if it is a hierarchical system, link each level of risks with '/'
                - technique: attack method used to generate the prompt text
                - lang: the language of the prompt text, can be zh (i.e., chinese) or en (i.e., english)
                - attack_type: Optional, can be L1, L2, L3 or L4
    """
    if os.path.isdir(local_path):
        return load_dataset(local_path)["train"]
    elif os.path.isfile(local_path):
        return load_dataset("csv", data_files=local_path)["train"]
    else:
        raise TypeError(
            "local_path can only be a path to a directory containing multiple data files or to a single csv file."
        )


def save_dataset(save_path: str, dataset: Dataset, save_type="csv") -> None:
    save_type = save_type.lower()
    if save_type == "csv":
        dataset.to_csv(save_path)
    elif save_type == "json":
        dataset.to_json(save_path)
    elif save_type == "parquet":
        dataset.to_parquet(save_path)
    elif save_type == "sql":
        dataset.to_sql(save_path)
    else:
        raise TypeError("Invalid save_type, can only be csv, json, parquet or sql.")
