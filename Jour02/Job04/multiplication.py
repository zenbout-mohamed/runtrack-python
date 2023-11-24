# Pour ce faire nous demandons à l'utlisateur de saisir un nombre entier grace à l'attribut (int) puis de le saisir en utlisnat la fonction (input)
# 
while True:
    try:
        nombre = int(input("Entrez un nombre entier à partir de 0  : "))
        # Une fois que l'utilistaeur entrera un nombre compris à partir de 0 alors la condtition suivante s'appliquera.
        # Légende :l'instruction (break)permet de sortir d'une boucle
        # L'instruction (try--except) est l'instruction qui permet d'intercepter les exceptions que peuvent générer votre application et d'exécuter d'autres instructions en conséquence.
        # En pratique, le programme exécute les instructions se trouvant dans la clause try. except.
        # ValueError : Cette exception survient lorsqu'une valeur est inappropriée pour une certaine opération, par exemple, l'obtention du logarithme d'un nombre négatif.
        if nombre > 0:
            break
        else:
            print("Entrez un nombre à partir de 0 .")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

# Affichage des mutliplications de 0 à n
for i in range(1, nombre + 1):
    print(f"\n Présentation, Table de multiplication de {i} :")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
