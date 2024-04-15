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

test_taxonomy()
test_dataset()
