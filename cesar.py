#encoding: utf-8

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def convertir_car(el: str, d: int):
    if el == ' ' : return ' '
    index = alphabet.index(el)
    return alphabet[(index+d)%26]

def convertir_chaine(chaine: str, decalage: int):
    resultat = ""
    for caractere in range(len(chaine)):
        resultat += convertir_car(chaine[caractere], decalage)
    print(resultat)

def convertir_auto(chaine: str):
    caractere_max = max(set(chaine), key = chaine.count)
    # On suppose que le caractère le plus présent est un e
    decalage_calcule = alphabet.index('e') - alphabet.index(caractere_max)
    convertir_chaine(chaine, decalage_calcule)


convertir_chaine("avion qui volle",4)
convertir_chaine("ezmsr", -4)
convertir_chaine("le chien est beau",-5)
convertir_auto("gz xcdzi zno wzvp")
