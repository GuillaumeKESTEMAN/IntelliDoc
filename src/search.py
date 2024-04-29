import os

from utils.summarize import summarize


def select_result(results, is_summarized):
    selected_result = -1

    print("0: Revenir au menu principal")
    print()

    for index, result in enumerate(results):
        print(f"{index + 1} :", result["_source"]["title"])

        if is_summarized:
            four_first_sentences = " ".join(
                [var for var in result["_source"]["text"].split("\n") if var][0:4]
            )
            print(summarize(four_first_sentences))

        print()

    while True:
        print()
        try:
            selected_result = int(input("Quel résultat choisissez-vous : "))

            if selected_result >= 0 and selected_result <= len(results):
                break
            else:
                raise ValueError
        except ValueError:
            print("\033[A                                                 \033[A")
            print("\033[A                                                 \033[A")

    if selected_result == 0:
        return 0

    return results[selected_result - 1]["_source"]


# select result and print it
def print_result(results, is_summarized=False):
    print()

    if len(results) == 0:
        print("Aucune donnée trouvé")
    else:
        research_result = select_result(results, is_summarized)

        if research_result == 0:
            return

        os.system("cls" if os.name == "nt" else "clear")
        print("\033[1m" + research_result["title"] + "\033[0m")
        print()
        print(research_result["text"])
        print()
        print()
        print("\nSource : " + research_result["link"])

    print()
    input("appuyez sur Entrée pour revenir au menu principal...")


def textual_search(elastic):
    print("RECHERCHE TEXTUELLE")

    # get user research
    research = input("Que recherchez-vous : ")

    # create ElasticSearch search query
    query = {
        "query": {
            "bool": {
                "should": [
                    {
                        "fuzzy": {
                            "title": {
                                "value": research,
                                "fuzziness": "AUTO",
                                "boost": 2,
                            }
                        }
                    },
                    {
                        "fuzzy": {
                            "text": {
                                "value": research,
                                "fuzziness": "AUTO",
                                "boost": 1,
                            }
                        }
                    },
                ],
            },
        },
        "size": 10,
        "min_score": 1.3,
    }

    # make ElasticSearch search query
    try:
        res = elastic.search(
            index="documents",
            body=query,
            source=["title", "text", "link"],
        )
    except Exception:
        print("Une erreur est survenue")

    print_result(res["hits"]["hits"])


def semantic_search(elastic, model):
    print("RECHERCHE SÉMANTIQUE")

    # get user research
    research = input("Que recherchez-vous : ")

    # encore research to vector to compare in database
    vector_of_research = model.encode(research)

    # create ElasticSearch search query
    query = {
        "query": {
            "bool": {
                "should": [
                    {
                        "knn": {
                            "field": "title_vector",
                            "query_vector": vector_of_research,
                            "boost": 2,
                        }
                    },
                    {
                        "knn": {
                            "field": "text_vector",
                            "query_vector": vector_of_research,
                            "boost": 1,
                        }
                    },
                ],
            },
        },
        "size": 10,
        "min_score": 1.3,
    }

    # make ElasticSearch search query
    try:
        res = elastic.search(
            index="documents", body=query, source=["title", "text", "link"]
        )
    except Exception:
        print("Une erreur est survenue")

    print_result(res["hits"]["hits"], True)
