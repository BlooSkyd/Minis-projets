# coding: utf-8
import os

plateau = [' ' for _ in range(9)]
joueur = "X"
coup = 0

# Fonction pour afficher le plateau
def afficherPlateau():
    #os.system('cls')
    global plateau
    print("",plateau[0],"|",plateau[1],"|",plateau[2])
    print("-"*11)
    print("",plateau[3],"|",plateau[4],"|",plateau[5])
    print("-"*11)
    print("",plateau[6],"|",plateau[7],"|",plateau[8])


# Fonction pour jouer un coup    
def jouerCoup() -> bool:
    global joueur, coup
    position = int(input("Entrez un numéro de case entre 1 et 9: "))
    position -= 1
    if (position < 0) or ( position > 8):
        print("Coup invalide : saisissez un nombre entre 1 et 9")
        return False

    if plateau[position] != ' ':
        print("Coup invalide : cette case est déjà remplie")
        return False
    
    plateau[position] = joueur
    coup += 1
    return True
   

# Fonction qui s'occupe du déroulement du jeu
def jouer():
    global coup, joueur
    victory = False
    while coup < 9 and not victory:
        jouerCoup()
        victory = victoire()
        if not victory:
            joueur = "O" if joueur == "X" else "X"
        afficherPlateau()
    if victory:
        print(f"Le joueur {joueur} a gagné !")
    else:
        print("Égalité")


# Fonction qui vérifie les conditions de victoires
def victoire() -> bool:
    global plateau, joueur

    for i in range(0,9,3):
        if plateau[i] == joueur and plateau[i+1] == joueur and plateau[i+2] == joueur : return True
    for i in range(0,3):
        if plateau[i] == joueur and plateau[i+3] == joueur and plateau[i+6] == joueur : return True
    if plateau[0] == joueur and plateau[4] == joueur and plateau[8] == joueur : return True
    if plateau[6] == joueur and plateau[4] == joueur and plateau[2] == joueur : return True
    return False


jouer()