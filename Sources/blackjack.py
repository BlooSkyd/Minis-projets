import random
import sys

couleurs = ["Coeur", "Pique", "Carreau", "Trèfle"]
figures = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]

class Carte:
    def __init__(self, couleur: str, figure: str) -> None:
        self.couleur = couleur
        self.figure = figure
        if figure in ["Valet", "Dame", "Roi"]:
            self.poid = 10
        elif figure == "As":
            self.poid = None
        else:
            self.poid = int(figure)
    
    def __str__(self) -> str:
        if self.figure == "Dame" : res = "la " 
        else: res = "le "
        return res + self.figure + " de " + self.couleur

    def getFigure(self):
        return self.figure
    
    def getPoid(self):
        return self.poid
    
    def setPoid(self, p):
        self.poid = p


class MainJoueur:

    def __init__(self, type="Joueur") -> None:
        self.main = []
        self.totalMain = 0
        self.type = type
    
    def demanderPoid() -> int:
        val = input("Vous avez piochez un as, choisissez sa valeur parmis 1 ou 11 : ")
        while(val not in ["1","11"]):
            print("Saisie incorrecte, recommencez.")
            val = input("Vous avez piochez un as, choisissez sa valeur parmis 1 ou 11 : ")
        return int(val)

    def piocher(self, paquet, afficher=True):
        carte = paquet.pop()
        #print(">>> DEBUG: "+str(carte))
        if self.type != "Joueur":
            if afficher: print(f"[Dealer] Le dealer a piocher {carte}.")
            else: print("[Dealer] Le dealer a piocher une carte.")
            if carte.getPoid() == None:
                carte.setPoid(10)
            self.totalMain += carte.getPoid()
        else:
            if carte.getPoid() == None:
                carte.setPoid(self.demanderPoid())
            self.main.append(carte)
            self.totalMain += carte.getPoid()
            if afficher: print(f"Vous avez piochez {carte}.")
            print(f"Vous avez {self.totalMain} points")


def demandePioche():
    res = input("Voulez-vous piocher une carte supplémentaire ? (y/n) ")
    while(res not in ["y","n"]):
        print("Saisie incorrecte, recommencez.")
        res = input("Voulez-vous piocher une carte supplémentaire ? (y/n) ")
    return res == "y"


paquet = []
for coul in couleurs:
    for fig in figures:
        paquet.append(Carte(coul, fig))
random.shuffle(paquet)


def jeu(paquet):
    dealer = MainJoueur("Dealer")
    joueur = MainJoueur()
    joueur.piocher(paquet)
    dealer.piocher(paquet)
    joueur.piocher(paquet)
    if joueur.totalMain == 21: print("Blackjack !")
    dealer.piocher(paquet, False)

    continuer = True if joueur.totalMain < 21 else False
    while continuer:
        if demandePioche():
            joueur.piocher(paquet)
            if joueur.totalMain >= 21 : continuer = False
        else:
            continuer = False
    
    if joueur.totalMain > 21:
        print("Vous avez perdu !")
        sys.exit(0)

    while dealer.totalMain < 17:
        dealer.piocher(paquet, False)

    print()
    print("Résultats :")
    print(f"Vous avez {joueur.totalMain} points." + (" Blackjack !" if joueur.totalMain == 21 else ""))
    print(f"Le dealer a {dealer.totalMain} points.")
    
    if dealer.totalMain > 21:
        print("Le [Dealer] a perdu !")
    elif dealer.totalMain == joueur.totalMain:
        print("Egalité !")
    elif dealer.totalMain < joueur.totalMain:
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu.")    

jeu(paquet)