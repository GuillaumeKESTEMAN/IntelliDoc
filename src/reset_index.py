import os


def reset_index(elastic, index_name):
    print("Réinitialisation en cours...")

    try:
        elastic.delete_by_query(index=index_name, body={"query": {"match_all": {}}})

        os.system("cls" if os.name == "nt" else "clear")
        print("Réinitialisation effectuées avec succès")
    except Exception:
        print("Une erreur est survenue")

    print()
    input("appuyez sur Entrée pour revenir au menu principal...")
