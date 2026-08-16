import csv

totals = {}

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["categorie"]
        amount = float(row["montant"])
        if category not in totals:
            totals[category] = 0
        totals[category] = totals[category] + amount

print("Dépenses de janvier")
print("-" * 30)

for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{category}: {amount:.2f} €")
