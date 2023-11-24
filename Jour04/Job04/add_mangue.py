def add_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    # Ajouter "Mangue" à l'index 2
    # La fonction add_mangue utilise la méthode insert pour ajouter la chaîne de caractères "Mangue" à l'index 2 de la liste "fruits".
    # Ensuite, la nouvelle liste de fruits est retournée.
    fruits.insert(2, "Mangue")
    return fruits

# Appeler la fonction pour ajouter "Mangue" à la liste
nouvelle_liste_de_fruits = add_mangue()

# Affichons le résultat
print("La nouvelle liste de fruits est :", nouvelle_liste_de_fruits)

# La mangue à été rajouté à l'index numéro 2 de la liste.
