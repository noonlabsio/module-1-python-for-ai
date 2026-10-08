"""Chapter 13 — re-run every fact that appears on a slide or in a note.

Like chapter 12, this script imports third-party libraries, by approved
exception to the skill's stdlib-only rule. Pin the versions when you run it,
without touching the repo:

    uv run --no-project --python 3.12 --with pandas==3.0.6 --with pyarrow==25.0.1 \\
        --with polars==2.0.0 --with duckdb==1.5.6 \\
        python 13-pandas-and-modern-dataframe-libraries/verify-facts.py

Verified on CPython 3.12.3 with pandas 3.0.6, pyarrow 25.0.1, NumPy 2.5.3,
Polars 2.0.0 and DuckDB 1.5.6. The deck describes pandas 3 (Copy-on-Write,
the str dtype, microsecond datetimes, 'ME'); the script refuses pandas 2.

Every number comes from ../00-premier-script/depenses_janvier.csv, the first
video's data, so a change to that file shows up here. Slide 12 times real
work and asserts the direction only.

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 21-slide deck: 01 cover, 02 divider, 03-20
content, 21 closing card.
"""

import io
import sys
import tempfile
import time
import warnings
from collections import Counter
from pathlib import Path

import duckdb
import numpy as np
import pandas as pd
import polars as pl
import pyarrow

FAILS = []


def check(slide, label, actual, expected):
    ok = actual == expected
    if not ok:
        FAILS.append((slide, label))
    print(f"{'[ok]   ' if ok else '[DRIFT]'} s{slide:02} {label}")
    if not ok:
        print(f"         slide says:  {expected!r}")
        print(f"         python says: {actual!r}")


def raises(fn):
    """The exception as Python prints it on the last traceback line, or a marker."""
    try:
        fn()
    except Exception as e:
        return f"{type(e).__name__}: {e}"
    return "<no exception>"


def info(slide, text):
    print(f"[info]  s{slide:02} {text}")


if int(pd.__version__.split(".")[0]) < 3:
    sys.exit(f"pandas {pd.__version__}: this deck describes pandas 3")
print(f"CPython {sys.version}")
print(f"pandas {pd.__version__}, pyarrow {pyarrow.__version__}, NumPy {np.__version__}, "
      f"Polars {pl.__version__}, DuckDB {duckdb.__version__}\n")
CSV = Path(__file__).resolve().parent.parent / "00-premier-script" / "depenses_janvier.csv"
TMP = Path(tempfile.mkdtemp(prefix="nl-ch13-"))
df = pd.read_csv(CSV)


# ── slide 3 · from CSV to DataFrame ───────────────────────────────────────
check(3, "shape (247, 4)", df.shape, (247, 4))
check(3, "3 str columns, 1 float64", dict(df.dtypes.astype(str)),
      {"date": "str", "description": "str", "montant": "float64", "categorie": "str"})
buf = io.StringIO()
df.info(buf=buf)
text = buf.getvalue()
check(3, "info() names the class pandas.DataFrame", "<class 'pandas.DataFrame'>" in text, True)
check(3, "info(): no missing value", "247 non-null" in text and text.count("247 non-null") == 4, True)
d = df.describe()["montant"]
check(3, "describe(): mean 21.49, max 1250.00", (round(d["mean"], 2), round(d["max"], 2)), (21.49, 1250.0))
check(3, "describe() lists count, mean, std, quartiles",
      d.index.tolist(), ["count", "mean", "std", "min", "25%", "50%", "75%", "max"])
check(3, "the float sum is 5308.389999999999", repr(df["montant"].sum()), "np.float64(5308.389999999999)")
check(3, "loadtxt cannot read the text columns",
      raises(lambda: np.loadtxt(CSV, delimiter=",", skiprows=1)).split(":")[0], "ValueError")


