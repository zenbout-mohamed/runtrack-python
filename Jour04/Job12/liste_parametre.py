def tri_bulles(liste):
    n = len(liste)

    # Parcourir tous les éléments de la liste
    for i in range(n):
        # Derniers i éléments sont déjà triés, donc nous n'avons pas besoin de les considérer
        for j in range(0, n - i - 1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

# Réalisation de la liste
liste_triee = [64, 34, 25, 12, 22, 11, 90]

# Appeler la fonction définie :
tri_bulles(liste_triee)

# Affichage le résultat
print("Liste triée par l'ordre croissant :", liste_triee)
