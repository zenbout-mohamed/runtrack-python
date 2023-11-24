# Nous définissons la liste paires parmis le tableau suivant déja réalisé.
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Nous initialisons la somme à 0
nombre_paires = 0

# Nous ouvrons une boucle for puis une condition intégré Parcourir la liste et additionner les valeurs paires
for indice in L:
    if indice % 2 == 0:
        nombre_paires += indice

# Afficher la nombre des valeurs paires
print("Le nombre paire par les valeurs indiquées est :", nombre_paires)
