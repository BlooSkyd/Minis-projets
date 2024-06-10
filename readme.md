# Minis projets

Pour l'ensemble des projets, nous pourront utiliser Python ou JavaScript comme langage de programmation.

## 1. Motus

L'idée est de faire un petit programme qui choisi un mot, et nous l'affiche de manière *sensurée*.
L'utilisateur devra donc saisir des mots comme tentatives, et les lettres communes seront affichées.
L'affichage de retour est à déterminer, soit avec des caractères spéciaux (?,#,€, etc) ou bien via des couleurs de manière plus proche du jeu existant.
Nous pourrions avoir une évolution avec un système de vie.

Exemple :
Mot à trouver : `bateaux`
Affichage : `??????`
Saisie : `palmier`
Réponse : `-a---?-` (affichage relatif à la saisie)
Saisie : `tambour`
Réponse : `?a-?-u-` (affichage relatif à la saisie)


## 2. Calculatrice

Le but est de pouvoir saisir des opérations plus ou moins simples et d'obtenir le résultat.
Pour cela, il faudra analyser les données passées en entrées et les décomposer en opération ou expression.

Exemples :
Saisie : `5-2`
Réponse : `3`
Saisie : `3*3+6/2`
Réponse : `12`

Pour cela, je propose de "simplement" décomposer chaque opérations en *expressions* :
- e --> n (valeur)
- e + e --> (expression)
- e - e --> (expression)
- e * e --> (expression)
- e / e --> (expression)
- e % e --> (expression)
- ( e ) --> (expression)

## 3. Discord / Site web hébergé