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


from yijian_community.technique.txt2txt_seeds.code_attack import code_attack
from yijian_community.technique.txt2txt_seeds.fallacious_premise import (
    fallacious_premise,
)
from yijian_community.technique.txt2txt_seeds.forced_consent import forced_consent
from yijian_community.technique.txt2txt_seeds.implicit_knowledge import (
    implicit_knowledge,
)
from yijian_community.technique.txt2txt_seeds.introduction import introduction
from yijian_community.technique.txt2txt_seeds.pros_and_cons import pros_and_cons
from yijian_community.technique.txt2txt_seeds.repetition import repetition
from yijian_community.technique.txt2txt_seeds.reverse_induction import reverse_induction
from yijian_community.technique.txt2txt_seeds.sentence_overflow import sentence_overflow
from yijian_community.technique.txt2txt_seeds.step_by_step import step_by_step
from yijian_community.technique.txt2txt_seeds.text_summarization import (
    text_summarization,
)
from yijian_community.technique.txt2txt_seeds.virtualization import virtualization
from yijian_community.technique.txt2txt_seeds.writing_assistant import writing_assistant

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
