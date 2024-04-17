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


from utils import OPEN, API, CUSTOM

# models for text to text task
txt2txt_models = {
    OPEN: {
        "Command R+": "CohereForAI/c4ai-command-r-plus",
        "Mistral-7B": "mistralai/Mistral-7B-Instruct-v0.2",
    },
    API: {},
    CUSTOM: {},
}


# models for text to image task
txt2img_models = {
    OPEN: {"Stable Diffusion V1-5": "runwayml/stable-diffusion-v1-5"},
    API: {},
    CUSTOM: {},
}


# models for image text to text task
imgtxt2txt_models = {OPEN: {}, API: {}, CUSTOM: {}}
