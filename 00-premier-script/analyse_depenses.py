import csv 

total_depense = 0
total_par_categie = {}
with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        categorie = row["categorie"]
        montant= float(row["montant"])

        if categorie not in total_par_categie:
            total_par_categie[categorie] = 0

        total_par_categie[categorie] += montant
            
total_depense = sum(total_par_categie.values())

print("="*40)
print(f"total depense: {total_depense:.2f} €")
print("total depense par categorie")
for categorie, montant in sorted(total_par_categie.items(), key=lambda x: x[1], reverse=True):
    print(f"{categorie}:  {montant:.2f}")