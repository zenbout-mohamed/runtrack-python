def tapis_diag(taille):
    for i in range(taille + 1):
        for j in range(taille + 1):
            if i == j:
                print(" ", end=" ")
            else:
                print("", end="#")
        print()

# réclamer à l'utilisateur de saisir un evaluer qui servira à définir la taille du tapis.
tapis_size = int(input("Entrez la taille du tapis : "))

# Appeler la fonction 
tapis_diag(tapis_size)
