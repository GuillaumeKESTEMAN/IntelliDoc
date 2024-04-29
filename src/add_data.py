def add_data(elastic, model):
    # get textual data
    title = input("Entrez le titre du document : ")
    text = input("Entrez le texte : ")
    link = input("Entrez le lien de la source : ")

    # create json and add title_vector and text_vector
    new_data = {
        "title": title,
        "title_vector": model.encode(title),
        "text": text,
        "text_vector": model.encode(text),
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
