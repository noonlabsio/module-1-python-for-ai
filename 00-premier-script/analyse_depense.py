import csv
total_depense = 0
depense_par_categorie = {}
with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        categorie = row["categorie"]
        montant = float(row["montant"])

        if categorie not in depense_par_categorie:
            depense_par_categorie[categorie] = 0
        depense_par_categorie[categorie] += montant
        total_depense += float(row["montant"])

    print("="*40)
    print(f"total depense: {total_depense:.2f}")
    print(f"Depense par categorie")
    for categorie, montant in sorted(depense_par_categorie.items(), key = lambda x: x[1], reverse=True):
        print(f"{categorie}:  {montant:.2f}")
    