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


from yijian_community.technique.txt2img_seeds.fallacious_premise import (
    fallacious_premise,
)
from yijian_community.technique.txt2img_seeds.info_compression import info_compression
from yijian_community.technique.txt2img_seeds.info_expansion import info_expansion
from yijian_community.technique.txt2img_seeds.keyword_extraction import (
    keyword_extraction,
)
from yijian_community.technique.txt2img_seeds.reverse_induction import reverse_induction

txt2img_attack_names_zh = ("错误前提", "反向诱导", "信息压缩", "信息扩展", "关键字提取")

txt2img_attack_names_en = (
    "fallacious_premise",
    "reverse_induction",
    "info_compression",
    "info_expansion",
    "keyword_extraction",
)

txt2img_attack_methods = (
    fallacious_premise,
    reverse_induction,
    info_compression,
    info_expansion,
    keyword_extraction,
)

txt2img_attacks = dict(zip(txt2img_attack_names_en, txt2img_attack_methods))
