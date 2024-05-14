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


import os
from model.base_infer import Infer
from utils import OPENAI_API_KEY, BATCH_SIZE, TEMPERATURE, MAX_NEW_TOKENS
from openai import OpenAI
from datasets import Dataset
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)


class OpenAITxt2TxtInfer(Infer):

    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        """

        Args:
            model_name (str): can be one of the models listed in https://platform.openai.com/docs/models
        """
        super().__init__(model_name)
        self.model_name = model_name
        self.model = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY))

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def completion_with_backoff(self, **kwargs):
        return self.model.completions.create(**kwargs)

    def infer_dataset(
        self,
        dataset: Dataset,
        batch_size: int = BATCH_SIZE,
        temperature: float = TEMPERATURE,
        **kwargs
    ):
        response_texts = []
        dataset_len = len(dataset)
        i = 0
        while i * batch_size < dataset_len:
            responses = self.completion_with_backoff(
                model=self.model_name,
                prompt=dataset["prompt_text"][i * batch_size : (i + 1) * batch_size],
                max_tokens=MAX_NEW_TOKENS,
                temperature=temperature,
            )
            answers = [""] * min(batch_size, dataset_len - i * batch_size)
            for choice in responses.choices:
                answers[choice.index] = choice.text
            response_texts.extend(answers[:])
        return dataset.add_column("response_text", response_texts)
