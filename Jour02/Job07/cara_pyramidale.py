# La fonction len est utilisées pour obtenir la longueur d'une séquence comme une chaine de caractère.
# min est une fonction intégré qui renvoie le plus petit élément en un ou plusieurs arguments.
alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

nombre_cara = 0
ligne = 1

while nombre_cara < len(alphabet):
    affichage_cara = min(ligne, len(alphabet) - nombre_cara)
    print(alphabet[nombre_cara:nombre_cara + affichage_cara])
    nombre_cara += affichage_cara
    ligne += 1