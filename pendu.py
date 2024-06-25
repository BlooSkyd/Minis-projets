#encoding: utf-8

import random
import os

lettres_trouvees = []
nb_erreur = 0
dessin = ""

def evoluer_dessin():
    global dessin, nb_erreur
    match nb_erreur:
        case 0:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |\n"\
                    "   |\n"\
                    "   |\n"\
                    "   |\n"\
                    "============="
        case 1:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |     O\n"\
                    "   |\n"\
                    "   |\n"\
                    "   |\n"\
                    "============="
        case 2:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |     O\n"\
                    "   |     |\n"\
                    "   |\n"\
                    "   |\n"\
                    "============="
        case 3:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |     O\n"\
                    "   |    /|\n"\
                    "   |\n"\
                    "   |\n"\
                    "============="
        case 4:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |     O\n"\
                    "   |    /|\\\n"\
                    "   |\n"\
                    "   |\n"\
                    "============="
        case 5:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |     O\n"\
                    "   |    /|\\\n"\
                    "   |    /\n"\
                    "   |\n"\
                    "============="
        case _:
            dessin = "[]=======v=\n"\
                    "   |/    |\n"\
                    "   |     O\n"\
                    "   |    /|\\\n"\
                    "   |    / \\\n"\
                    "   |\n"\
                    "============="
            pass

def ajouter_lettre(lettre: str):
    if lettre not in lettres_trouvees:
        lettres_trouvees.append(lettre)

def devoiler(mot: str, avancee: str, lettre: str):
    global nb_erreur
    
    ajouter_lettre(lettre)

    if mot.count(lettre) == 0 :
        print("Lettre absente")
        nb_erreur += 1
        return avancee
    
    
    resultat = ""
    for index in range(len(mot)):
        if avancee[index] != "-":
            resultat += mot[index]
        elif mot[index] == lettre:
            resultat += lettre
        else:
            resultat += "-"
    
    print(resultat)
    print(lettres_trouvees)
    return resultat

def initialiser_mot(mot: str):
    resultat = ""
    for index in range(len(mot)):
        resultat += "-"
    return resultat

def afficher(progression: str):
    global dessin, lettres_trouvees
    print()
    print(dessin)
    print(lettres_trouvees)
    print(progression)


def jouer():
    global nb_erreur

    liste_mots = ["bateaux", "navires", "catamaran","toboguant"]

    mot_selectionne = random.choice(liste_mots)
    progression = initialiser_mot(mot_selectionne)
    progression = devoiler(mot_selectionne, progression, mot_selectionne[0])

    
    while True:
        if nb_erreur > 5 :
            print("C'est perdu !")
            print("Le mot à trouver était : "+mot_selectionne)
            evoluer_dessin()
            afficher(progression)
            break
        
        if progression == mot_selectionne:
            print("C'est gagné !")
            break
        
        evoluer_dessin()
        afficher(progression)
        lettre = input("=> ")
        progression = devoiler(mot_selectionne, progression, lettre)
        


jouer()