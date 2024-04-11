import os
from search import search
from add_data import add_data

isAppOpen = True

while isAppOpen:
    os.system("cls" if os.name == "nt" else "clear")
    print("1 : ajouter une donnée")
    print("2 : faire une recherche sémantique")
    print("3 : quitter")
    mainQuestion = input("Que voulez vous faire : ")

    os.system("cls" if os.name == "nt" else "clear")

    if mainQuestion == "1":
        add_data()
    elif mainQuestion == "2":
        search()
    elif mainQuestion == "3":
        isAppOpen = False
