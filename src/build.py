from sentence_transformers import SentenceTransformer

# download sbert model during docker build
# https://www.sbert.net/docs/pretrained_models.html
# https://huggingface.co/sentence-transformers/all-mpnet-base-v2
SentenceTransformer("all-mpnet-base-v2")
