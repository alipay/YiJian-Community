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
from typing import List

import pandas as pd
from datasets import Dataset, load_dataset
from PIL import Image


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
    if os.path.isdir(data_path):
        return load_dataset(data_path)["train"]
    if os.path.isfile(data_path):
        if data_path.endswith("csv"):
            # load single csv file with load_dataset() is astonishingly slow
            return Dataset.from_pandas(pd.read_csv(data_path))
        if data_path.endswith("json") or data_path.endswith("jsonl"):
            return load_dataset("json", data_files=data_path)["train"]
        if data_path.endswith("parquet"):
            return load_dataset("parquet", data_files=data_path)["train"]
    raise ValueError(
        f"Invalid data_path, should be a path to a 'csv', 'json' or 'parquet' file, or a path to a directory containing the three types of files, but {data_path} found!"
    )


def save_data(data_path: str, data: Dataset) -> None:
    """save the Dataset instance to a file

    Args:
        data_path (str): data path for saving, the data type can be "csv", "json" or "parquet"
        data (Dataset): Dataset instance to be saved
    """
    file_type = data_path.split(".")[-1].strip()
    if file_type == "csv":
        data.to_csv(data_path)
    elif file_type == "json" or file_type == "jsonl":
        data.to_json(data_path)
    elif file_type == "parquet":
        data.to_parquet(data_path)
    else:
        raise ValueError(
            f"Invalid data_path, should be a path to a 'csv', 'json' or 'parquet' file, but {file_type} found!"
        )


def save_image(
    save_path: str,
    prompt_texts: List[str],
    images: List[Image.Image],
) -> List[str]:
    """save images and return the save path

    Args:
        save_path (str): path to the directory which saves the images
        model_name (str): target model name
        prompt_texts (List[str]): list of prompt texts
        images (List[Image.Image]): list of Image.Image instance

    Returns:
        List[str]: list of paths which targeted the saved images
    """
    img_save_paths = []
    for prompt_text, image in zip(prompt_texts, images):
        img_save_path = os.path.join(save_path, prompt_text + ".jpg")
        image.save(img_save_path)
        img_save_paths.append(img_save_path)
    return img_save_paths
