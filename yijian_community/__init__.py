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


from yijian_community.data import load_data, save_data, save_image
from yijian_community.evaluator import (
    Bert,
    Bleu,
    Chrf,
    NaiveTextSimilarityTagger,
    Perplexity,
    RougeSU,
    Tagger,
    Ter,
    accuracy,
    attack_success_rate,
    decline_rate,
    f1_score,
    precision,
    recall,
    safety_score,
)
from yijian_community.model import (
    AnthropicTxt2TxtInfer,
    BaichuanTxt2TxtInfer,
    CohereTxt2TxtInfer,
    HFTxt2ImgInfer,
    HFTxt2TxtInfer,
    Infer,
    MidJourneyTxt2ImgInfer,
    MoonshotTxt2TxtInfer,
    OpenAITxt2ImgInfer,
    OpenAITxt2TxtInfer,
    StabilityAITxt2ImgInfer,
    TongyiQwenTxt2TxtInfer,
    VLLMTxt2TxtInfer,
)
from yijian_community.technique import BasePromptAttack, TextPromptAttack
