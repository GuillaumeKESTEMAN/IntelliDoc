# print first result
def print_result(results):
    print("\n")

    if len(results) == 0:
        print("Aucune donnée trouvé")
    else:
        research_result = results[0]["_source"]
        print("\033[1m" + research_result["title"] + "\033[0m")
        print("")
        print(research_result["paragraph"])
        print("\nSource : " + research_result["link"])

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
                {
                    "fuzzy": {
                        "title": {"value": research, "fuzziness": "AUTO", "boost": 2}
                    }
                },
                {
                    "fuzzy": {
                        "paragraph": {
                            "value": research,
                            "fuzziness": "AUTO",
                            "boost": 1,
                        }
                    }
                },
            ],
        },
        "size": 10,
        "min_score": 1.3,
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
