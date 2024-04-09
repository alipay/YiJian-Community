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


from typing import Dict


class PromptRecord:

    def __init__(
        self,
        input_text: str,
        input_image: str = None,
        risk_type: Dict = None,
        lang: str = "zh",
        output_text: str = None,
        output_image: str = None,
    ) -> None:
        """

        Args:
            input_text (str): text prompt
            input_image (str, optional): a path or an url to an image. Defaults to None.
            risk_type (Dict, optional): a dict denoting the risk type of the input prompt, the format as follows,
            {
                primary: (no_risk, content_security, data_security, tech_ethics),
                secondary: (...),
                tertiary: (...)
            }. Primary, secondary and tertiary represent the different level of categories. Defaults to None.
            lang (str, optional): can be "zh" or "en", depending on the language of input_text. Defaults to "zh".
            output_text (str, optional): text response from target large models. Defaults to None.
            output_image (str, optional): a path or an url to the generated image response. Defaults to None.
        """
        self.input_text = input_text
        self.input_image = input_image
        self.risk_type = risk_type
        self.lang = lang
        self.output_text = output_text
        self.output_image = output_image
