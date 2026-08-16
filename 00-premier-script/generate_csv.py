import csv
import random
from datetime import date

random.seed(20260125)

MERCHANTS = {
    "Courses": [
        "Carrefour Market", "Monoprix", "Lidl", "Intermarche", "Franprix",
        "Auchan", "Leclerc Drive", "Naturalia", "Grand Frais", "Picard",
        "Boulangerie Saint-Michel", "Boucherie Fontaine", "Marche Bastille",
        "Biocoop", "Nicolas",
    ],
    "Restaurant": [
        "Le Petit Bistrot", "Cafe de la Gare", "Pizzeria Napoli", "Sushi Yaki",
        "Le Comptoir", "Brasserie du Nord", "Chez Mamou", "O Tacos",
        "Bagel Corner", "Le Bouillon", "Cantine Merci", "Starbucks Republique",
        "Paul", "Columbus Cafe", "La Fontaine",
    ],
    "Transport": [
        "SNCF Connect", "RATP Navigo", "Uber", "Velib Metropole",
        "Total Energies", "BlaBlaCar", "Station Esso", "Parking Vinci",
        "Trainline", "Free Now", "Cityscoot",
    ],
    "Loisirs": [
        "Cinema Pathe", "FNAC", "Decathlon", "Librairie Mollat",
        "Basic Fit", "Musee d'Orsay", "Ticketmaster", "Cultura",
        "Piscine Municipale", "Theatre du Rond-Point",
    ],
    "Sante": [
        "Pharmacie du Centre", "Dr Lemoine", "Laboratoire Cerba",
        "Optique Krys", "Pharmacie Lafayette", "Dentiste Moreau",
        "Kinesitherapeute Dubois",
    ],
    "Abonnements": [
        "Spotify", "Netflix", "Orange Mobile", "Free Internet",
        "Amazon Prime", "Le Monde Numerique", "iCloud", "Deezer",
    ],
    "Logement": [
        "EDF Electricite", "Veolia Eau", "Assurance Habitation",
        "Engie Gaz", "Charges Copropriete", "Bricorama",
    ],
}

# (count, min, max) - tuned for a believable two-person household month
SPEC = {
    "Courses":     (72,  3.20,  24.00),
    "Restaurant":  (58,  3.80,  26.00),
    "Transport":   (45,  1.90,  24.00),
    "Loisirs":     (26,  5.50,  36.00),
    "Sante":       (17,  5.50,  48.00),
    "Abonnements": (15,  4.99,  24.99),
    "Logement":    (13, 12.00,  62.00),
}

rows = []
for category, (count, lo, hi) in SPEC.items():
    for _ in range(count):
        rows.append((
            date(2026, 1, random.randint(1, 31)),
            random.choice(MERCHANTS[category]),
            round(random.uniform(lo, hi), 2),
            category,
        ))

# The rent - one big line on the 3rd, keeps Logement clearly on top
rows.append((date(2026, 1, 3), "Loyer Janvier", 1250.00, "Logement"))

# Sort by date only, shuffling within each day - real statements are not alphabetical
random.shuffle(rows)
rows.sort(key=lambda r: r[0])

with open("depenses_janvier.csv", "w", newline="\n", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["date", "description", "montant", "categorie"])
    for d, desc, amount, cat in rows:
        w.writerow([d.isoformat(), desc, f"{amount:.2f}", cat])

# Report
totals = {}
for _, _, amount, cat in rows:
    totals[cat] = totals.get(cat, 0) + amount

print(f"rows: {len(rows)}")
print(f"TOTAL: {sum(r[2] for r in rows):.2f} EUR\n")
for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
    print(f"  {cat:14s} {amt:8.2f}")
