def add_data(elastic, model):
    title = input("Entrez le titre du document : ")
    paragraph = input("Entrez le paragraphe : ")
    link = input("Entrez le lien de la source : ")

    new_data = {
        "title": title,
        "paragraph": paragraph,
        "text_vector": model.encode(title + "\n" + paragraph),
        "link": link,
    }

    try:
        elastic.index(index="documents", document=new_data)
        print("Donnée ajoutée avec succès")
        input()
    except Exception as e:
        print(e)
