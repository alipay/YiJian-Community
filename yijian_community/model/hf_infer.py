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
from datetime import datetime

import torch
from datasets import Dataset
from diffusers import DiffusionPipeline
from numpy import dtype
from PIL import Image
from tqdm import tqdm
from transformers import pipeline
from vllm import LLM, SamplingParams

from yijian_community.data import save_image
from yijian_community.model.base_infer import Infer
from yijian_community.utils import (
    BATCH_SIZE,
    DEVICE_MAP,
    DO_SAMPLE,
    MAX_NEW_TOKENS,
    RETURN_FULL_TEXT,
    SEED,
    TEMPERATURE,
    TOP_P,
    TORCH_DTYPE,
    console,
)


class HFTxt2TxtInfer(Infer):

    def __init__(self, model_path: str, **kwargs):
        """initialization for model inference with transformers.

        Args:
            model_path (str): path to the target model.
        """
        super().__init__(model_path)
        try:
            self.infer = pipeline(
                "text-generation", model=model_path, device_map=DEVICE_MAP, **kwargs
            )
        except Exception as e:
            console.log(e)
            console.log("reloading model ...")
            self.infer = pipeline("text-generation", model=model_path, **kwargs)

    def infer_data(
        self,
        data: str,
        max_new_tokens: int = MAX_NEW_TOKENS,
        do_sample: bool = DO_SAMPLE,
        temperature: float = TEMPERATURE,
        **kwargs,
    ) -> str:
        """

        Args:
            data (str): input text, also known as a query or a prompt.
            max_new_tokens (int, optional): max number of new tokens that the target model can generate. Defaults to MAX_NEW_TOKENS.
            do_sample (bool, optional): whether or not to use sampling. Defaults to DO_SAMPLE.
            temperature (float, optional): used to module the probabilities of next token. Defaults to TEMPERATURE.

        Returns:
            str: an output text, also known as a response.
        """
        return self.infer(
            data,
            max_new_tokens=max_new_tokens,
            return_full_text=RETURN_FULL_TEXT,
            do_sample=do_sample,
            temperature=temperature,
            **kwargs,
        )[0]["generated_text"]

    def infer_dataset(
        self,
        dataset: Dataset,
        target_column: str = "prompt_text",
        batch_size: int = BATCH_SIZE,
        max_new_tokens: int = MAX_NEW_TOKENS,
        do_sample: bool = DO_SAMPLE,
        temperature: float = TEMPERATURE,
        **kwargs,
    ) -> Dataset:
        """

        Args:
            dataset (Dataset): input dataset, containing text prompts.
            target_column (str, optional): the name of the column which stores the text prompts. Defaults to "prompt_text".
            batch_size (int, optional): batch size. Defaults to BATCH_SIZE.
            max_new_tokens (int, optional): maximum number of new tokens that the target model can generate. Defaults to MAX_NEW_TOKENS.
            do_sample (bool, optional): whether or not to use sampling. Defaults to DO_SAMPLE.
            temperature (float, optional): used to module the probabilities of next token. Defaults to TEMPERATURE.

        Returns:
            Dataset: output dataset, containing responses stored in a column named "response_text".
        """
        if not self.infer.tokenizer.pad_token:
            self.infer.tokenizer.pad_token_id = self.infer.model.config.eos_token_id
        if not self.infer.model.config.is_encoder_decoder:
            self.infer.tokenizer.padding_side = "left"

        res = self.infer(
            dataset[target_column],
            batch_size=batch_size,
            max_new_tokens=max_new_tokens,
            return_full_text=RETURN_FULL_TEXT,
            do_sample=do_sample,
            temperature=temperature,
            **kwargs,
        )

        response_texts = [r[0]["generated_text"] for r in res]

        return dataset.add_column("response_text", response_texts)


