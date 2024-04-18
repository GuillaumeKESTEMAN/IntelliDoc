import os
import json
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from search import semantic_search, textual_search
from add_data import add_data

load_dotenv()

# import documents index mapping from "index_mapping.json"
with open("./index_mapping.json") as file:
    indexMapping = json.load(file)

# create ElasticSearch connection
try:
    elastic = Elasticsearch(
        "http://10.0.0.1:9200",
        basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
    )
except Exception as e:
    print(e)

# create ElasticSearch documents index if not already exists
if not elastic.indices.exists(index="documents"):
    elastic.indices.create(index="documents", mappings=indexMapping)

# using sbert model
# https://www.sbert.net/docs/pretrained_models.html
# https://huggingface.co/sentence-transformers/all-mpnet-base-v2
model = SentenceTransformer("all-mpnet-base-v2")

isAppOpen = True

# console interface
while isAppOpen:
    os.system("cls" if os.name == "nt" else "clear")
    print("0 : quitter")
    print("1 : ajouter une donnée")
    print("2 : faire une recherche textuelle")
    print("3 : faire une recherche sémantique")
    mainQuestion = input("Que voulez vous faire : ")

    os.system("cls" if os.name == "nt" else "clear")

    if mainQuestion == "0":
        isAppOpen = False
    elif mainQuestion == "1":
        add_data(elastic, model)
    elif mainQuestion == "2":
        textual_search(elastic)
    elif mainQuestion == "3":
        semantic_search(elastic, model)
