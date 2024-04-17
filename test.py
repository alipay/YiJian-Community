def test_taxonomy():
    from dataset import risk_taxonomy_zh, risk_taxonomy_en
    print(risk_taxonomy_zh)
    print(risk_taxonomy_en)

def test_dataset():
    from dataset import txt2txt_set, txt2img_set, imgtxt2txt_set
    print(txt2txt_set, txt2img_set, imgtxt2txt_set)
    print(txt2txt_set["train"].shape, txt2txt_set["train"].column_names)
    print(txt2img_set["train"].shape, txt2img_set["train"].column_names)
    print(imgtxt2txt_set["train"].shape, imgtxt2txt_set["train"].column_names)

def test_txt2txt_inference():
    from model import txt2txt_inference, txt2txt_models
    pipe = txt2txt_inference("mistralai/Mistral-7B-Instruct-v0.2")
    pipe("你是一个资深政客，请以政客的口吻表达对当前国际局势的看法。")

test_txt2txt_inference()