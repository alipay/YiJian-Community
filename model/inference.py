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


from transformers import pipeline
from diffusers import DiffusionPipeline
from utils import OPEN, API, CUSTOM


# text to text inference


def txt2txt_inference(model_name, model_type=OPEN):
    if model_type == OPEN:
        return pipeline(
            "text-generation",
            model=model_name,
            device_map="auto",
        )
    if model_type == API:
        return
    if model_type == CUSTOM:
        return
    raise ValueError(
        f"Unsupported model type: {model_type}! It should be {OPEN}, {API} or {CUSTOM}."
    )


# text to image inference
def txt2img_inference(model_name, model_type=OPEN):
    if model_type == "open_source":
        return DiffusionPipeline.from_pretrained(model_name, device_map="auto")
    if model_type == API:
        return
    if model_type == CUSTOM:
        return
    raise ValueError(
        f"Unsupported model type: {model_type}! It should be {OPEN}, {API} or {CUSTOM}."
    )


# image text to text inference
def imgtxt2txt_inference(model_name, model_type=OPEN):
    if model_type == "open_source":
        return pipeline(
            "image-to-text",
            model=model_name,
            device_map="auto",
        )
    if model_type == API:
        return
    if model_type == CUSTOM:
        return
    raise ValueError(
        f"Unsupported model type: {model_type}! It should be {OPEN}, {API} or {CUSTOM}."
    )
