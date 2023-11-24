# Une liste L est créée avec au moins 5 entiers.
# La deuxième valeur de la liste (L[1]) est affichée.
# Une fonction remplacer_element est définie pour remplacer un élément à un indice donné par la somme de ses voisins.
# La fonction est appelée pour remplacer L[3] par la somme des cases voisines L[2] et L[4].
# La liste est affichée après la modification.
# La dernière valeur de la liste (L[-1]) est affichée.

def remplacement(liste, valeur):
    # Il faut que nous vérifions que la valeur est valide
    if valeur < 0 or valeur >= len(liste):
        print("valeur invalide.")
        return

    # Remplacer l'élément à l'indice par la somme des éléments voisins
    liste[valeur] = liste[valeur - 1] + liste[valeur + 1]

# Nous créons une liste d'au moins 5 entiers.
L = [1, 2, 3, 4, 5]

# Afficher la deuxième valeur de la liste
print("Affichage de la 2ème Valeur :", L)
print("Deuxième valeur de la liste :", L[1])

# Nous appellons la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
remplacement(L, 3)

# Afficher la dernière valeur de la liste
print("Affichage de la liste mise à jour :", L)
print("Dernière valeur de la liste :", L[-1])




