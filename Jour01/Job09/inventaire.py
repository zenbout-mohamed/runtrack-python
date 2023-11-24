# La 1ère étape consiste à organiser et assigner une valeur correspondante.
nom_produit = "Voiture"
prix_unitaire = 6500
stock = 5

print(f"Nom du produit : {nom_produit}")
print(f"le prix unitaire est {prix_unitaire}")
print(f"Quantité en stock : {stock} unités\n ")


# Ajout de produits en stock
quantite_selectionnee = int(input("Quantité produit : "))
stock += quantite_selectionnee

# Mise à jour du prix unitaire suite à l'inflation
nouveau_prix_unitaire = prix_unitaire * 1.10
prix_unitaire = round(nouveau_prix_unitaire, 2)

print('Le nouveau prix selon la quantité que vous venez de sélectionner est :', +nouveau_prix_unitaire)
# Résultat aprés mise à jour des données
print("\nInformations mises à jour sur le produit après achat et inflation :")
print(f"Nom du produit : {nom_produit}")
print(f"Nouveau prix unitaire : ${prix_unitaire:.2f}")
print(f"Nouvelle quantité en stock : {stock} unités")


