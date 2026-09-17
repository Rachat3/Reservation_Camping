# Reservation de Camping
#1. Les Entrees
# ce que l'utilisateur doit saisir( le numbre de nuits)
nb_nuits = int(input("Enter the number of nuits: "))
#2.Les Traitements
#A.Determiner le prix de la nuits, calculer le sous-total et les taxes.
if nb_nuits >= 30:
    prix_nuits = 25
else:
    prix_nuits = 35
#B. Calcauls financiers
sous_total = prix_nuits * nb_nuits
tps = sous_total * 0.05
tvq = sous_total * 0.09975
total_avec_taxes = sous_total + tps + tvq
#3. Les Sorties
# Afficher le resume, le sous-total avec taxes.
print(f"duree du sejours: {nb_nuits} nuits a {prix_nuits} $")
print(f"sous-total: {sous_total:.2f} $")
print(f"total avec taxes: {total_avec_taxes:.2f} $")