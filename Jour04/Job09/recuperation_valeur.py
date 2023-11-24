def liste_alternatif(liste):
    if not liste:
        print("La liste est vide.")
        return None
# La fonction trouver_infos_liste_alternatif utilise la fonction sum pour calculer la somme des éléments de la liste,
# et les fonctions intégrées max et min pour trouver respectivement le maximum et le minimum.
# Cette approche est plus concise et peut rendre le code plus lisible.
    somme = sum(liste)
    maximum = max(liste)
    minimum = min(liste)
# Nous retournons les 3 variables :
    return somme, maximum, minimum

# Nous réalisons notre liste :
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Appeler la fonction pour récupérer les informations.
result = liste_alternatif(L)

# Nous affichons le résultat :
print("La valeur max est :", result[1])
print("La valeur min est :", result[2])
