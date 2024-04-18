def add_data(elastic, model):
    # get textual data
    title = input("Entrez le titre du document : ")
    paragraph = input("Entrez le paragraphe : ")
    link = input("Entrez le lien de la source : ")

    # create json and add text_vector from concatenation of the title and the paragraph
    new_data = {
        "title": title,
        "paragraph": paragraph,
        "text_vector": model.encode(title + "\n" + paragraph),
        "link": link,
    }

    # index data in ElasticSearch
    try:
        elastic.index(index="documents", document=new_data)
        print("\n")
        print("Donnée ajoutée avec succès")

        print("\n")
        input("appuyez sur Entrée pour continuer...")
    except Exception:
        print("Une erreur est survenue")
