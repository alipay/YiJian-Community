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


from datasets import load_dataset
from datasets.arrow_dataset import Dataset


def load_data(data_path: str) -> Dataset:
    """get datasets.arrow_dataset.Dataset object for evaluating

    Args:
        data_path (str): path to the directory containing the evaluation data files.
        NOTE: Files should all
        1) be the same format, which can be csv, jsonl or parquet;
        2) have the same columns.
        3) (optional but recommended) contains a column named "prompt_text"

    Returns:
        Dataset: a Dataset instance for the later evaluation pipeline
    """
    return load_dataset(data_path)["train"]


def save_data(data_path: str, data: Dataset) -> None:
    """save the Dataset instance to a file

    Args:
        data_path (str): data path for saving, the data type can be "csv", "json" or "parquet"
        data (Dataset): Dataset instance to be saved
    """
    file_type = data_path.split(".")[-1].strip()
    if file_type == "csv":
        data.to_csv(data_path)
    elif file_type == "json":
        data.to_json(data_path)
    elif file_type == "parquet":
        data.to_parquet(data_path)
    else:
        raise ValueError(
            f"Invalid data_path, should be a path to a 'csv', 'json' or 'parquet' file, but {file_type} found!"
        )
