# Initialisation des variables
montant_initial = 20000 
rendement_annuel = 10.0  

# Affichage du gain annuel en fonction du taux de rendement initial
gain_annuel = (rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel:.2f} euros")

# Augmentation du capital de 10 000 euros et augmentation du taux de rendement de 2%
montant_initial += 10000
rendement_annuel += 2
# -------------------------------------------------------------------------------------------------------------------
# Calcul du nouveau gain annuel
nouveau_gain = (rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel : {nouveau_gain:.2f} euros")

# Retrait de 10% représenté par 0.10 du montant total et diminution du taux de rendement de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
rendement_annuel -= 1

# Calcul du montant final de l'investissement et du nouveau gain
montant_final = montant_initial + nouveau_gain
print(f"Montant final de l'investissement : {montant_final:.2f} euros")
