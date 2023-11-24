# Ce programme permet de calculer le produit de toutes les valeurs de la liste comprises
# dans l’intervalle [25, 90]

# La 1ère Etape consiste à réaliser notre liste L :
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit à 1
nombre_produit = 1

# Parcourir la liste et multiplier les valeurs dans l'intervalle [25, 90]
for valeur in L:
    if 25 <= valeur <= 90:
        nombre_produit *= valeur

# Afficher le produit des valeurs dans l'intervalle :
print("Le produit des valeurs dans l'intervalle [25, 90] est :", nombre_produit)
