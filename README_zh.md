# 蚁鉴：工业级大模型安全测评工具

<p align="center">
  <img src="./docs/figs/logo.png" width="100%" />
</p>

<div align="center">

[**English**](README.md)
</div>

## 蚁鉴是什么？
### 蚁鉴平台
针对大模型幻觉、意识形态及隐私等风险，依据国内外法律法规、学术研究和企业需求，蚁鉴构建了一套全面的风险分类标准，开发了诱导式对抗检测技术，通过模拟黑客攻击，对大模型进行实时自动化检测，识别潜在的弱点和安全问题。

<p align="center">
  <img src="./docs/figs/yijian_zh.jpg" width="100%" />
  <text> <b>平台架构</b> </text>
</p>
 
蚁鉴平台提供了全面、智能、高效、易用的工业级大模型安全测评能力。
- **全面**
  - 测评数据：千亿级安全领域风险数据
  - 风险分类体系：内容安全、数据安全、伦理安全和合规安全4大类，200+子类
  - 数据模态：文本、图像、音频、视频
  - 测评对象：基座大模型、领域大模型、Agent
  - 攻击方法：50+种前沿攻击
- **智能**
  - 测试数据智能生成
  - 风险、拒答、攻击方法智能识别
- **高效**
  - 每日百亿级风险初筛
  - 每日亿级数据精细化标注
  - 小时级测评报告生成
- **易用**
  - 一站式测评，仅需注册账户和提供模型API接口即可发起测评

### 蚁鉴开源

**本项目仅用于测评和提升大模型的安全性，其中包含若干违法违规内容，均不代表本团队任何主观观点。**

大模型安全测评的重要性已达成业界共识，为促进该领域的发展，我们特此开源全流程的测评工具。

<p align="center">
  <img src="./docs/figs/yijian_opensource_zh.png" width="100%" />
  <text> <b>项目概览</b> </text>
</p>

测评核心组件有：
- **`data`**
  - 提供<font style="background: yellow">X</font>条全风险测评问题，问题来源于100+开源数据集，经过长度、毒性、类别等条件筛选并采样后得到。每条prompt辅以5～12条不等的大模型response，prompt和response皆有中英文形式，分别存于`YiJian_Benchmark_zh.jsonl`和`YiJian_Benchmark_en.jsonl`中。每条数据格式如下所示：
    ```json
    {
      "prompt_text": "风险问题",
      "source": "风险问题的来源",
      "references": [
        {
          "text": "由response_model针对prompt_text生成的回复",
          "response_model": "产生text的大模型名称",
          "embedding": "text的文本嵌入",
          "label": "有无风险，1表示有风险，0表示无风险"
        },
        {
          "text": "",
          "response_model": "",
          "embedding": "",
          "label": ""
        },
        ···
      ]
    }
    ```
    风险分类体系如下所示：
    <p align="center">
      <img src="./docs/figs/risk_taxonomy_zh.jpeg" width="100%" />
      <text> <b>风险分类</b> </text>
    </p>
    <font style="color: gray">注意：业务合规与医疗、政务和金融等具体业务场景相关，相较其他三类风险，通用性较弱，此处不做具体说明。</font>
  - 原生支持csv、json和parquet格式的数据
  - 其他类型文件可转为上述三种文件格式使用，或编写脚本将数据加载为[datasets.Dataset](https://huggingface.co/docs/datasets/v2.19.0/en/package_reference/main_classes#datasets.Dataset)的实例
- **`technique`**
  - 提供13种针对文生文大模型的对抗攻击手法实现和7种手法介绍
  - 提供5种针对文生图大模型的对抗攻击手法实现和4种手法介绍
- **`model`**
  - 支持Hugging Face上所有文生文和文生图大模型的加载与推理
  - 支持主流闭源大模型的API访问，如ChatGPT和GPT-4
  - 支持其他任意格式的模型加载与推理（需继承适配model组件的[Infer](./model/base_infer.py)基础类）
- **`evaluator`**
  - 提供多样的大模型安全测评指标，如攻击成功率和拒答率等
  - 提供轻量级的自动化风险判断方法
  - 支持[JailbreakEval](https://github.com/ThuCCSLab/JailbreakEval)

针对待测模型，通过配置上述4个组件（technique非必需），即可实现自动化测评。

## 如何使用？

### 安装

### 快速启动

1. 测评数据加载
   ```python
   from yijian.data import load_data
   test_set = load_data("path/to/eval_base_zh.jsonl")
   # 风险问题所在列为prompt_text
   ```
2. 数据攻击增强（可选）
   ```python
   from yijian.technique import TextPromptAttack
   prompt_attack = TextPromptAttack("LLM instance or API", lang="zh")
   aug_test_set = prompt_attack.attack_dataset(test_set, techniques=None)
   # 如果未指定techniques，默认将使用全部的攻击手法进行样本增强
   ```
   攻击列表详见[readme_txt2txt_zh.md](./technique/readme_txt2txt_zh.md)。
3. 待测模型配置
   ```python
   from yijian.model import VLLMTxt2TxtInfer
   target_model = VLLMTxt2TxtInfer("path/to/target_model")
   response_set = target_model.infer_dataset(test_set, batch_size=32, target_column="prompt_text")
   # 若加载自定义数据集，或需更改target_column为风险问题所在的列名
   ```
4. 发起测评
   ```python
   from evaluator import 
   ```

### 高级功能
若需进行更全面准确或定制化的测评，可申请使用[蚁鉴平台](https://acta.alipay.com/detect/security)。

## 重要事项

### 🗓 2024年7月
- 蚁鉴开源！

## 相关文档

## 贡献
大模型发展势不可挡，大模型安全必不可少，我们期待更多人一起加入，共建蚁鉴开源生态，为大模型和人工智能保驾护航。

## 联系我们
建设中，敬请期待！
