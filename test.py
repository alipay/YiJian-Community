from dataset import Txt2TxtRecord

record = Txt2TxtRecord(prompt_text="this is something")

print(record)

record.response_text = "this is response"

print(record)