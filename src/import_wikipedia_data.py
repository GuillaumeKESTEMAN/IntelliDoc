import os
from datasets import load_dataset
from import_bulk import import_bulk


def import_wikipedia_data(elastic, model):
    # import wikipedia dataset
    # source : https://huggingface.co/datasets/wikipedia
    datasets_list = load_dataset("wikipedia", "20220301.fr", trust_remote_code=True)

    os.system("cls" if os.name == "nt" else "clear")

    dataset_size = len(datasets_list["train"])
    size = input(
        f"Combien d'éléments voulez-vous importer (nombre max d'élément: {dataset_size}): "
    )

    try:
        size = int(size)
    except Exception:
        size = dataset_size

    data_list = []

    for index in range(0, size):
        # format data for import_bulk function
        data_list.append(
            {
                "title": datasets_list["train"][index]["title"],
                "text": datasets_list["train"][index]["text"],
                "link": datasets_list["train"][index]["url"],
            }
        )

    if import_bulk(elastic, model, data_list):
        print()
        print("Données JSON importées avec succès")

    print()
    input("appuyez sur Entrée pour revenir au menu principal...")
