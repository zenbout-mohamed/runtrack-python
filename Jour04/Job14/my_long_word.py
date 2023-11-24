














def my_long_word(longueur_min,chaine):
    # mots_long = []: Initialise une liste vide qui sera utilisée pour stocker les mots plus longs que la longueur minimale.
    mots_long = []
    # mot_actuel = "": Initialise une chaîne vide qui sera utilisée pour construire le mot actuel lors du parcours de la chaîne de caractères.
    mot_actuel = ""
    # en_mot = False: Initialise un indicateur pour suivre si nous sommes actuellement en train de construire un mot.
    en_mot = False
# La boucle for caractere in chaine: parcourt chaque caractère de la chaîne.
    for caractere in chaine:
        # if caractere.isalnum():: Vérifie si le caractère est alphanumérique.
        # Si c'est le cas, cela signifie que nous sommes dans un mot,
        # alors le caractère est ajouté à mot_actuel et l'indicateur en_mot est mis à True.
        if caractere.isalnum():
            mot_actuel += caractere
            en_mot = True
            # elif en_mot:: Si nous étions précédemment en train de construire un mot et que le caractère actuel n'est pas alphanumérique,
            # cela signifie que le mot actuel est terminé. On vérifie ensuite si la longueur du mot actuel est supérieure à la longueur minimale spécifiée (longueur_minimale).
            # Si oui,le mot est ajouté à la liste mots_long, et les variables mot_actuel et en_mot sont réinitialisées.
        elif en_mot:
            if len(mot_actuel) > longueur_minimale:
                mots_long.append(mot_actuel)
            mot_actuel = ""
            en_mot = False
    # Après la boucle, il y a une vérification supplémentaire pour ajouter le dernier mot si la phrase se termine par un mot.
    # Ajouter le dernier mot si la phrase se termine par un mot
    if len(mot_actuel) > longueur_minimale:
        
        mots_long.append(mot_actuel)
    # Enfin, la fonction retourne une chaîne de mots concaténés avec des espaces à l'aide de " ".join(mots_long).
    return " ".join(mots_long)
# L'exemple d'utilisation montre comment appeler la fonction avec une longueur minimale de 3 et une phrase donnée.
longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance."

# Appeler la fonction pour obtenir les mots plus longs que la longueur minimale
resultat = my_long_word(longueur_minimale, phrase)

# Le résultat est ensuite affiché.
print(f"Mots plus longs que {longueur_minimale} caractères : {resultat}")
