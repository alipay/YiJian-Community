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
import asyncio
from datasets.arrow_dataset import Dataset
from .base_infer import Infer
from openai import AsyncOpenAI, OpenAI
from utils import BATCH_SIZE, MAX_NEW_TOKENS, TEMPERATURE, TOP_P


class OpenAITxt2TxtInfer(Infer):

    def __init__(self, model_path: str):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("api_key = ", api_key)
            raise ValueError(
                "Invalid OPENAI_API_KEY, please check whether is has been set properly!"
            )

        self.infer = OpenAI(api_key=api_key)
        self.model = model_path

    def infer_data(
        self,
        data: str,
        max_tokens: int = MAX_NEW_TOKENS,
        temperature: float = TEMPERATURE,
        top_p: int = TOP_P,
        **kwargs
    ):
        response = self.infer.chat.completions.create(
            messages=[{"role": "user", "content": data}],
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            **kwargs
        )
        return response.choices[0].message.content

    def infer_dataset(
        self,
        dataset: Dataset,
        target_column: str = "prompt_text",
        batch_size: int = BATCH_SIZE,
        max_tokens: int = MAX_NEW_TOKENS,
        temperature: float = TEMPERATURE,
        top_p: int = TOP_P,
        **kwargs
    ) -> Dataset:

        response_texts = []

        for data in dataset.iter(batch_size=batch_size):
            responses = self.infer.chat.completions.create(messages="")
            outputs = self.infer.generate(data[target_column], self.sampling_params)
            response_texts.extend([output.outputs[0].text for output in outputs])
        return dataset.add_column("response_text", response_texts)
