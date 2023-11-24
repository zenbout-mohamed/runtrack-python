def decaler_message(message, espacement):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resultat = ''

    for lettre in message:
        if lettre.isalpha():  # Vérifier si la lettre est alphabétique
            majuscule = lettre.isupper()  # Vérifier si la lettre est en majuscule

            lettre = lettre.lower()  # Convertir en minuscule pour le traitement

            if lettre in alphabet:
                indice = (alphabet.index(lettre) + espacement) % 26
                # Assigne à nouvelle_lettre la lettre située à l'indice indice dans la séquence alphabet.
                # Si indice a la valeur 0, nouvelle_lettre contiendra la première lettre de alphabet, si indice a la valeur 1,
                # elle contiendra la deuxième lettre, et ainsi de suite.
                nouvelle_lettre = alphabet[indice]

                if majuscule:
                    # On utilise la méthode upper() pour convertir une chaîne de caractères en majuscules.
                    nouvelle_lettre = nouvelle_lettre.upper()

                resultat += nouvelle_lettre
            else:
                resultat += lettre
        else:
            resultat += lettre

    return resultat

# Exemple d'utilisation de la fonction
original = "Hello, World!"
espacement = 3
message_espace = decaler_message(original, espacement)

# Afficher le résultat
print(f"Message original: {original}")
print(f"Message :   {message_espace}")
