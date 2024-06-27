# 风险分类体系

<p align="center">
    <img src="./figs/risk_taxonomy_zh.jpeg" width="100%" />
</p>
<font style="color: gray">业务合规与医疗、政务和金融等具体业务场景相关，相较其他三类风险，通用性较弱，此处不做具体说明。</font>

<br>

# 样例数据

为帮助大家快速上手蚁鉴社区版的全流程自动化测评能力，我们从开源数据集（即[Salad-Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)、[jade-db](https://github.com/whitzard-ai/jade-db)、[BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails)、[UltraSafety](https://huggingface.co/datasets/openbmb/UltraSafety)、[cvalues_rlhf](https://huggingface.co/datasets/Skepsun/cvalues_rlhf)、[HarmfulQ](https://github.com/SALT-NLP/chain-of-thought-bias)、[Safety-Prompts](https://huggingface.co/datasets/thu-coai/Safety-Prompts)、[do-not-answer](https://huggingface.co/datasets/LibrAI/do-not-answer)、[toxic-chat](https://huggingface.co/datasets/lmsys/toxic-chat)）中采样了少部分低风险问题，并将每一条问题送入十款开源大模型（即[GOAT-AI/GOAT-7B-Community](https://huggingface.co/GOAT-AI/GOAT-7B-Community)、[microsoft/Orca-2-7b](https://huggingface.co/microsoft/Orca-2-7b)、[stabilityai/StableBeluga-7B](https://huggingface.co/stabilityai/StableBeluga-7B)、[migtissera/SynthIA-7B-v1.3](https://huggingface.co/migtissera/SynthIA-7B-v1.3)、[PygmalionAI/pygmalion-2-7b](https://huggingface.co/PygmalionAI/pygmalion-2-7b)、[Local-Novel-LLM-project/Ninja-v1-NSFW-128k](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-NSFW-128k)、[KoboldAI/OPT-13B-Nerybus-Mix](https://huggingface.co/KoboldAI/OPT-13B-Nerybus-Mix)、[microsoft/Orca-2-13b](https://huggingface.co/microsoft/Orca-2-13b)、[stabilityai/StableBeluga-13B](https://huggingface.co/stabilityai/StableBeluga-13B)、[facebook/opt-13b](https://huggingface.co/facebook/opt-13b)）中获取回复，形成样例测评数据[samples_50_zh.jsonl](../yijian_community/data/samples_50_zh.jsonl)。这些模型经过初步测试，较容易生成风险回复。

<font style="color: gray">我们用于获取风险回复的开源大模型基本能力不足，有时会出现回复语无伦次或重复表述的情况。</font>
<br>

每一条测评数据的格式如下所示：

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

# 更多测评数据

大量安全测评数据（如[SafetyPrompts.com](https://safetyprompts.com/)）已开源，大家可以自行尝试不同的数据发起测评。