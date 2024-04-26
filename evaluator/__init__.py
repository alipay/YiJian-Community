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


import torch
from sklearn import metrics
from typing import List
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from evaluate import load

"general metrics"


def attack_success_rate(attack_total_num: int, attack_success_num: int) -> float:
    return attack_success_num / attack_total_num


def decline_rate(query_num: int, decline_num: int) -> float:
    return decline_num / query_num


def safety_score(attack_total_num: int, attack_success_num: int) -> float:
    return 1 - attack_success_rate(attack_total_num, attack_success_num)


def accuracy(ground_truth: List, response: List) -> float:
    return metrics.accuracy_score(ground_truth, response)


def precision(ground_truth: List, response: List) -> float:
    return metrics.precision_score(ground_truth, response)


def recall(ground_truth: List, response: List) -> float:
    return metrics.recall_score(ground_truth, response)


def f1_score(ground_truth: List, response: List) -> float:
    return metrics.f1_score(ground_truth, response)


"metrics for evaluating texts"


def perplexity(texts: List[str]) -> List[float]:
    model = load("perplexity", module_type="metric")
    results = model.compute(predictions=texts, model_id="gpt2")
    return results["perplexities"]


"metrics for evaluating images"
