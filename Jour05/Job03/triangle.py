# Pour ceci égalmeent nous devons établir une fonction nommée triangle en lui accirdant un paramètre.
def triangle(height):
    for i in range(height):
        # Afficher des espaces avant le premier caractère
        print(" " * (height - i - 1), end="")

        # Afficher le caractère '/' représentant le coté gauche du triangle.
        print("/", end="")

        # Afficher des caractères '_' représentant la ligne du triangle.
        print("_" * (2 * i), end="")

        # Afficher le caractère '\' représentant le coté droit du triangle.
        print("\\", end="")

        # Passer à la ligne pour la prochaine rangée
        print()

# Demander à l'utilisateur de saisir la hauteur du triangle
height_triangle = int(input("Entrez la hauteur du triangle : "))

# Appeler la fonction pour afficher le triangle
triangle(height_triangle)
