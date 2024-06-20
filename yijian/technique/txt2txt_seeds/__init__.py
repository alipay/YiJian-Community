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


from .introduction import introduction
from .writing_assistant import writing_assistant
from .reverse_induction import reverse_induction
from .step_by_step import step_by_step
from .forced_consent import forced_consent
from .sentence_overflow import sentence_overflow
from .fallacious_premise import fallacious_premise
from .virtualization import virtualization
from .repetition import repetition
from .code_attack import code_attack
from .implicit_knowledge import implicit_knowledge
from .pros_and_cons import pros_and_cons
from .text_summarization import text_summarization


txt2txt_attack_names_zh = (
    "介绍了解",
    "帮忙写作",
    "反向诱导",
    "循序渐进",
    "强制同意",
    "长句溢出",
    "错误前提",
    "虚拟化",
    "口令复述",
    "代码攻击",
    "隐晦知识",
    "正反介绍",
    "文本摘要",
)

txt2txt_attack_names_en = (
    "introduction",
    "writing_assistant",
    "reverse_induction",
    "step_by_step",
    "forced_consent",
    "sentence_overflow",
    "fallacious_premise",
    "virtualization",
    "repetition",
    "code_attack",
    "implicit_knowledge",
    "pros_and_cons",
    "text_summarization",
)

txt2txt_attack_methods = (
    introduction,
    writing_assistant,
    reverse_induction,
    step_by_step,
    forced_consent,
    sentence_overflow,
    fallacious_premise,
    virtualization,
    repetition,
    code_attack,
    implicit_knowledge,
    pros_and_cons,
    text_summarization,
)

# some attacks do not require llms to generate risky prompts
template_based_attacks = ("forced_consent", "sentence_overflow", "text_summarization")

txt2txt_attacks = dict(zip(txt2txt_attack_names_en, txt2txt_attack_methods))
