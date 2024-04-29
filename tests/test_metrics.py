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


import pytest
from evaluator import (
    attack_success_rate,
    decline_rate,
    safety_score,
    accuracy,
    precision,
    recall,
    f1_score,
)
from evaluator import Perplexity, Bleu, Chrf, Ter, RougeSU, Bert


def test_attack_sucess_rate():
    attack_total_num = 100
    attack_success_num = 50
    assert attack_success_rate(attack_total_num, attack_success_num) == pytest.approx(
        0.5
    )


def test_decline_rate():
    query_num = 100
    decline_num = 8
    assert decline_rate(query_num, decline_num) == pytest.approx(0.08)


def test_safety_score():
    attack_total_num = 100
    attack_success_num = 20
    assert safety_score(attack_total_num, attack_success_num) == pytest.approx(0.8)


def test_accuracy():
    ground_truth = [0, 1, 0, 1, 0, 0, 1]
    response = [1, 1, 1, 1, 0, 0, 0]
    assert accuracy(ground_truth, response) == pytest.approx(4 / 7)


def test_precision():
    ground_truth = [0, 1, 0, 1, 0, 0, 1]
    response = [1, 1, 1, 1, 0, 0, 0]
    assert precision(ground_truth, response) == pytest.approx(2 / 4)


def test_recall():
    ground_truth = [0, 1, 0, 1, 0, 0, 1]
    response = [1, 1, 1, 1, 0, 0, 0]
    assert recall(ground_truth, response) == pytest.approx(2 / 3)


def test_f1_score():
    ground_truth = [0, 1, 0, 1, 0, 0, 1]
    response = [1, 1, 1, 1, 0, 0, 0]
    assert f1_score(ground_truth, response) == pytest.approx(12 / 21)


def test_perplexity_zh():
    fluent_sent = "我中午要去吃面"
    unfluent_sent = "的了人吃上看吗人说"
    perplexity = Perplexity(lang="zh")
    assert perplexity(fluent_sent) < perplexity(unfluent_sent)


def test_perplexity_en():
    fluent_sent = "Large language models can achieve remark performances."
    unfluent_sent = "dc jak nkjs skjak dnjks"
    perplexity = Perplexity(lang="en")
    assert perplexity(fluent_sent) < perplexity(unfluent_sent)


def test_Bleu_zh():
    responses = [
        "敏捷的棕色狐狸跳过了懒狗。",
        "敏捷的棕色狐狸跳过了睡着的猫。",
        "每天一个苹果，医生远离我。",
    ]
    references = ["敏捷的棕色狐狸跳过了懒狗。"]
    assert Bleu(responses[0], references, lang="zh") > Bleu(
        responses[1], references, lang="zh"
    ) and Bleu(responses[1], references, lang="zh") > Bleu(
        responses[2], references, lang="zh"
    )


def test_Bleu_en():
    responses = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the sleeping cat.",
        "An apple a day keeps the doctor away.",
    ]
    references = ["The quick brown fox jumps over the lazy dog."]
    assert Bleu(responses[0], references, lang="en") > Bleu(
        responses[1], references, lang="en"
    ) and Bleu(responses[1], references, lang="en") > Bleu(
        responses[2], references, lang="en"
    )


def test_Chrf_zh():
    responses = [
        "敏捷的棕色狐狸跳过了懒狗。",
        "敏捷的棕色狐狸跳过了睡着的猫。",
        "每天一个苹果，医生远离我。",
    ]
    references = ["敏捷的棕色狐狸跳过了懒狗。"]
    assert Chrf(responses[0], references, lang="zh") > Chrf(
        responses[1], references, lang="zh"
    ) and Chrf(responses[1], references, lang="zh") > Chrf(
        responses[2], references, lang="zh"
    )


def test_Chrf_en():
    responses = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the sleeping cat.",
        "An apple a day keeps the doctor away.",
    ]
    references = ["The quick brown fox jumps over the lazy dog."]
    assert Chrf(responses[0], references, lang="en") > Chrf(
        responses[1], references, lang="en"
    ) and Chrf(responses[1], references, lang="en") > Chrf(
        responses[2], references, lang="en"
    )


def test_Ter_zh():
    responses = [
        "敏捷的棕色狐狸跳过了懒狗。",
        "敏捷的棕色狐狸跳过了睡着的猫。",
        "每天一个苹果，医生远离我。",
    ]
    references = ["敏捷的棕色狐狸跳过了懒狗。"]
    assert Ter(responses[0], references, lang="zh") < Ter(
        responses[1], references, lang="zh"
    ) and Ter(responses[1], references, lang="zh") < Ter(
        responses[2], references, lang="zh"
    )


def test_Ter_en():
    responses = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the sleeping cat.",
        "An apple a day keeps the doctor away.",
    ]
    references = ["The quick brown fox jumps over the lazy dog."]
    assert Ter(responses[0], references, lang="en") < Ter(
        responses[1], references, lang="en"
    ) and Ter(responses[1], references, lang="en") < Ter(
        responses[2], references, lang="en"
    )


def test_RougeSU_zh():
    responses = [
        "敏捷的棕色狐狸跳过了懒狗。",
        "敏捷的棕色狐狸跳过了睡着的猫。",
        "每天一个苹果，医生远离我。",
    ]
    references = ["敏捷的棕色狐狸跳过了懒狗。"]
    assert RougeSU(responses[0], references, lang="zh") > RougeSU(
        responses[1], references, lang="zh"
    ) and RougeSU(responses[1], references, lang="zh") > RougeSU(
        responses[2], references, lang="zh"
    )


def test_RougeSU_en():
    responses = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the sleeping cat.",
        "An apple a day keeps the doctor away.",
    ]
    references = ["The quick brown fox jumps over the lazy dog."]
    assert RougeSU(responses[0], references, lang="en") > RougeSU(
        responses[1], references, lang="en"
    ) and RougeSU(responses[1], references, lang="en") > RougeSU(
        responses[2], references, lang="en"
    )


def test_Bert_zh():
    responses = [
        "敏捷的棕色狐狸跳过了懒狗。",
        "敏捷的棕色狐狸跳过了睡着的猫。",
        "每天一个苹果，医生远离我。",
    ]
    references = ["敏捷的棕色狐狸跳过了懒狗。"]
    assert Bert(responses[0], references, lang="zh") > Bert(
        responses[1], references, lang="zh"
    ) and Bert(responses[1], references, lang="zh") > Bert(
        responses[2], references, lang="zh"
    )


def test_Bert_en():
    responses = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the sleeping cat.",
        "An apple a day keeps the doctor away.",
    ]
    references = ["The quick brown fox jumps over the lazy dog."]
    assert Bert(responses[0], references, lang="en") > Bert(
        responses[1], references, lang="en"
    ) and Bert(responses[1], references, lang="en") > Bert(
        responses[2], references, lang="en"
    )
