#encoding: utf-8

import random

liste_mots = ["bateaux", "navires", "catamaran"]

mot_selectionne = liste_mots[random.randint(0,2)]

mot_init = ""
for _ in range(len(mot_selectionne)):
    mot_init += "?"

print("Début de la partie :")
print("Mot à trouver : "+mot_init+" ("+str(len(mot_init))+")")

while mot_init != mot_selectionne:
    saisie = input("=> ")
    
    if saisie == "STOP": # Permet de sortir du programme
        break
    
    elif len(saisie) != len(mot_selectionne):
        print("Longueur incorrecte, réessayez !")
    
    elif saisie == mot_selectionne:
        print("Vous avez trouvé !")
        break

    else:
        affichage = ""
        for i in range(len(saisie)):
            if saisie[i] == mot_selectionne[i]:
                # La i est au bon endroit
                affichage += saisie[i]
                pass
            elif mot_selectionne.count(saisie[i]) > 0:
                # La i est présente mais mal placée
                affichage += "?"
            else:
                # La i n'apparait pas
                affichage += "-"
        print(affichage)

print("Fin du programme.")