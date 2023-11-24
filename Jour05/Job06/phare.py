def dist_wc(nombre_de_marches, hauteur_marche_cm):
    # 1 semaine = 7 jours
    nombre_de_jours_par_semaine = 7
    nombre_de_allers_retours_par_semaine = 2
    # nous déclarons nos variables
    hauteur_totale_cm = nombre_de_marches * hauteur_marche_cm * nombre_de_allers_retours_par_semaine
    # Puis nous utiliserons la conversion des cm en m
    hauteur_totale_m = hauteur_totale_cm / 100  
    distance_parcourue_m = hauteur_totale_m * nombre_de_jours_par_semaine

    print(f"Pour {nombre_de_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_parcourue_m:.2f} m par semaine.")

 
nombre_de_marches = 10
hauteur_marche_cm = 20
# Nous affichons la fonction
dist_wc(nombre_de_marches, hauteur_marche_cm)
