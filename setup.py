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


from setuptools import find_packages, setup


def read_requirements():
    with open("./requirements.txt") as file:
        requirements = file.read().splitlines()
    return requirements


def long_description():
    with open("./README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="yijian",
    version="0.1.0",
    license="Apache 2.0",
    description="YiJian",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="Ant Group",
    url="https://acta.alipay.com/detect/security",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.8",
)