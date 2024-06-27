# 风险分类体系

<p align="center">
    <img src="./figs/risk_taxonomy_zh.jpeg" width="100%" />
</p>
<font style="color: gray">业务合规与医疗、政务和金融等具体业务场景相关，相较其他三类风险，通用性较弱，此处不做具体说明。</font>

<br>

# 数据处理

我们下载了[SafetyPrompts.com](https://safetyprompts.com/)上的102个数据集和其他未被其收录的少量开源数据集，通过长度、毒性、风险类别、文本质量等条件筛选并采样后，获取了数万条风险问题，并将其作为我们的benchmark数据集的基础。对于每一条风险问题，我们会通过翻译分别获取中文问题的英文形式和英文问题的中文形式，以此来扩充测评的数据量。

之后对于每一条问题，我们会将其送入十款开源大模型（即[GOAT-AI/GOAT-7B-Community](https://huggingface.co/GOAT-AI/GOAT-7B-Community)、[microsoft/Orca-2-7b](https://huggingface.co/microsoft/Orca-2-7b)、[stabilityai/StableBeluga-7B](https://huggingface.co/stabilityai/StableBeluga-7B)、[migtissera/SynthIA-7B-v1.3](https://huggingface.co/migtissera/SynthIA-7B-v1.3)、[PygmalionAI/pygmalion-2-7b](https://huggingface.co/PygmalionAI/pygmalion-2-7b)、[Local-Novel-LLM-project/Ninja-v1-NSFW-128k](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-NSFW-128k)、[KoboldAI/OPT-13B-Nerybus-Mix](https://huggingface.co/KoboldAI/OPT-13B-Nerybus-Mix)、[microsoft/Orca-2-13b](https://huggingface.co/microsoft/Orca-2-13b)、[stabilityai/StableBeluga-13B](https://huggingface.co/stabilityai/StableBeluga-13B)、[facebook/opt-13b](https://huggingface.co/facebook/opt-13b)）中，这些模型经过初步测试，较容易生成风险回复。我们采纳的风险问题的具体来源有：

| Name    | License |
|--------------------|:---------:|
| [Salad-Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)          |     Apache-2.0    |
| [SafetyPrompts](https://huggingface.co/datasets/thu-coai/Safety-Prompts)       |    Apache-2.0     |
| [CValuesResponsibilityPrompts](https://huggingface.co/datasets/Skepsun/cvalues_rlhf)               |    Apache-2.0     |
| [BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails)         |    CC-BY-NC-4.0     |
| [JADE](https://github.com/whitzard-ai/jade-db)                |    MIT     |
| [UltraSafety](https://huggingface.co/datasets/openbmb/UltraSafety)         |   MIT      |
| [AART](https://github.com/google-research-datasets/aart-ai-safety-dataset)                |    CC-BY-4.0     |
| [HarmfulQA](https://huggingface.co/datasets/declare-lab/HarmfulQA)           |     Apache-2.0    |
| [ParlAIDialogueSafety](https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks/dialogue_safety)|     MIT    |
| [PKU-SafeRLHF](https://hf-mirror.com/datasets/PKU-Alignment/PKU-SafeRLHF)        |    CC-BY-NC-4.0     |
| [DoNotAnswer](https://huggingface.co/datasets/LibrAI/do-not-answer)         |     Apache-2.0    |
| [SafetyTunedLLaMAs](https://github.com/vinid/safety-tuned-llamas)   |    CC-BY-NC-4.0     |
| [BeaverTails-Evaluation](https://hf-mirror.com/datasets/PKU-Alignment/BeaverTails-Evaluation)    |    CC-BY-NC-4.0     |
| [AdvBench](https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench)            |     MIT    |
| [HarmfulQ](https://github.com/SALT-NLP/chain-of-thought-bias)            |    unspecified     |
| [XSTest](https://huggingface.co/datasets/natolambert/xstest-v2-copy)              |    CC-BY-4.0     |
| [TruthfulQA](https://huggingface.co/datasets/truthfulqa/truthful_qa)          |     Apache-2.0    |
| [StrongREJECT](https://github.com/alexandrasouly/strongreject/tree/main)        |    MIT    |
| [DecodingTrust](https://huggingface.co/datasets/AI-Secure/DecodingTrust)       |    CC-BY-SA-4.0     |
| [Cyber​​attackAssistance](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks/datasets/mitre)    |    MIT     |
| [MaliciousInstruct](https://github.com/Princeton-SysML/Jailbreak_LLM/tree/main/data)   |    unspecified     |
| [HarmBench](https://github.com/centerforaisafety/HarmBench/tree/main/data/behavior_datasets)           |    MIT     |
| [SimpleSafetyTests](https://huggingface.co/datasets/Bertievidgen/SimpleSafetyTests)   |    CC-BY-2.0     |
| [ToxicChat](https://huggingface.co/datasets/lmsys/toxic-chat)           |     CC-BY-NC-4.0    |
| [HExPHI](https://huggingface.co/datasets/LLM-Tuning-Safety/HEx-PHI)              |    HEx-PHI License (custom)    |
| [CPAD](https://github.com/liuchengyuan123/CPAD)                |    CC-BY-4.0     |
| [ConvAbuse](https://github.com/amandacurry/convabuse)           |     CC-BY-4.0     |
| [TDCRedTeaming](https://github.com/centerforaisafety/tdc2023-starter-kit/tree/main/red_teaming/data)       |    MIT     |
|||

<br>

# 数据格式

```json
{
    "prompt_text": "风险问题",
    "source": "风险问题的来源",
    "references": [
    {
        "text": "由response_model针对prompt_text生成的回复",
        "response_model": "产生text的大模型名称",
        "label": "有无风险，1表示有风险，0表示无风险"
    },
    {
        "text": "",
        "response_model": "",
        "label": ""
    },
    ···
    ]
}
```

<font style="color: gray">references字段主要用于基于相似度的自动化测评方法，若采用其他测评方案，可省略。</font>
<br>

# 样例数据

完整的benchmark数据集包含大量风险问题和风险回复，目前尚未经过完备的审计。为避免不必要的内外部合规风险，我们开源少部分低风险数据，便于大家快速上手蚁鉴社区版的全流程自动化测评能力。中英文样例测评数据分别存于[samples_50_zh.jsonl](../yijian_community/data/samples_50_zh.jsonl)和[samples_50_en.jsonl](../yijian_community/data/samples_50_en.jsonl)中。

<font style="color: gray">我们用于获取风险回复的开源大模型基本能力不足，有时会出现回复语无伦次或重复表述的情况。</font>
<br>

# 其他测评数据

大量安全测评数据（如[SafetyPrompts.com](https://safetyprompts.com/)）已开源，大家可以自行尝试不同的数据发起测评。若在测评过程中，发现蚁鉴社区版的问题，欢迎且感谢反馈！