import json

from import_bulk import import_bulk


def import_from_json(elastic, model):
    try:
        # get json data
        with open("import_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if len(data) == 0:
            print("Aucune données trouvée")
        else:
            # import data into ElasticSearch
            if import_bulk(elastic, model, data):
                print()
                print("Dataset Wikipédia importé avec succès")

    except Exception:
        print("Une erreur est survenue")

    print()
    input("appuyez sur Entrée pour revenir au menu principal...")
