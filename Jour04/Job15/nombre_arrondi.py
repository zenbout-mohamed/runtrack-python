def arrondir(mod):
    n = len(mod)

    # Nous parcourons tous les éléments de la liste
    for i in range(n):
        # Derniers i éléments sont déjà triés, donc nullement besoin de el considérer.
        for j in range(0, n - i - 1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if mod[j] > mod[j + 1]:
                mod[j], mod[j + 1] = mod[j + 1], mod[j]

# Liste originale
liste_originale = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres dans la liste
for i in range(len(liste_originale)):
     # Arrondir en convertissant en entier
    liste_originale[i] = int(liste_originale[i] + 0.5) 
    

# Tri 
arrondir(liste_originale)

# Affichage du résultat
print("Liste arrondie et triée avec succès :", liste_originale)

# Après modification, les nombres ont été arrondis avec succès.
