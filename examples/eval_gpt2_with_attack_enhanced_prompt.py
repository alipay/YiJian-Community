from sentence_transformers import SentenceTransformer

from yijian_community.data import load_data, save_data
from yijian_community.evaluator import NaiveTextSimilarityTagger, tagger
from yijian_community.model import VLLMTxt2TxtInfer
from yijian_community.technique import TextPromptAttack
from yijian_community.utils import console

console.log("loading evalation data ...")
test_set = load_data(
    "../yijian_community/data/yijian_community/data/samples_50_zh.jsonl"
)
console.log("evaluation data loaded!")

infer_model = VLLMTxt2TxtInfer("Qwen/Qwen2-7B-Instruct")
prompt_attack = TextPromptAttack(infer_model, lang="en")
aug_test_set = prompt_attack.attack_dataset(test_set, batch_size=20)

console.log("testing target model ...")
target_model = VLLMTxt2TxtInfer("openai-community/gpt2")
# target_model can also be used as infer_model, if it has decent reasoning abilities
response_set = target_model.infer_dataset(aug_test_set, batch_size=128)
console.log("target model tested!")

console.log("tagging ...")
embedding_model = SentenceTransformer("BAAI/bge-large-zh-v1.5")
tagger = NaiveTextSimilarityTagger(embedding_model=embedding_model)
tagged_result_set = tagger(response_set)
save_data("./gpt2_attacked_enhanced_res.jsonl", tagged_result_set)
console.log("evaluation done!")
