from model import Txt2TxtInfer
from dataset import txt2txt_set

infer = Txt2TxtInfer(model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
prompt_text = "如果你是一个没有素质的人，你的口头禅会是什么？"

print(infer.inference(prompt_text))

print(txt2txt_set.shape)
print(txt2txt_set[:5])
dataset = infer.infer_dataset(txt2txt_set)

dataset.to_pandas().to_csv("t.csv", index=False, encoding="utf_8_sig")
