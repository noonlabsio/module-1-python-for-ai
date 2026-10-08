import csv
total = 0
total_par_categorie = {}

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        categorie = row["categorie"]
        amount = float(row["montant"])
        if categorie not in total_par_categorie: 
            total_par_categorie[categorie] = 0
        total_par_categorie[categorie] += amount
        total += amount

print("=" * 40)
print(f"Total des dépenses: {sum(total_par_categorie.values()):.2f} €")

for categorie, montant in sorted(total_par_categorie.items(), key=lambda x: x[1], reverse=True):
    print(f"{categorie}: {montant:.2f} €")
print("=" * 40)
