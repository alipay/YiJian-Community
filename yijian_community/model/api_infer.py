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


from datasets import Dataset

from yijian_community.model.base_infer import Infer
from yijian_community.utils.util_func import console


class APIInfer(Infer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log(
            "This class will be implemented in the next update or you are welcomed to make a contribution."
        )

    def infer_data(self, data: str):
        console.log(
            "This will be implemented in the next update or you are welcomed to make a contribution."
        )

    def infer_dataset(self, dataset: Dataset) -> Dataset:
        console.log(
            "This will be implemented in the next update or you are welcomed to make a contribution."
        )


class OpenAITxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://github.com/openai/openai-python")


class AnthropicTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://github.com/anthropics/anthropic-sdk-python")


class CohereTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://github.com/cohere-ai/cohere-python")


class TongyiQwenTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log(
            "Reference: https://help.aliyun.com/zh/dashscope/developer-reference/api-details"
        )


class MoonshotTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.moonshot.cn/docs/api/chat#基本信息")


class BaichuanTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.baichuan-ai.com/docs/api")


class StabilityAITxt2ImgInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.stability.ai/docs/api-reference")


class OpenAITxt2ImgInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.openai.com/docs/guides/images")


class MidJourneyTxt2ImgInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log(
            "Reference: https://docs.midjourney.com/docs/quick-start or https://github.com/erictik/midjourney-api"
        )
