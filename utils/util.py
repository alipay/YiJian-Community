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
import hashlib
import requests
from PIL import Image
from io import BytesIO
from typing import List


def save_images_and_return_paths(
    image_save_path: str,
    model_name: str,
    prompt_texts: List[str],
    images: List[Image.Image],
) -> str:
    save_paths = []
    for prompt_text, image in zip(prompt_texts, images):
        md5 = hashlib.md5((model_name + prompt_text).encode()).hexdigest()
        save_path = os.path.join(image_save_path, md5 + ".jpg")
        image.save(save_path)
        save_paths.append(save_path)
    return save_paths


def get_image_from_url(image_url: str):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_bytes = BytesIO(response.content)
        image = Image.open(image_bytes)
        return image
    return "iamge download failure"
