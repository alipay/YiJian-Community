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

# This is specially provided for Global AI Offensive and Defensive Challenge Track 1：Vaccination for Text-to-Image Generative Models (https://tianchi.aliyun.com/competition/entrance/532268/information?lang=en-us)

import torch
import numpy as np
import pandas as pd
from diffusers import KolorsPipeline, FluxPipeline
from typing import Tuple
from datasets import Dataset
from PIL import Image
from yijian_community.data import load_data, save_data
from yijian_community.model import HFTxt2ImgInfer
from yijian_community.defense import ThuCoaiShieldLM, InternVL2ImageDefense


def text_defense_usage_example(text_defense_model="thu-coai/ShieldLM-7B-internlm2"):
    text_defense = ThuCoaiShieldLM(model_path=text_defense_model)

    # check one text prompt
    text_prompt = "This Sunday will be sunny."
    text_risky = text_defense.infer_data(
        data=text_prompt, lang="en"
    )  # lang should be "en" or "zh" depending on the text_prompt
    print(text_risky)  # text_risky is 0 for safe or 1 for risky

    # check a dataset containing text prompts
    dataset = Dataset.from_dict({"task_id": [1], "task": [text_prompt]})
    dataset_risky = text_defense.infer_dataset(dataset=dataset, target_column="task", batch_size=2, lang="en")
    print(dataset_risky)  # the results are stored in column 'text_risky'
    print(dataset_risky[0])


def txt2img_zh_usage_example(txt2img_zh_model="Kwai-Kolors/Kolors-diffusers"):
    # if you don't have enough GPU power, set memory_reduced to True
    txt2img_zh = HFTxt2ImgInfer(model_path=txt2img_zh_model, pipe=KolorsPipeline, memory_reduced=False, variant="fp16")

    # generate one image
    text_prompt = "今天天气很好。"
    img = txt2img_zh.infer_data(data=text_prompt, guidance_scale=5.0, num_inference_steps=50)
    img.show()

    # generate multiple images and save them on the disk
    dataset = Dataset.from_dict({"task_id": [1], "task": [text_prompt]})
    dataset_img = txt2img_zh.infer_dataset(
        dataset=dataset, target_column="task", batch_size=2, guidance_scale=5.0, num_inference_steps=50
    )
    print(dataset_img)  # the path to saved images are stored in column 'response_image'
    print(dataset_img[0])


class Txt2ImgAttackPipeline:

    def __init__(
        self,
        text_defense_model: str = "thu-coai/ShieldLM-7B-internlm2",
        txt2img_zh_model: str = "Kwai-Kolors/Kolors-diffusers",
        txt2img_en_model: str = "black-forest-labs/FLUX.1-schnell",
        image_defense_model: str = "OpenGVLab/InternVL2-2B",
    ) -> None:
        self.text_defense = ThuCoaiShieldLM(model_path=text_defense_model)
        self.txt2img_zh = HFTxt2ImgInfer(model_path=txt2img_zh_model, pipeline=KolorsPipeline, variant="fp16")
        self.txt2img_en = HFTxt2ImgInfer(model_path=txt2img_en_model, pipeline=FluxPipeline, torch_dtype=torch.bfloat16)
        self.image_defense = InternVL2ImageDefense(model_path=image_defense_model)


if __name__ == "__main__":
    text_defense_usage_example("/yijian/hf_models/thu-coai/ShieldLM-7B-internlm2")
