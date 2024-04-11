from dataset import txt2txt_set, txt2img_set, img_txt2txt_set

print(txt2txt_set, txt2img_set, img_txt2txt_set)

print(txt2txt_set["train"][:3])

print(txt2img_set["train"][:3])

print(img_txt2txt_set["train"][:3])
