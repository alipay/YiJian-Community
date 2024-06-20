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


from .data import load_data, save_data, save_image
from .model import Infer, HFTxt2TxtInfer, VLLMTxt2TxtInfer, HFTxt2ImgInfer, OpenAITxt2TxtInfer
from .evaluator import (
    attack_success_rate,
    decline_rate,
    safety_score,
    accuracy,
    precision,
    recall,
    f1_score,
    Perplexity,
    Bleu,
    Chrf,
    Ter,
    RougeSU,
    Bert,
    Tagger,
    NaiveTextSimilarityTagger,
)
from .technique import TextPromptAttack