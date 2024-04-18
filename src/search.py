# print first result
def print_result(results):
    print("\n")

    if len(results) == 0:
        print("Aucune donnée trouvé")
    else:
        research_result = results[0]["_source"]
        print("Titre: " + research_result["title"])
        print("Paragraphe: " + research_result["paragraph"])
        print("Lien: " + research_result["link"])

    print("\n")
    input("appuyez sur Entrée pour continuer...")


def textual_search(elastic):
    print("RECHERCHE TEXTUELLE")

    # get user research
    research = input("Que recherchez-vous : ")

    # create ElasticSearch search query
    query = {
        "bool": {
            "should": [
                {"fuzzy": {"title": {"value": research, "fuzziness": "AUTO"}}},
                {"fuzzy": {"paragraph": {"value": research, "fuzziness": "AUTO"}}},
            ]
        }
    }

    # make ElasticSearch search query
    try:
        res = elastic.search(
            index="documents",
            query=query,
            size=1,
            source=["title", "paragraph", "link"],
        )
    except Exception:
        print("Une erreur est survenue")

    # print first result or none
    print_result(res["hits"]["hits"])


def semantic_search(elastic, model):
    print("RECHERCHE SÉMANTIQUE")

    # get user research
    research = input("Que recherchez-vous : ")

    # encore research to vector to compare in database
    vector_of_research = model.encode(research)

    # create ElasticSearch search query
    query = {
        "field": "text_vector",
        "query_vector": vector_of_research,
        "k": 1,
    }

    # make ElasticSearch search query
    try:
        res = elastic.search(
            index="documents", knn=query, source=["title", "paragraph", "link"]
        )
    except Exception:
        print("Une erreur est survenue")

    # print first result or none
    print_result(res["hits"]["hits"])
