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


from yijian.data import load_data, save_data, save_image
from yijian.model import Infer, HFTxt2TxtInfer, VLLMTxt2TxtInfer, HFTxt2ImgInfer
from yijian.model import (
    OpenAITxt2TxtInfer,
    AnthropicTxt2TxtInfer,
    CohereTxt2TxtInfer,
    TongyiQwenTxt2TxtInfer,
    MoonshotTxt2TxtInfer,
    BaichuanTxt2TxtInfer,
)
from yijian.model import StabilityAITxt2ImgInfer, OpenAITxt2ImgInfer, MidJourneyTxt2ImgInfer
from yijian.evaluator import (
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
from yijian.technique import BasePromptAttack, TextPromptAttack
