def arrondir_notes(liste_notes):
    notes_arrondies = []
    # La boucle for parcourt chaque note dans la liste d'origine.
    for note in liste_notes:
        # Si la note est inférieure à 40, l'étudiant échoue, et la note n'est pas arrondie à la hausse.
        if note < 40:
            # Étudiant échoue, pas d'arrondi à la hausse
            notes_arrondies.append(note)
        else:
            # Étudiant réussit, vérifier les critères d'arrondi
            multiple_de_5_suivant = (note + 4) // 5 * 5
            # Si la note est supérieure ou égale à 40, les critères d'arrondi sont vérifiés.
            # Le prochain multiple de 5 est calculé, et si la différence entre la note et ce multiple est strictement inférieure à 3.
            # La note est arrondie à ce multiple. Sinon, la note reste inchangée.
            if multiple_de_5_suivant - note < 3:
                notes_arrondies.append(multiple_de_5_suivant)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation de la fonction
liste_notes = [35, 48, 72, 83, 92]

# Appeler la fonction pour arrondir les notes
notes_arrondies = arrondir_notes(liste_notes)

# Afficher le résultat
print("Notes originales   :", liste_notes)
print("Notes arrondies    :", notes_arrondies)
