# LE CODE

## Progression à l'écran (5 états)

**Étape 1 — Lire et explorer** *(Section 3)*

```python
import csv

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

**Étape 2 — L'erreur volontaire** *(Section 4 — supprimer la boucle ci-dessus d'abord)*

```python
import csv

total = 0

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = total + row["montant"]

print(total)
```

→ `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

**Étape 3 — Le fix `float()`**

```python
import csv

total = 0

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = total + float(row["montant"])

print(total)
```

**Étape 4 — Filtrer une catégorie** *(Section 5)*
```python
import csv

total = 0

with open("depenses_janvier.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["categorie"] == "Restaurant":
            total = total + float(row["montant"])

print(total)
```

**Étape 5 — Toutes les catégories**

```python
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

print(totals)
```

## Version finale — `analyse_depenses.py`

```python
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
```

## Le CSV — `depenses_janvier.csv`

Schéma verrouillé. Colonnes sans accent, point décimal, virgule comme séparateur, montants positifs.

```csv
date,description,montant,categorie
2026-01-02,Carrefour Market,47.20,Courses
2026-01-03,Le Petit Bistrot,32.50,Restaurant
2026-01-03,SNCF Connect,89.00,Transport
2026-01-04,Loyer Janvier,850.00,Logement
2026-01-05,Pharmacie du Centre,18.90,Sante
2026-01-05,Spotify,10.99,Abonnements
2026-01-06,Cinema Pathe,12.50,Loisirs
```

**Catégories :** Restaurant, Courses, Transport, Loisirs, Sante, Abonnements, Logement **À générer :** 247 lignes réparties sur janvier 2026, noms de marchands français réalistes. Tâche de préparation au tournage — pas aujourd'hui.
```python
import csv
total_per_category = {}
with open('depenses_janvier.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row['categorie'] 
        amount = float(row['montant']) 
        if category not in total_per_category:
            total_per_category[category] = 0
        total_per_category[category] += amount
total_depense = sum(total_per_category.values())

print("="*30)
print(f"Total dépenses : {total_depense} €")
print()
print("Total dépenses per catégorie")
for category, amount in sorted(total_per_category.items(), key=lambda x: x[1], reverse=True):
    print(f"{category} : {amount:.2f} €")
```

