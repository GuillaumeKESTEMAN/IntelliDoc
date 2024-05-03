import warnings
from datasets import load_dataset
from sentence_transformers import SentenceTransformer

warnings.simplefilter(action="ignore", category=FutureWarning)

# download sbert model during docker build
# https://www.sbert.net/docs/pretrained_models.html
# https://huggingface.co/sentence-transformers/all-mpnet-base-v2
SentenceTransformer("all-mpnet-base-v2")

# https://pypi.org/project/bert-extractive-summarizer/#use-sbert
SentenceTransformer("paraphrase-MiniLM-L6-v2")

# import wikipedia dataset
# source : https://huggingface.co/datasets/wikipedia
load_dataset("wikipedia", "20220301.fr", trust_remote_code=True)