# ── slide 4 · Series (the PLANT) ──────────────────────────────────────────
s = pd.Series([13.16, 5.5], index=["Resto", "Courses"])
check(4, "s['Courses'], s.dtype", repr((s["Courses"], s.dtype)), "(np.float64(5.5), dtype('float64'))")
check(4, "s.iloc[0] by position", s.iloc[0], 13.16)
check(4, "adding aligns on labels, not positions",
      str(s + pd.Series([1.0], index=["Resto"])), "Courses      NaN\nResto      14.16\ndtype: float64")
check(4, ".index, .values, .dtype, .name exist", all(hasattr(s, a) for a in ("index", "values", "dtype", "name")), True)
check(4, "every column of a DataFrame is a Series", isinstance(df["montant"], pd.Series), True)


# ── slide 5 · loc & iloc ──────────────────────────────────────────────────
check(5, "df.loc[0, 'categorie']", df.loc[0, "categorie"], "Restaurant")
check(5, "df.iloc[0, 2]", df.iloc[0, 2], 13.16)
check(5, "loc[:2] includes the end: 3 rows", len(df.loc[:2]), 3)
check(5, "iloc[:2] excludes it: 2 rows", len(df.iloc[:2]), 2)
check(5, "loc[:2, [cols]] and iloc[:2, [1, 2]]",
      (df.loc[:2, ["description", "montant"]].shape, df.iloc[:2, [1, 2]].columns.tolist()),
      ((3, 2), ["description", "montant"]))


# ── slide 6 · boolean filters & query ─────────────────────────────────────
big = df[df["montant"] > 100]
check(6, "one expense above 100: the rent", (len(big), big["categorie"].iloc[0], big["montant"].iloc[0]),
      (1, "Logement", 1250.0))
resto = df[(df["categorie"] == "Restaurant") & (df["montant"] > 20)]
q = df.query("categorie == 'Restaurant' and montant > 20")
check(6, "17 rows either way", (len(resto), len(q), resto.index.equals(q.index)), (17, 17, True))


# ── slide 7 · adding & modifying columns ──────────────────────────────────
d = df.copy()
d["ttc"] = d["montant"] * 1.2
check(7, "a computed column", round(d.loc[0, "ttc"], 3), 15.792)
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    d["montant"][0] = 0
names = [w.category.__name__ for w in caught]
check(7, "chained assignment warns ChainedAssignmentError", "ChainedAssignmentError" in names, True)
check(7, "... and changes nothing", d.loc[0, "montant"], 13.16)
check(7, "the warning says it never works",
      any("chained assignment never works" in " ".join(str(w.message).split()) for w in caught), True)
d.loc[0, "montant"] = 0
check(7, "one .loc assignment works", d.loc[0, "montant"], 0.0)
sel = df[df["montant"] > 100]
sel["montant"] = 0
check(7, "Copy-on-Write: changing a selection leaves the original", df["montant"].max(), 1250.0)
check(7, "assign with pd.col (3.0)", round(df.assign(ttc=pd.col("montant") * 1.2).loc[0, "ttc"], 3), 15.792)
check(7, "SettingWithCopyWarning no longer exists", hasattr(pd.errors, "SettingWithCopyWarning"), False)


# ── slide 8 · missing data ────────────────────────────────────────────────
m = pd.Series([1.0, None, 3.0])
check(8, "None becomes NaN; isnull", m.isnull().tolist(), [False, True, False])
check(8, "fillna(0)", m.fillna(0).tolist(), [1.0, 0.0, 3.0])
check(8, "interpolate()", m.interpolate().tolist(), [1.0, 2.0, 3.0])
check(8, "dropna()", m.dropna().tolist(), [1.0, 3.0])
check(8, "mean() skips NaN", repr(m.mean()), "np.float64(2.0)")
check(8, "unless skipna=False", bool(np.isnan(m.mean(skipna=False))), True)
check(8, "NumPy's mean returns nan (chapter 12)", bool(np.isnan(np.mean(m.to_numpy()))), True)


