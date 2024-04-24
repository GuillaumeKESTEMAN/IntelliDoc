def add_data(elastic, model):
    # get textual data
    title = input("Entrez le titre du document : ")
    paragraph = input("Entrez le paragraphe : ")
    link = input("Entrez le lien de la source : ")

    # create json and add title_vector and paragraph_vector
    new_data = {
        "title": title,
        "title_vector": model.encode(title),
        "paragraph": paragraph,
        "paragraph_vector": model.encode(paragraph),
        "link": link,
    }

    # index data in ElasticSearch
    try:
        elastic.index(index="documents", document=new_data)
        print()
        print("Donnée ajoutée avec succès")

        print()
        input("appuyez sur Entrée pour continuer...")
    except Exception:
        print("Une erreur est survenue")
