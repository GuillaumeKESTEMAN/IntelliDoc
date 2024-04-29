import os
import json
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from import_from_json import import_from_json
from import_wikipedia_data import import_wikipedia_data
from reset_index import reset_index
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
    print("2 : importer un dataset Wikipédia")
    print("3 : importer depuis le fichier import_data.json")
    print("4 : réinitialiser les données")
    print("5 : faire une recherche textuelle")
    print("6 : faire une recherche sémantique")
    print()
    mainQuestion = input("Que voulez vous faire : ")

    os.system("cls" if os.name == "nt" else "clear")

    if mainQuestion == "0":
        isAppOpen = False
    elif mainQuestion == "1":
        add_data(elastic, model)
    elif mainQuestion == "2":
        import_wikipedia_data(elastic, model)
    elif mainQuestion == "3":
        import_from_json(elastic, model)
    elif mainQuestion == "4":
        reset_index(elastic, "documents")
    elif mainQuestion == "5":
        textual_search(elastic)
    elif mainQuestion == "6":
        semantic_search(elastic, model)
