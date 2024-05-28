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


from .constants import MAX_NEW_TOKENS, DO_SAMPLE, RETURN_FULL_TEXT, TEMPERATURE
from .constants import HF, API, CUSTOM
from .constants import BATCH_SIZE, DEVICE_MAP, USE_SAFETENSORS, SEED, TORCH_DTYPE
from .constants import OPENAI_API_KEY
from .util import save_images_and_return_paths, get_image_from_url
