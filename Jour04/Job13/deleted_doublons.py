# Cette fonction prend une liste en paramètre (liste) et crée une nouvelle liste (sans_doublons)
# qui ne contient pas d'éléments en double.
# sans_doublons : Liste vide qui sera utilisée pour stocker les éléments uniques.
# La boucle for parcourt chaque élément de la liste d'origine (liste).
# L'instruction if element not in sans_doublons: vérifie si l'élément n'est pas déjà présent dans la liste sans_doublons.
# Si l'élément n'est pas présent, il est ajouté à la liste sans_doublons à l'aide de la méthode append().
# La liste sans_doublons est ensuite renvoyée.
def deleted_doublons(liste):
    sans_doublons = []

    for element in liste:
        if element not in sans_doublons:
            sans_doublons.append(element)

    return sans_doublons

# Liste réalisé :
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = deleted_doublons(ma_liste)

# Afficher le résultat
print("Résultat sans doublons :", liste_sans_doublons)
