# Nous rédigeons une fonction qui permet de vérifier si 3 longueur ont la possibilité de former un triangle par l'inégalité triangulaire
def est_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
# Cette fonction permet de vérifier si les longeuru ne peuvent pas former un triangle alors on retourne le message suivant.
def form_triangulaire(a, b, c):
    if not est_triangle(a, b, c):
        return "Les longueurs ne peuvent pas former un triangle."
    # Le code vérifie le type spécifique de triangle en fonction des longueurs données. Il utilise une série de conditions if, elif, et else :
    # Si les trois côtés sont égaux (a == b == c), le triangle est équilatéral.
    # Sinon, s'il y a au moins deux côtés égaux (a == b ou b == c ou c == a), il vérifie ensuite si le triangle est à la fois isocèle et rectangle en utilisant la condition if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2. Si c'est le cas, il renvoie "Le triangle est rectangle et isocèle." Sinon, il renvoie "Le triangle est isocèle mais pas rectangle."
    # Ensuite, si la condition ci-dessus n'est pas satisfaite, il vérifie à nouveau la condition if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 pour déterminer si le triangle est rectangle. Si c'est le cas, il renvoie "Le triangle est rectangle."
    # Si aucune des conditions ci-dessus n'est satisfaite, cela signifie que le triangle est quelconque, et la fonction renvoie "Le triangle est quelconque."
    if a == b == c:
        return "Le triangle est équilatéral."
    elif a == b or b == c or c == a:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return "Le triangle est rectangle et isocèle."
        else:
            return "Le triangle est isocèle mais pas rectangle."
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "Le triangle est rectangle."
    else:
        return "Le triangle est quelconque."
# A partir de cette étape nous récamons à l'utilisateur d'entrer une longueur de chaque cotés.
a = float(input("Entrez une valeur à la longueur A : "))
b = float(input("Entrez une valeur à la longueur B : "))
c = float(input("Entrez une valeur à la longueur C : "))

# Puis nous attribuons notre valeur résultante à notre forme triangulaire intégrant chaques cotés respectifs. 
valeur_resultante = form_triangulaire(a, b, c)

# Finalement, nous affichons de ce qui en résulte de la valeur résultante.
print(valeur_resultante)
