def type_aliment(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucun produit correspondant à cette combinaison de type et saison")
# Ensuite nius appellons la fonction.
type_aliment("fruits", "hiver")
type_aliment("fruits", "ete")
type_aliment("legume", "hiver")
type_aliment("legume", "ete")

