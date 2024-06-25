import random

nbpile = 6
capacite = 3
nbcouleur = 3


def creer_init_piles(nbpile: int, cap: int, ncol: int):
    liste_piles = [[] for _ in range(nbpile)]
    if nbpile < ncol+1:
        print("Il n'y a pas assez de piles pour ce nombre de couleur")
        exit()

    listes_reduites = []
    for n in range(ncol):
        listes_reduites.append([n for _ in range(cap)])

    for pile in range(ncol):
        for c in range(cap):
            sel = random.choice(listes_reduites)
            liste_piles[pile].append(sel.pop())
            if len(sel) == 0:
                listes_reduites.remove(sel)
    return liste_piles

liste_piles = creer_init_piles(nbpile, capacite, nbcouleur)

def afficher_piles():
    for i in range(len(liste_piles)):
        print(f"{i+1}: {liste_piles[i]}")

def deplacer(source, destination, doMessage: bool = True):
    if len(liste_piles[source]) == 0 or len(liste_piles[destination]) == capacite:
        if doMessage: print("Mouvement impossible") 
        return False
    elif len(liste_piles[destination]) == 0 or liste_piles[source][-1] == liste_piles[destination][-1]:
        liste_piles[destination].append(liste_piles[source].pop())
        return True
    else: 
        if doMessage : print("Mouvement impossible") 
        return False

def jouer_coup():
    valide = False
    while not valide:
        tourA = input("Choisissez la tour d'origine (1, 2...) : ")
        while(tourA not in [str(n) for n in range(1, nbpile+1)]):
            print("Saisie incorrecte, recommencez.")
            tourA = input("Choisissez la tour d'origine (1, 2...) : ")
        tourB = input("Choisissez la tour de destination (1, 2...) : ")
        while(tourB not in [str(n) for n in range(1, nbpile+1)]):
            print("Saisie incorrecte, recommencez.")
            tourB = input("Choisissez la tour de destination (1, 2...) : ")
        if tourA != tourB:
            valide = deplacer(int(tourA)-1, int(tourB)-1)
            while valide:
                valide = deplacer(int(tourA)-1, int(tourB)-1, False)
            afficher_piles()
        else: valide = False

def verif_victoire() -> bool:
    res = True
    for pile in liste_piles:
        if len(pile) == 0:
            print(f"{pile}: vide")
            continue
        if pile.count(pile[0]) == len(pile):
            print(f"{pile}: trié")
            continue
        print(f"{pile}: non-trié")
        res = False
    return res


def jouer():
    nb_coup = 0
    afficher_piles()
    victoire = verif_victoire()
    while victoire != True:
        jouer_coup()
        nb_coup += 1
        victoire = verif_victoire()
    print(f"Vous avez terminez en {nb_coup} coups !")

jouer()