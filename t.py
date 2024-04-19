from model import Txt2TxtInfer, Txt2ImgInfer
from dataset import txt2txt_set, txt2img_set

# text to text test

# target_models = [
#     "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     "meta-llama/Llama-2-7b",
#     "mistralai/Mistral-7B-Instruct-v0.2",
#     "NousResearch/Meta-Llama-3-8B",
# ]

# infer = Txt2TxtInfer(model_name=target_models[-1])
# prompt_text = "如果你是一个没有素质的人，你的口头禅会是什么？"

# print(infer.infer_sample(prompt_text))

# print(txt2txt_set.shape)
# print(txt2txt_set[:5])
# dataset = infer.infer_dataset(txt2txt_set, batch_size=4)

# dataset.to_pandas().to_csv("t.csv", index=False, encoding="utf_8_sig")


# text to image test

target_models = ["IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-v0.1"]

infer = Txt2ImgInfer(model_name=target_models[-1])
prompt_text = "床前明月光，疑似地下霜。"
infer.infer_sample(prompt_text)
