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


from .model import txt2txt_model, txt2img_model, imgtxt2txt_model
from utils import HF, API, CUSTOM, MAX_NEW_TOKENS, RETURN_FULL_TEXT, BATCH_SIZE


# text to text inference
class Txt2TxtInfer:

    def __init__(self, model_name, model_type=HF):
        self.model_name = model_name
        self.model_type = model_type
        self.model = txt2txt_model(
            model_name=self.model_name, model_type=self.model_type
        )

    def inference(self, prompt_text):
        if self.model_type == HF:
            return self.model(
                prompt_text,
                max_new_tokens=MAX_NEW_TOKENS,
                return_full_text=RETURN_FULL_TEXT,
            )[0]["generated_text"]
        if self.model_type == API:
            return
        if self.model_type == CUSTOM:
            return

    def infer_dataset(self, dataset):
        if self.model_type == HF:
            response_texts = self.model(
                dataset["prompt_text"],
                max_new_tokens=MAX_NEW_TOKENS,
                return_full_text=RETURN_FULL_TEXT,
                batch_size=BATCH_SIZE,
            )

            return dataset.add_column(
                "response_text", [r[0]["generated_text"] for r in response_texts]
            )

        if self.model_type == API:
            return
        if self.model_type == CUSTOM:
            return


# text to image inference


# image text to text inference
