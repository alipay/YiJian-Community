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

from yijian_community.data import load_data, save_data
from yijian_community.model import HFTxt2ImgInfer
from yijian_community.defense import ThuCoaiShieldLM, InternVL2ImageDefense


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

    def attack_data(self, data: str) -> Tuple[int, str, int]:
        pass

    def attack_dataset(self, dataset: Dataset) -> Dataset:
        pass
