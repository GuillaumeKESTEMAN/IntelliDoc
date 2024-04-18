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

indexMapping = {
    "properties": {
        "title": {"type": "text"},
        "paragraph": {"type": "text"},
        "text_vector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "l2_norm",
        },
        "link": {"type": "text"},
    }
}


def add_data():
    title = input("Entrez le titre du document : ")
    paragraph = input("Entrez le paragraphe : ")
    link = input("Entrez le lien de la source : ")

    new_data = {
        "title": title,
        "paragraph": paragraph,
        "text_vector": model.encode(title + "\n" + paragraph),
        "link": link,
    }

    if not es.indices.exists(index="documents"):
        es.indices.create(index="documents", mappings=indexMapping)

    try:
        es.index(index="documents", document=new_data)
        print("Donnée ajoutée avec succès")
        input()
    except Exception as e:
        print(e)
