# la fonction inverser_chaine utilise la syntaxe de découpage de liste ([::-1]) 
# pour inverser la chaîne de caractères et la renvoyer.
# Nous pouvons appeler cette fonction avec différentes chaînes de caractères pour voir les résultats inversés.


def inverser_chaine(chaine):
    return chaine[::-1]

# Appeler la fonction 
chaine_inversee = inverser_chaine("nikana")

# Nous affichons le résultat
print(chaine_inversee)
