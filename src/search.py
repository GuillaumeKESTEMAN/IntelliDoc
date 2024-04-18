import os
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

try:
    es = Elasticsearch(
        "http://10.0.0.1:9200",
        basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
    )
except Exception as e:
    print(e)

# utilisation d'un modèle de sbert
# https://www.sbert.net/docs/pretrained_models.html
# https://huggingface.co/sentence-transformers/all-mpnet-base-v2
model = SentenceTransformer("all-mpnet-base-v2")


def search():
    research = input("Que recherchez-vous : ")

    vector_of_research = model.encode(research)

    query = {
        "field": "text_vector",
        "query_vector": vector_of_research,
        "k": 1,
    }

    res = es.search(index="documents", knn=query, source=["title", "paragraph", "link"])

    print(res["hits"]["hits"])

    input()
