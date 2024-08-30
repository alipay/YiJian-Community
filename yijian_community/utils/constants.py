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

# parameters for decoding strategies
MAX_NEW_TOKENS = 100
DO_SAMPLE = True
RETURN_FULL_TEXT = False
TEMPERATURE = 0.5
TOP_P = 0.5

# parameters for run evaluations
BATCH_SIZE = 16
DEVICE_MAP = "auto"
SEED = 2024
TORCH_DTYPE = torch.float16

# API keys
OPENAI_API_KEY = "fill in with your openai api key"
