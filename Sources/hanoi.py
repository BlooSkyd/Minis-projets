nbDisques = 4
liste_piles = [[i for i in range(nbDisques,0,-1)], [], []]

def afficher_piles():
    for i in range(len(liste_piles)):
        print(liste_piles[i])

# FIFO : First In, First Out
# Image : pile d'assiettes
    
# LIFO : Last In, First Out
# Image : file d'attente
    
def deplacer(source, destination):
    if len(liste_piles[source]) == 0:
        print("Mouvement impossible") 
        return False
    elif len(liste_piles[destination]) == 0 or liste_piles[source][-1] < liste_piles[destination][-1]:
        liste_piles[destination].append(liste_piles[source].pop())
        afficher_piles()
        return True
    else: 
        print("Mouvement impossible") 
        return False

def jouer_coup():
    valide = False
    while not valide:
        tourA = input("Choisissez la tour d'origine (1, 2 ou 3) : ")
        while(tourA not in ["1","2", "3"]):
            print("Saisie incorrecte, recommencez.")
            tourA = input("Choisissez la tour d'origine (1, 2 ou 3) : ")
        tourB = input("Choisissez la tour de destination (1, 2 ou 3) : ")
        while(tourB not in ["1","2", "3"]):
            print("Saisie incorrecte, recommencez.")
            tourB = input("Choisissez la tour de destination (1, 2 ou 3) : ")
        if tourA != tourB:
            valide = deplacer(int(tourA)-1, int(tourB)-1)
        else: valide = False

def jouer():
    objectif_piles = [[], [], [i for i in range(nbDisques,0,-1)]]
    nb_coup = 0
    afficher_piles()
    while liste_piles != objectif_piles:
        jouer_coup()
        nb_coup += 1
    print(f"Vous avez terminez en {nb_coup} coups !")

jouer()