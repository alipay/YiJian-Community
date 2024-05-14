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


def save_image_and_return_path(
    image_save_path: str, model_name: str, prompt_text: str, image: Image.Image
) -> str:
    md5 = hashlib.md5((model_name + prompt_text).encode()).hexdigest()
    save_path = os.path.join(image_save_path, md5 + ".jpg")
    image.save(save_path)
    return save_path


def get_image_from_url(image_url: str):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_bytes = BytesIO(response.content)
        image = Image.open(image_bytes)
        return image
    return "iamge download failure"
