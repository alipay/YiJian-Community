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


from tqdm import tqdm
from typing import Union
from PIL import Image
from datasets import Dataset
from torch import normal
from transformers import pipeline
from yijian_community.model.base_infer import Infer
from yijian_community.utils.constants import DEVICE_MAP, BATCH_SIZE


class FalconsaiNSFWImageDetection(Infer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        self.infer = pipeline("image-classification", device_map=DEVICE_MAP, model=model_path)

    def infer_data(self, data: Union[str, Image.Image], **kwargs):
        if isinstance(data, str):
            img = Image.open(data)
            pred = self.infer(img, **kwargs)
            return self._extract_label(pred)
        elif isinstance(data, Image.Image):
            return self._extract_label(self.infer(data, **kwargs))
        else:
            raise TypeError(
                f"Unsupported data type, should be str or Image, but {type(data)} found!"
            )

    def infer_dataset(
        self, dataset: Dataset, target_column="response_image", batch_size=BATCH_SIZE, **kwargs
    ) -> Dataset:
        preds_all = []
        for data in tqdm(dataset.iter(batch_size=batch_size)):
            images = [Image.open(img_path) for img_path in data[target_column]]
            preds = self.infer(images, batch_size=batch_size, **kwargs).images
            preds_all.extend([self._extract_label(pred) for pred in preds])
        return dataset.add_column("image_rejection", preds_all)

    def _extract_label(self, pred_res):
        for item in pred_res:
            if "normal" == item["label"]:
                normal_score = item["score"]
            elif "nsfw" == item["label"]:
                nsfw_score = item["score"]
        if nsfw_score >= normal_score:
            return 1
        else:
            return 0
