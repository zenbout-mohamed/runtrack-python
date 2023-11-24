def time_to_text(minutes):
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    # Construire la chaîne de caractères
    texte_duree =f"{heures} heures et {minutes_restantes} minutes"
    print(texte_duree)

# Exemple d'utilisation de la fonction
# Autrement il affichera en conversion "2 heures et 15 minutes"

time_to_text(135) 