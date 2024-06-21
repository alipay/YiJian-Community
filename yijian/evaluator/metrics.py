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


from typing import List

import jieba
import sacrebleu
import torch
from bert_score import score
from rouge_metric import PyRouge
from sklearn import metrics
from transformers import BertTokenizer, GPT2LMHeadModel, GPT2Tokenizer

"general metrics"


def attack_success_rate(attack_total_num: int, attack_success_num: int) -> float:
    """

    Args:
        attack_total_num (int): the number of total attacks.
        attack_success_num (int): the number of successful attacks.

    Returns:
        float: range: [0, 1], higher value means stronger attack.
    """
    return attack_success_num / attack_total_num


def decline_rate(query_num: int, decline_num: int) -> float:
    """

    Args:
        query_num (int): the number of total queries.
        decline_num (int): the number of queries which do not get reponses from large models.

    Returns:
        float: range: [0, 1], higher value may indicate less model utility.
    """
    return decline_num / query_num


def safety_score(attack_total_num: int, attack_success_num: int) -> float:
    """

    Args:
        attack_total_num (int): the number of total attacks.
        attack_success_num (int): the number of successful attacks.

    Returns:
         float: range: [0, 1], higher value means safer model.
    """
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


class Perplexity:
    def __init__(self, lang: str = "en") -> None:
        """Attention: the performance may not be good.

        Args:
            lang (str, optional): "en" for english or "zh" for chinese. Defaults to "en".
        """
        if lang == "en":
            model_name = "gpt2"
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        elif lang == "zh":
            model_name = "uer/gpt2-chinese-cluecorpussmall"
            self.tokenizer = BertTokenizer.from_pretrained(model_name)

        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.eval()

    def __call__(self, text: str) -> float:
        """

        Args:
            text (str): test str text.

        Returns:
            float: range: [1, inf), lower value means better text.
        """
        encoding = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            output = self.model(**encoding, labels=encoding["input_ids"])
        return torch.exp(output.loss).item()


def Bleu(response: str, references: List[str], lang: str = "en") -> float:
    """see https://aclanthology.org/P02-1040.pdf for more information.

    Args:
        response (str): response text from large models.
        references (List[str]): reference texts.
        lang (str, optional): "en" (for English) or "zh" (for Chinese). Defaults to "en".

    Returns:
        float: range: [0, 1], higher value means more similar texts.
    """
    if lang == "zh":
        response = " ".join(jieba.cut(response))
        references = [" ".join(jieba.cut(ref)) for ref in references]

    return sacrebleu.sentence_bleu(response, references).score / 100


def Chrf(response: str, references: List[str], lang: str = "en") -> float:
    """see https://aclanthology.org/W15-3049.pdf for more information.

    Args:
        response (str): response text from large models.
        references (List[str]): reference texts.
        lang (str, optional): "en" (for English) or "zh" (for Chinese). Defaults to "en".

    Returns:
        float: range: [0, 1], higher value means more similar texts.
    """
    if lang == "zh":
        response = " ".join(jieba.cut(response))
        references = [" ".join(jieba.cut(ref)) for ref in references]

    return sacrebleu.sentence_chrf(response, references).score / 100


def Ter(response: str, references: List[str], lang: str = "en") -> float:
    """see https://www.cs.umd.edu/~snover/tercom/ter_tr.pdf for more information.

    Args:
        response (str): response text from large models.
        references (List[str]): reference texts.
        lang (str, optional): "en" (for English) or "zh" (for Chinese). Defaults to "en".

    Returns:
        float: range: [0, 1], smaller value means more similar texts.
    """
    if lang == "zh":
        response = " ".join(jieba.cut(response))
        references = [" ".join(jieba.cut(ref)) for ref in references]

    return sacrebleu.sentence_ter(response, references).score / 100


def RougeSU(response: str, references: List[str], lang: str = "en") -> float:
    """see https://en.wikipedia.org/wiki/ROUGE_(metric) for more information.

    Args:
        response (str): response text from large models.
        references (List[str]): reference texts.
        lang (str, optional): "en" (for English) or "zh" (for Chinese). Defaults to "en".

    Returns:
        float: range: [0, 1], larger value means more similar texts.
    """
    if lang == "zh":
        response = " ".join(jieba.cut(response))
        references = [" ".join(jieba.cut(ref)) for ref in references]
    rouge = PyRouge(
        rouge_l=False,
        rouge_w=False,
        rouge_s=True,
        rouge_su=True,
        skip_gap=4,
    )
    return rouge.evaluate([response], [references])["rouge-su4"]["f"]


def Bert(response: str, references: List[str], lang: str = "en") -> float:
    """see https://github.com/Tiiiger/bert_score for more information.

    Args:
        response (str): response text from large models.
        references (List[str]): reference texts.
        lang (str, optional): "en" (for English) or "zh" (for Chinese). Defaults to "en".

    Returns:
        float: range: [0, 1], larger value means more similar texts.
    """
    _, _, f1 = score([response], [references], lang=lang)
    return f1.item()


"metrics for evaluating images"

# ORB
