def textual_search(elastic):
    print("RECHERCHE TEXTUELLE")

    research = input("Que recherchez-vous : ")

    query = {
        "bool": {
            "should": [
                {"fuzzy": {"title": {"value": research, "fuzziness": "AUTO"}}},
                {"fuzzy": {"paragraph": {"value": research, "fuzziness": "AUTO"}}},
            ]
        }
    }

    res = elastic.search(
        index="documents", query=query, size=1, source=["title", "paragraph", "link"]
    )

    print(res["hits"]["hits"])

    input()


def semantic_search(elastic, model):
    print("RECHERCHE SÉMANTIQUE")

    research = input("Que recherchez-vous : ")

    vector_of_research = model.encode(research)

    query = {
        "field": "text_vector",
        "query_vector": vector_of_research,
        "k": 1,
    }

    res = elastic.search(
        index="documents", knn=query, source=["title", "paragraph", "link"]
    )

    print(res["hits"]["hits"])

    input()