# ── slide 9 · type conversion ─────────────────────────────────────────────
coerced = pd.to_numeric(pd.Series(["1.5", "abc"]), errors="coerce").tolist()
check(9, "errors='coerce' gives [1.5, nan]", (coerced[0], bool(np.isnan(coerced[1]))), (1.5, True))
check(9, "without it, to_numeric raises", raises(lambda: pd.to_numeric(pd.Series(["1.5", "abc"]))),
      'ValueError: Unable to parse string "abc" at position 1')
check(9, "dates parse to microseconds (pandas 3)", pd.to_datetime(df["date"]).dtype.name, "datetime64[us]")
cat = df["categorie"].astype("category")
check(9, "7 categories", len(cat.cat.categories), 7)
check(9, "category uses less memory than str",
      cat.memory_usage(deep=True) < df["categorie"].memory_usage(deep=True), True)
check(9, "float('abc') raises too (chapter 02)", raises(lambda: float("abc")).split(":")[0], "ValueError")


# ── slide 10 · the .str accessor ──────────────────────────────────────────
desc = df["description"]
check(10, ".str.upper()", desc.str.upper().iloc[0], "LA FONTAINE")
check(10, ".str.contains('Carrefour'): 5 rows", int(desc.str.contains("Carrefour").sum()), 5)
check(10, ".str.split(' ').str[0]", desc.str.split(" ").str[0].iloc[0], "La")
check(10, "a text column has the str dtype", str(desc.dtype), "str")
check(10, "code testing for object breaks", desc.dtype == object, False)
strs = pd.Series(["a", "b"])


def _put_int():
    strs[0] = 1


check(10, "a str column holds only strings or NaN", raises(_put_int) != "<no exception>", True)


# ── slide 11 · index, labels & duplicates ─────────────────────────────────
renamed = df.rename(columns={"montant": "amount"})
check(11, "rename returns a new frame", ("amount" in renamed.columns, "montant" in df.columns), (True, True))
check(11, "set_index makes dates the labels", df.set_index("date").index.name, "date")
check(11, "reset_index turns labels back into a column", "date" in df.set_index("date").reset_index().columns, True)
re3 = df.reindex([0, 1, 999])
check(11, "reindex: an unknown label gets a row of NaN", (len(re3), bool(re3.loc[999].isna().all())), (3, True))
check(11, "no fully repeated row", int(df.duplicated().sum()), 0)
check(11, "178 repeated descriptions", int(df.duplicated(subset=["description"]).sum()), 178)
check(11, "drop_duplicates keeps 247 rows", len(df.drop_duplicates()), 247)


# ── slide 12 · apply, map & transform ─────────────────────────────────────
check(12, "map(round)", df["montant"].map(round).iloc[0], 13)
mapped = df["categorie"].map({"Sante": "Santé"})
n_sante = int((df["categorie"] == "Sante").sum())
check(12, "map with a dict: every unmatched value becomes NaN", int(mapped.isna().sum()), 247 - n_sante)
check(12, "replace keeps the others",
      df["categorie"].replace({"Sante": "Santé"}).isna().sum() == 0 and "Santé" in df["categorie"].replace({"Sante": "Santé"}).values,
      True)
t = time.perf_counter()
applied = df.apply(lambda r: r["montant"] * 2, axis=1)
slow = time.perf_counter() - t
t = time.perf_counter()
vector = df["montant"] * 2
fast = time.perf_counter() - t
info(12, f"apply(axis=1) {slow * 1000:.2f} ms, column arithmetic {fast * 1000:.3f} ms")
check(12, "apply(axis=1) gives the same values", applied.equals(vector), True)
check(12, "... much more slowly (over 10x on this file)", slow / fast > 10, True)
check(12, "transform keeps the input's shape", len(df.groupby("categorie")["montant"].transform("sum")), 247)