class VLLMTxt2TxtInfer(Infer):

    def __init__(
        self,
        model_path: str,
        temperature: float = TEMPERATURE,
        top_p: float = TOP_P,
        max_tokens=MAX_NEW_TOKENS,
        **kwargs,
    ):
        """initialization for model inference with vLLM.

        Args:
            model_path (str): path to the target model.
            temperature (float, optional): used to module the probabilities of next token. Defaults to TEMPERATURE.
            top_p (float, optional): controls the number of top tokens to consider. Defaults to TOP_P.
            max_tokens (_type_, optional): maximum number of tokens to generate. Defaults to MAX_NEW_TOKENS.
        """
        super().__init__(model_path)
        self.sampling_params = SamplingParams(
            temperature=temperature, top_p=top_p, max_tokens=max_tokens
        )
        self.infer = LLM(model=model_path, **kwargs)

    def infer_data(self, data: str) -> str:
        """

        Args:
            data (str): input text, also known as a query or a prompt.

        Returns:
            str: an output text, also known as a response.
        """
        return self.infer.generate(data, self.sampling_params)[0].outputs[0].text

    def infer_dataset(
        self,
        dataset: Dataset,
        target_column: str = "prompt_text",
        batch_size: int = BATCH_SIZE,
    ) -> Dataset:
        """

        Args:
            dataset (Dataset): input dataset, containing text prompts.
            target_column (str, optional): the name of the column which stores the text prompts. Defaults to "prompt_text".
            batch_size (int, optional): batch size. Defaults to BATCH_SIZE.

        Returns:
            Dataset: output dataset, containing responses stored in a column named "response_text".
        """

        response_texts = []
        for data in dataset.iter(batch_size=batch_size):
            outputs = self.infer.generate(data[target_column], self.sampling_params)
            response_texts.extend([output.outputs[0].text for output in outputs])
        return dataset.add_column("response_text", response_texts)


class HFTxt2ImgInfer(Infer):

    def __init__(
        self,
        model_path: str,
        pipe: DiffusionPipeline = DiffusionPipeline,
        torch_dtype: dtype = TORCH_DTYPE,
        seed: int = SEED,
        memory_reduced: bool = True,
        **kwargs,
    ):
        """initialization for model inference with diffusers.

        Args:
            model_path (str): path to the target model.
            torch_dtype (dtype, optional): model's dtype. Defaults to TORCH_DTYPE.
        """
        super().__init__(model_path)

        self.infer = pipe.from_pretrained(
            model_path,
            torch_dtype=torch_dtype,
            **kwargs,
        )

        if memory_reduced:
            self.infer.enable_model_cpu_offload()
        else:
            self.infer = self.infer.to("cuda")

        self.generator = torch.Generator(self.infer.device).manual_seed(seed)

    def infer_data(
        self,
        data: str,
        **kwargs,
    ) -> Image.Image:
        """

        Args:
            data (str): input text, also known as a query or a prompt.

        Returns:
            Image.Image: response image.
        """
        img = self.infer(data, generator=self.generator, **kwargs).images[0]
        torch.cuda.empty_cache()
        return img

    def infer_dataset(
        self,
        dataset: Dataset,
        target_column: str = "prompt_text",
        batch_size: int = BATCH_SIZE,
        **kwargs,
    ) -> Dataset:
        """

        Args:
            dataset (Dataset): input dataset, containing text prompts.
            batch_size (int, optional): batch size. Defaults to BATCH_SIZE.

        Returns:
            Dataset: output dataset, containing responses stored in a column named "response_image".
        """
        image_save_path = os.path.join(
            os.getcwd(),
            "txt2img_"
            + self.model_path.split("/")[-1]
            + "_"
            + datetime.now().strftime("%Y%m%d_%H%M%S"),
        )
        os.makedirs(image_save_path, exist_ok=True)

        response_images = []
        for data in tqdm(dataset.iter(batch_size=batch_size)):
            images = self.infer(
                data[target_column], generator=self.generator, **kwargs
            ).images
            response_images.extend(
                save_image(image_save_path, data[target_column], images)
            )
            torch.cuda.empty_cache()
        return dataset.add_column("response_image", response_images)
