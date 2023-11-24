# la fonction echanger_premiere_et_derniere prend une liste en paramètre,
# puis échange les valeurs de la première et de la dernière case de la liste à l'aide de l'affectation multiple.
# La condition if len(liste) >= 2 vérifie que la liste a au moins deux éléments pour pouvoir effectuer l'échange.

def rangee_inversees(liste):
    if len(liste) >= 2:
        # Échanger les valeurs de la première et de la dernière case.
        liste[0], liste[-1] = liste[-1], liste[0]
    else:
        print("La liste est insuffisante pour procéder à l'échange.")

# Exemple d'utilisation avec une liste quelconque.
tableau = [1, 2, 3, 4, 5]
print("Avant modification :", tableau)

# Appeler la fonction pour échanger les valeurs.
rangee_inversees(tableau)

# Afficher le résultat après l'échange.
print("Après modification :", tableau)
