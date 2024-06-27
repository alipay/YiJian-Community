# Risk Taxonomy

<p align="center">
    <img src="./figs/risk_taxonomy_en.jpeg" width="100%" />
</p>
<font style="color: gray">Business compliance is related to specific business scenarios such as healthcare, government affairs, and finance. Compared with the other three types of risks, it is less universal and will not be explained in detail here.</font>

<br>

# Data Process

We downloaded 102 datasets from [SafetyPrompts.com](https://safetyprompts.com/) and a small number of other open-source datasets not included by them. After filtering and sampling based on criteria such as length, toxicity, risk category, and text quality, we obtained tens of thousands of risk-related questions, which serve as the foundation for our benchmark dataset. For each risk-related question, we translate it to obtain the English version of the Chinese question and the Chinese version of the English question, thereby expanding the volume of the evaluation data.

For each question, we then input it into ten open-source large models ([GOAT-AI/GOAT-7B-Community](https://huggingface.co/GOAT-AI/GOAT-7B-Community), [microsoft/Orca-2-7b](https://huggingface.co/microsoft/Orca-2-7b), [stabilityai/StableBeluga-7B](https://huggingface.co/stabilityai/StableBeluga-7B), [migtissera/SynthIA-7B-v1.3](https://huggingface.co/migtissera/SynthIA-7B-v1.3), [PygmalionAI/pygmalion-2-7b](https://huggingface.co/PygmalionAI/pygmalion-2-7b), [Local-Novel-LLM-project/Ninja-v1-NSFW-128k](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-NSFW-128k), [KoboldAI/OPT-13B-Nerybus-Mix](https://huggingface.co/KoboldAI/OPT-13B-Nerybus-Mix), [microsoft/Orca-2-13b](https://huggingface.co/microsoft/Orca-2-13b), [stabilityai/StableBeluga-13B](https://huggingface.co/stabilityai/StableBeluga-13B), [facebook/opt-13b](https://huggingface.co/facebook/opt-13b)) which, upon preliminary testing, are more easily to generate risk responses. The specific sources of the risk-related questions we adopted are:

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

# Data Format

```json
{
    "prompt_text": "risky quesion",
    "source": "the source of the risky quesion",
    "references": [
    {
        "text": "the response generated by response_model for prompt_text",
        "response_model": "the name of the model that generates text",
        "label": "Whether text is risky, 1 means yes and 0 means no "
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

<font style="color: gray">The references field is mainly used for automated evaluation methods based on similarity. If other evaluation schemes are used, it can be omitted.</font>
<br>

# Sample Data

The complete benchmark dataset contains a large number of risk-related questions and responses, which have not yet undergone comprehensive auditing. To avoid unnecessary internal and external compliance risks, we are open-sourcing a small portion of low-risk data to help users quickly get started with the full-process automated evaluation capabilities of YiJian-Community. The Chinese and English sample evaluation data are stored in [samples_50_zh.jsonl](../yijian_community/data/samples_50_zh.jsonl) and [samples_50_en.jsonl](../yijian_community/data/samples_50_en.jsonl), respectively.

<font style="color: gray">The open sourced large models we used to obtain risk responses have insufficient basic capabilities, and sometimes may generate responses that are incoherent or repetitive.</font>
<br>

# Other evaluation dataset

A large amount of safety evaluation data (such as [SafetyPrompts.com](https://safetyprompts.com/)) has been open sourced, and you can try different data to initiate evaluations. If you find problems with the YiJian-Community during the evaluation process, we welcome and appreciate your feedback!

