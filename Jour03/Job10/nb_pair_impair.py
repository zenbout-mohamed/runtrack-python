# Dans ce programme, la fonction verifier_pair_impair prend un paramètre nombre et vérifie s'il est un nombre entier positif.
# Si c'est le cas, elle détermine ensuite si le nombre est pair ou impair et retourne le résultat approprié.
# Si le nombre n'est pas un entier positif, un message d'erreur est renvoyé.

def pair_et_impair(nombre):
    if type(nombre) == int and nombre >= 0:
        if nombre % 2 == 0:
            return "Le nombre est pair."
        else:
            return "Le nombre est impair."
    else:
        return "Veuillez entrer un nombre entier positif."

# Appeler la fonction correspondante aux paramètres.
resultat_n_1 = pair_et_impair(6)
resultat_n_2 = pair_et_impair(9)
resultat_n_3 = pair_et_impair(0)
resultat_n_4 = pair_et_impair(-3)
resultat_n_5 = pair_et_impair(11.5)

# Nous Affichons les résultats correspondants.
print(resultat_n_1)
print(resultat_n_2)
print(resultat_n_3)
print(resultat_n_4)
print(resultat_n_5)
