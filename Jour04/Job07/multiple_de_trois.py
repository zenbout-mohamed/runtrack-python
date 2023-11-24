

def element_de_trois(liste):
    # Initialiser un compteur pour les multiples de 3
    nombre_de_multiples_de_trois = 0
    
    # Pour parcourir la liste et incrémente un compteur chaque fois qu'un élément est un multiple de 3.
    for nombre in liste:
        # Vérifier si le nombre est un multiple de 3
        if nombre % 3 == 0:
            nombre_de_multiples_de_trois += 1
    
    return nombre_de_multiples_de_trois

## Nous définissons notre tableau pour la table de 3 par la variable ma_liste.
ma_liste = [1, 3, 6, 9, 12, 15, 7, 18, 21]
nombre_de_multiples = element_de_trois(ma_liste)

# Afficher le résultat
print("Le nombre de multiples de 3 dans la liste est :", nombre_de_multiples)

