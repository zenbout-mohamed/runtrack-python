# Il suffit cependant de réaliser une boucle comprenant une condition intégré à l'intérieur de la boucle en rajoutant la condition suivante.

for i in range(101):
    if i not in [26, 37, 88]:
        print(i)
