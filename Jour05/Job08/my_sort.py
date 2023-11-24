def my_sort(ma_liste):
    nombre_de_coups = 0

    while True:
        a_eu_echange = False

        for i in range(len(ma_liste) - 1):
            if ma_liste[i] > ma_liste[i + 1]:
                ma_liste[i], ma_liste[i + 1] = ma_liste[i + 1], ma_liste[i]
                nombre_de_coups += 1
                a_eu_echange = True
    # La condition if not a_eu_echange permet de sortir de la boucle lorsque la liste est triée.
        if not a_eu_echange:
            break

    print(f"Nombre total de coups nécessaires pour trier la liste : {nombre_de_coups}")
    return ma_liste

# Exemple d'utilisation
liste_originale = [22, 34, 11, 25, 12, 64, 90]
# L'utilisation de liste_originale.copy() crée une copie superficielle (shallow copy) de la liste liste_originale.
liste_triee = my_sort(liste_originale.copy())
print("Liste triée :", liste_triee)
