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
from datasets import Dataset
from diffusers import FluxPipeline, KolorsPipeline
from lmdeploy.vl import load_image

from yijian_community.data import load_data, save_data
from yijian_community.defense import InternVL2ImageDefense, ThuCoaiShieldLM
from yijian_community.model import HFTxt2ImgInfer


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
    dataset_risky = text_defense.infer_dataset(
        dataset=dataset, target_column="task", batch_size=2, lang="en"
    )
    print(dataset_risky)  # the results are stored in column 'text_risky'
    print(dataset_risky[0])


def txt2img_zh_usage_example(txt2img_zh_model="Kwai-Kolors/Kolors-diffusers"):
    # if you don't have enough GPU power, set memory_reduced to True
    txt2img_zh = HFTxt2ImgInfer(
        model_path=txt2img_zh_model,
        pipe=KolorsPipeline,
        memory_reduced=False,
        variant="fp16",
    )

    # generate one image
    text_prompt = "今天天气很好。"
    img = txt2img_zh.infer_data(
        data=text_prompt, guidance_scale=5.0, num_inference_steps=50
    )
    img.show()

    # generate multiple images and save them on the disk
    dataset = Dataset.from_dict({"task_id": [1], "task": [text_prompt]})
    dataset_img = txt2img_zh.infer_dataset(
        dataset=dataset,
        target_column="task",
        batch_size=2,
        guidance_scale=5.0,
        num_inference_steps=50,
    )
    print(dataset_img)  # the path to saved images are stored in column 'response_image'
    print(dataset_img[0])


def txt2img_en_usage_example(txt2img_en_model="black-forest-labs/FLUX.1-schnell"):
    # if you don't have enough GPU power, set memory_reduced to True
    txt2img_en = HFTxt2ImgInfer(
        model_path=txt2img_en_model,
        pipe=FluxPipeline,
        memory_reduced=False,
        torch_dtype=torch.bfloat16,
    )

    # generate one image
    text_prompt = "This Sunday will be sunny."
    img = txt2img_en.infer_data(
        data=text_prompt,
        guidance_scale=0.0,
        num_inference_steps=5,
        max_sequence_length=256,
    )
    img.show()

    # generate multiple images and save them on the disk
    dataset = Dataset.from_dict({"task_id": [1], "task": [text_prompt]})
    dataset_img = txt2img_en.infer_dataset(
        dataset=dataset,
        target_column="task",
        batch_size=2,
        guidance_scale=0.0,
        num_inference_steps=5,
        max_sequence_length=256,
    )
    print(dataset_img)  # the path to saved images are stored in column 'response_image'
    print(dataset_img[0])


def image_defense_usage_example(image_defense_model="OpenGVLab/InternVL2-2B"):
    image_defense = InternVL2ImageDefense(model_path=image_defense_model)
    text_prompt = "This Sunday will be sunny."

    # check single image with image path
    img_path = "./This Sunday will be sunny..jpg"
    img_risky = image_defense.infer_data(img_path)
    print(img_risky)  # img_risky is 0 for safe or 1 for risky

    # check single image with Image Instance
    img = load_image(img_path)
    img_risky = image_defense.infer_data(img_path)
    print(img_risky)

    # check a dataset containing image paths
    dataset = Dataset.from_dict(
        {"task_id": [1], "task": [text_prompt], "response_image": [img_path]}
    )
    dataset_risky = image_defense.infer_dataset(
        dataset=dataset, target_column="response_image", batch_size=2
    )
    print(dataset_risky)  # the results are stored in column 'text_risky'
    print(dataset_risky[0])
