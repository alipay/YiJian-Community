from dataset import txt2txt_set, txt2img_set, img2txt_set

print(txt2txt_set, txt2img_set, img2txt_set)

print(txt2txt_set["train"].shape, txt2txt_set["train"].column_names)

print(txt2img_set["train"].shape, txt2img_set["train"].column_names)

print(img2txt_set["train"].shape, img2txt_set["train"].column_names)


# def get_response(data):
#     data["response_text"] = "这不好吧"
#     return data


# txt2txt_set["train"] = txt2txt_set["train"].map(get_response)
# print(txt2txt_set["train"][1])
# print(txt2txt_set["train"][2])