# ── slide 13 · groupby (the PAYOFF) ───────────────────────────────────────
g = df.groupby("categorie")["montant"]
totals = g.sum().sort_values(ascending=False)
check(13, "totals by category, largest first",
      [(k, round(v, 2)) for k, v in totals.items()],
      [("Logement", 1670.03), ("Courses", 955.33), ("Restaurant", 880.41), ("Transport", 659.47),
       ("Loisirs", 474.18), ("Sante", 467.83), ("Abonnements", 201.14)])
check(13, "Restaurant prints 880.41", repr(totals["Restaurant"]), "np.float64(880.41)")
part = df["montant"] / g.transform("sum")
check(13, "transform: each row's share of its category", round(part.iloc[0], 4), 0.0149)
check(13, "the shares add up to 1 per category", np.allclose(part.groupby(df["categorie"]).sum(), 1), True)
check(13, "filter keeps whole groups above 900",
      sorted(df.groupby("categorie").filter(lambda x: x["montant"].sum() > 900)["categorie"].unique()),
      ["Courses", "Logement"])
check(13, "no sorting needed", df.sample(frac=1, random_state=0).groupby("categorie")["montant"].sum().round(2).equals(
      g.sum().round(2)), True)
check(13, "value_counts is Counter for a column",
      df["categorie"].value_counts().to_dict(), dict(Counter(df["categorie"])))


# ── slide 14 · pivot tables & crosstab ────────────────────────────────────
dd = df.copy()
dd["semaine"] = pd.to_datetime(dd["date"]).dt.isocalendar().week
pt = pd.pivot_table(dd, index="categorie", columns="semaine", values="montant", aggfunc="sum")
check(14, "one row per category", pt.shape[0], 7)
check(14, "the grid holds the same total", round(float(pt.sum().sum()), 2), 5308.39)
ct = pd.crosstab(dd["categorie"], dd["semaine"])
check(14, "crosstab cells add up to 247", int(ct.to_numpy().sum()), 247)
check(14, "ISO weeks start on Monday",
      (pd.Timestamp("2026-01-04").isocalendar().week, pd.Timestamp("2026-01-05").isocalendar().week), (1, 2))


# ── slide 15 · merge, join & concat ───────────────────────────────────────
budget = pd.DataFrame({"categorie": ["Courses", "Logement"], "plafond": [900, 1700]})
left = df.merge(budget, on="categorie", how="left")
n_both = int(df["categorie"].isin(["Courses", "Logement"]).sum())
check(15, "a left merge keeps all 247 rows", len(left), 247)
check(15, "rows without a budget get NaN", int(left["plafond"].isna().sum()), 247 - n_both)
check(15, "inner keeps only keys in both", len(df.merge(budget, on="categorie", how="inner")), n_both)
check(15, "outer keeps every key", len(df.merge(budget, on="categorie", how="outer")), 247)
check(15, "join matches the index",
      len(df.join(budget.set_index("categorie"), on="categorie")), 247)
a2, b2 = df.iloc[:3], df.iloc[3:5]
check(15, "concat stacks rows", len(pd.concat([a2, b2])), 5)
check(15, "concat(axis=1) aligns columns on the index",
      pd.concat([df[["date"]], df[["montant"]]], axis=1).shape, (247, 2))


# ── slide 16 · time series ────────────────────────────────────────────────
ts = df.assign(date=pd.to_datetime(df["date"])).set_index("date")["montant"]
check(16, "a DatetimeIndex", isinstance(ts.index, pd.DatetimeIndex), True)
check(16, "resample('ME').sum(): 5308.39", round(ts.resample("ME").sum().iloc[0], 2), 5308.39)
w = ts.resample("W").sum()
check(16, "weekly totals start 1741.86, 825.12", [round(x, 2) for x in w.iloc[:2]], [1741.86, 825.12])
pc = w.pct_change().round(3).iloc[:2].tolist()
check(16, "pct_change: nan, -0.526", (bool(np.isnan(pc[0])), pc[1]), (True, -0.526))
check(16, "shift(1) moves one period", round(w.shift(1).iloc[1], 2), 1741.86)
check(16, "rolling(7) first values", ts.resample("D").sum().rolling(7).mean().dropna().round(2).iloc[:2].tolist(),
      [287.66, 300.56])
