import warnings
from sentence_transformers import SentenceTransformer

warnings.simplefilter(action="ignore", category=FutureWarning)

# download sbert model during docker build
# https://www.sbert.net/docs/pretrained_models.html
# https://huggingface.co/sentence-transformers/all-mpnet-base-v2
SentenceTransformer("all-mpnet-base-v2")
SentenceTransformer("paraphrase-MiniLM-L6-v2")
