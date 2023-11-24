# Nous devons imposer à l'utilisateur un champ à remplir afin d'analyser si la chaine de caractère correspondant au choix de l'utilisateur comporte un "e"
phrase = input("Rédigez une phrase : ")

# VNous vérifions si la phrase de l'utilisateur comporte la lettre "e"
if 'e' in phrase:
    print("La phrase comporte la lettre 'e'.")
else:
    print("La phrase ne comporte pas la lettre 'e'.")