check(16, "'M' is gone (pandas 3)", raises(lambda: ts.resample("M").sum()),
      "ValueError: Invalid frequency: M. Failed to parse with error message: "
      "ValueError(\"'M' is no longer supported for offsets. Please use 'ME' instead.\")")
check(16, "QE and YE replace Q and Y", (len(ts.resample("QE").sum()), len(ts.resample("YE").sum())), (1, 1))


# ── slide 17 · reading & writing files ────────────────────────────────────
typed = df.assign(date=pd.to_datetime(df["date"]))
typed.to_csv(TMP / "with_index.csv")
typed.to_csv(TMP / "out.csv", index=False)
check(17, "without index=False, a column is added", "Unnamed: 0" in pd.read_csv(TMP / "with_index.csv").columns, True)
check(17, "with index=False, no extra column", pd.read_csv(TMP / "out.csv").shape, (247, 4))
check(17, "CSV turns dates back into text", str(pd.read_csv(TMP / "out.csv")["date"].dtype), "str")
typed.to_parquet(TMP / "depenses.parquet")
back = pd.read_parquet(TMP / "depenses.parquet")
check(17, "Parquet keeps the date type", back["date"].dtype.kind, "M")
check(17, "Parquet keeps every value", back["montant"].equals(typed["montant"]), True)
df.to_json(TMP / "depenses.json")
check(17, "read_json reads it back", pd.read_json(TMP / "depenses.json").shape, (247, 4))


# ── slide 18 · pitfalls ───────────────────────────────────────────────────
check(18, "pd.__version__ is pandas 3", pd.__version__.split(".")[0], "3")



# ── slide 19 · Polars ─────────────────────────────────────────────────────
lazy = pl.scan_csv(CSV)
check(19, "scan_csv returns a LazyFrame, a plan", type(lazy).__name__, "LazyFrame")
top = (lazy.group_by("categorie").agg(pl.col("montant").sum()).sort("montant", descending=True).collect())
check(19, "the same top three as pandas",
      [(r[0], round(r[1], 2)) for r in top.head(3).rows()], [("Logement", 1670.03), ("Courses", 955.33), ("Restaurant", 880.41)])
check(19, "to_pandas() crosses over", type(top.to_pandas()).__name__, "DataFrame")
check(19, "pl.from_pandas() crosses back", pl.from_pandas(df).shape, (247, 4))
check(19, "Polars is multithreaded", pl.thread_pool_size() > 1, True)


# ── slide 20 · DuckDB ─────────────────────────────────────────────────────
rows = duckdb.sql(f"""
  SELECT categorie, round(sum(montant), 2)
  FROM '{CSV}'
  GROUP BY 1 ORDER BY 2 DESC LIMIT 3
""").fetchall()
check(20, "SQL straight on the CSV", rows, [("Logement", 1670.03), ("Courses", 955.33), ("Restaurant", 880.41)])
check(20, "a pandas variable is a table", duckdb.sql("SELECT count(*) FROM df").fetchone(), (247,))
ranked = duckdb.sql("SELECT categorie, montant, rank() OVER (PARTITION BY categorie ORDER BY montant DESC) AS r "
                    "FROM df QUALIFY r = 1 ORDER BY montant DESC LIMIT 1").fetchone()
check(20, "window functions (OVER)", (ranked[0], ranked[1]), ("Logement", 1250.0))
exts = [r[0] for r in duckdb.sql("SELECT extension_name FROM duckdb_extensions()").fetchall()]
check(20, "the httpfs extension is available (s3:// paths)", "httpfs" in exts, True)
check(20, "reads a Polars frame too", duckdb.sql("SELECT count(*) FROM top").fetchone(), (7,))

print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
