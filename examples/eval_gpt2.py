from sentence_transformers import SentenceTransformer

from yijian.data import load_data, save_data
from yijian.evaluator import NaiveTextSimilarityTagger, tagger
from yijian.model import VLLMTxt2TxtInfer
from yijian.utils import console

console.log("loading evalation data ...")
eval_set = load_data("./DoNotAnswer.jsonl")
console.log("evaluation data loaded!")

console.log("testing target model ...")
target_model = VLLMTxt2TxtInfer("openai-community/gpt2")
response_set = target_model.infer_dataset(eval_set, batch_size=128)
console.log("target model tested!")

console.log("tagging ...")
embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
tagger = NaiveTextSimilarityTagger(embedding_model=embedding_model)
result_set = tagger(response_set)
save_data("./gpt2_res.jsonl", result_set)
console.log("evaluation done!")
