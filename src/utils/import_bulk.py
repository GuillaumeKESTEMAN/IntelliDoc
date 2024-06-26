import datetime
import os


def import_bulk(elastic, model, data):
    bulk_data = []
    data_size = len(data)

    os.system("cls" if os.name == "nt" else "clear")
    print("Formatage des données...\n")

    start_time = datetime.datetime.now()

    for index, data_entry in enumerate(data):
        # time estimation
        execution_time = (datetime.datetime.now() - start_time).total_seconds()
        rest_calc = data_size - index + 1
        time_rest = datetime.timedelta(
            seconds=(execution_time / (index + 1)) * rest_calc
        )
        minutes, seconds = divmod(int(time_rest.total_seconds()), 60)

        print("Importation de : " + data_entry["title"])
        print("")
        print(f"Element : {index + 1}/{data_size}")
        print(f"Temps restant estimé : {minutes:02}:{seconds:02}")

        # add each document to the good object format
        bulk_data.append(
            {
                "index": {
                    "_index": "documents",
                }
            }
        )

        bulk_data.append(
            {
                "title": data_entry["title"],
                "title_vector": model.encode(data_entry["title"]),
                "text": data_entry["text"],
                "text_vector": model.encode(data_entry["text"]),
                "link": data_entry["link"],
            }
        )

        print("\033[A                              \033[A")
        print("\033[A                              \033[A")
        print("\033[A                              \033[A")

    os.system("cls" if os.name == "nt" else "clear")

    # set pack size
    pack_size = 1000

    # Diviser le grand tableau en lots plus petits
    bulk_packs = [
        bulk_data[i : i + pack_size] for i in range(0, len(bulk_data), pack_size)
    ]

    print("Importation des données...")

    # make one bulk request for every group of X data
    for bulk_pack in bulk_packs:
        # index Wikipedia dataset in ElasticSearch
        try:
            elastic.bulk(index="documents", body=bulk_pack, refresh=True)
        except Exception:
            print("Une erreur est survenue")
            return False

    return True
