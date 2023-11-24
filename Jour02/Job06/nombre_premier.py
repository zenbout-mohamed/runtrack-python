# Dans ce cas de figure, nous utilisons la fonction (def) qui permet de définir une fonction,
# la fonction def_premier est utiliser pour déterminer si un nombre donnée est un nombre premier.
# Une focntion est un bloc de code réutilisable qui effectue une tache spéficique.
# Remarque : le terme (%) signifie modulo ce qui permet de diviser n'importe que nombres entre eux et de donner le résultat en nombre entier et non décimale.
# Autrement dit non un nombre à virgule.
def est_premier(entier):
    if entier < 2:
        return False
        # Dans le contexte de la fonction est_premier que nous avons discutée précédemment, nombre**0.5 est utilisé pour calculer la racine carrée de nombre.
        #  C'est une manière efficace de tester si un nombre est premier, car il n'est pas nécessaire de vérifier les diviseurs au-delà de la racine carrée du nombre pour déterminer s'il est divisible.
    for i in range(2, int(entier**0.5) + 1):
        if entier % i == 0:
            return False
    return True

for entier in range(2, 1001):
    if est_premier(entier):
        print(entier)
