"""Chapter 14 — re-run every fact that appears on a slide or in a note.

Like chapters 12 and 13, this script imports third-party libraries, by
approved exception to the skill's stdlib-only rule. Pin the versions when you
run it, without touching the repo. Leave kaleido out: slide 17 states that
write_image fails without it.

    uv run --no-project --python 3.12 --with pandas==3.0.6 \\
        --with matplotlib==3.11.2 --with seaborn==0.13.2 --with plotly==7.1.0 \\
        python 14-data-visualization/verify-facts.py

Verified on CPython 3.12.3 with pandas 3.0.6, NumPy 2.5.3, matplotlib 3.11.2,
seaborn 0.13.2 and plotly 7.1.0 (plotly.js 4.1.1). PNG sizes are read from
the file header with struct, so Pillow is not needed.

Every number comes from ../00-premier-script/depenses_janvier.csv, the first
video's data, so a change to that file shows up here. The figures on the
slides are drawn by make-figures.py from the same file; the first check makes
sure every figure the deck references exists.

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 19-slide deck: 01 cover, 02 divider, 03-18
content, 19 closing card.
"""

import inspect
import re
import struct
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import seaborn as sns

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


def png_size(path):
    """(width, height) from the IHDR chunk of a PNG file."""
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


print(f"CPython {sys.version}")
print(f"pandas {pd.__version__}, NumPy {np.__version__}, matplotlib {matplotlib.__version__}, "
      f"seaborn {sns.__version__}, plotly {plotly.__version__}\n")
CSV = Path(__file__).resolve().parent.parent / "00-premier-script" / "depenses_janvier.csv"
TMP = Path(tempfile.mkdtemp(prefix="nl-ch14-"))
df = pd.read_csv(CSV)
df["date"] = pd.to_datetime(df["date"])
totals = df.groupby("categorie")["montant"].sum().sort_values()
small = df.loc[df["montant"] < 100, "montant"]
daily = df.set_index("date")["montant"].resample("D").sum()


# ── every slide · the figures exist ──────────────────────────────────────
HERE = Path(__file__).resolve().parent
refs = sorted(re.findall(r'src="\./(figures/[^"]+)"', (HERE / "slides.md").read_text()))
on_disk = sorted(f"figures/{f.name}" for f in (HERE / "figures").iterdir())
check(0, "16 figures referenced, one per content slide", len(refs), 16)
check(0, "every referenced figure exists, and none is unused", refs, on_disk)


# ── slide 3 · Figure, Axes & Artists (the PLANT) ──────────────────────────
fig, ax = plt.subplots()
check(3, "type(ax)", repr(type(ax)), "<class 'matplotlib.axes._axes.Axes'>")
check(3, "ax.figure is fig", ax.figure is fig, True)
lines = ax.plot([1, 2, 3])
check(3, "ax.plot returns [<Line2D ...>]",
      (type(lines).__name__, len(lines), repr(lines[0]).startswith("<matplotlib.lines.Line2D object at 0x")),
      ("list", 1, True))
ax.set_title("Janvier")
check(3, "set_title", ax.get_title(), "Janvier")
kinds = {type(c).__name__ for c in ax.get_children()}
check(3, "the line, the text, the axes are all Artists",
      ({"Line2D", "Text", "XAxis", "Spine"} <= kinds,
       all(isinstance(c, matplotlib.artist.Artist) for c in ax.get_children())), (True, True))
check(3, "a Figure holds Axes", fig.axes, [ax])
plt.close("all")


# ── slide 4 · line & scatter ──────────────────────────────────────────────
check(4, "31 days", len(daily), 31)
check(4, "one spike, January 3: 1430.12",
      (str(daily.idxmax().date()), round(daily.max(), 2)), ("2026-01-03", 1430.12))
check(4, "the spike is the rent day", df.loc[df["montant"].idxmax(), "description"], "Loyer Janvier")
fig, ax = plt.subplots()
ax.plot(daily.index, daily.values)
pts = ax.scatter(df["date"], df["montant"], s=10)
check(4, "scatter: 247 expenses, one dot each", len(pts.get_offsets()), 247)
plt.close("all")


# ── slide 5 · bar & histogram ─────────────────────────────────────────────
check(5, "sorted totals: Abonnements first, Logement last",
      (totals.index[0], totals.index[-1]), ("Abonnements", "Logement"))
fig, ax = plt.subplots()
n, bins, _ = ax.hist(df["montant"], bins=20)
n = n.astype(int).tolist()
check(5, "hist on every expense: 246 | 0 ... 0 | 1", (n[0], set(n[1:-1]), n[-1]), (246, {0}, 1))
check(5, "the lone value is the rent, 1250", df["montant"].max(), 1250.0)
check(5, "246 expenses below 100", len(small), 246)
n2, _, _ = ax.hist(small, bins=20)
check(5, "they spread out (no bin holds most of them)", int(n2.max()) < 50, True)
check(5, "most of them between five and fifty euros", ((small >= 5) & (small <= 50)).mean() > 0.5, True)
plt.close("all")


# ── slide 6 · pie & boxplot ───────────────────────────────────────────────
fig, ax = plt.subplots()
_, _, autotexts = ax.pie(totals, labels=totals.index, autopct="%.1f%%")
pcts = dict(zip(totals.index, (t.get_text() for t in autotexts)))
check(6, "Logement 31.5%", pcts["Logement"], "31.5%")
check(6, "Santé 8.8 vs Loisirs 8.9", (pcts["Sante"], pcts["Loisirs"]), ("8.8%", "8.9%"))
check(6, "seven slices", len(totals), 7)
groups = [df.loc[df["categorie"] == c, "montant"] for c in totals.index]
fig, ax = plt.subplots()
r = ax.boxplot(groups, tick_labels=totals.index)
fliers = {c: f.get_ydata().tolist() for c, f in zip(totals.index, r["fliers"]) if len(f.get_ydata())}
check(6, "one outlier: the rent, in Logement", fliers, {"Logement": [1250.0]})
check(6, "labels= raises a TypeError in 3.11",
      raises(lambda: ax.boxplot(groups, labels=totals.index)),
      "TypeError: Axes.boxplot() got an unexpected keyword argument 'labels'")
plt.close("all")


# ── slide 7 · subplots ────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(10, 6), layout="constrained")
check(7, "axes is a NumPy array of shape (2, 2)", (type(axes).__name__, axes.shape), ("ndarray", (2, 2)))
axes[0, 0].plot(daily.index, daily.values)
axes[0, 1].barh(totals.index, totals.values)
axes[1, 0].hist(small, bins=20)
check(7, "subplots(1, 3) gives shape (3,)", plt.subplots(1, 3)[1].shape, (3,))
plt.close("all")
fig, axes = plt.subplots(1, 2)
plt.title("Janvier")
check(7, "plt.title titles only the last Axes", [a.get_title() for a in axes], ["", "Janvier"])
plt.close("all")


# ── slide 8 · GridSpec ────────────────────────────────────────────────────
fig = plt.figure(layout="constrained")
gs = fig.add_gridspec(2, 3)
top = fig.add_subplot(gs[0, :])
left = fig.add_subplot(gs[1, :2])
right = fig.add_subplot(gs[1, 2])
spans = [(a.get_subplotspec().rowspan, a.get_subplotspec().colspan) for a in (top, left, right)]
check(8, "a whole row, two cells, one cell", spans,
      [(range(0, 1), range(0, 3)), (range(1, 2), range(0, 2)), (range(1, 2), range(2, 3))])
fig, axd = plt.subplot_mosaic("AAA;BBC")
check(8, "subplot_mosaic returns a dict keyed A, B, C", (type(axd).__name__, sorted(axd)), ("dict", ["A", "B", "C"]))
check(8, "... with the same layout",
      [(axd[k].get_subplotspec().rowspan, axd[k].get_subplotspec().colspan) for k in "ABC"], spans)
plt.close("all")


# ── slide 9 · colors & colormaps ──────────────────────────────────────────
cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]
check(9, "C0 is '#1f77b4'", matplotlib.colors.to_hex("C0"), "#1f77b4")
check(9, "the default cycle: C0 to C9", len(cycle), 10)
check(9, "tab:orange is a named color", matplotlib.colors.is_color_like("tab:orange"), True)
cmap = plt.colormaps["viridis"]
lo, hi = cmap(0.0), cmap(1.0)
check(9, "viridis(0.0) is dark purple", (lo[0] < 0.3, lo[1] < 0.1, lo[2] > lo[0]), (True, True, True))
check(9, "viridis(1.0) is yellow", (hi[0] > 0.9, hi[1] > 0.85, hi[2] < 0.2), (True, True, True))
check(9, "viridis is the default colormap", plt.rcParams["image.cmap"], "viridis")
check(9, "jet still exists", "jet" in plt.colormaps(), True)
import matplotlib.cm
check(9, "matplotlib.cm.get_cmap is gone", hasattr(matplotlib.cm, "get_cmap"), False)
lum = [0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b, _ in cmap(np.linspace(0, 1, 11))]
check(9, "viridis: brightness rises at every step", all(b > a for a, b in zip(lum, lum[1:])), True)
lum = [0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b, _ in plt.colormaps["jet"](np.linspace(0, 1, 11))]
check(9, "jet: brightness goes up and down", all(b > a for a, b in zip(lum, lum[1:])), False)


# ── slide 10 · annotations & text ─────────────────────────────────────────
fig, ax = plt.subplots()
ax.plot(daily.index, daily.values)
a = ax.annotate("Loyer : 1250 €",
                xy=(pd.Timestamp("2026-01-03"), 1430.12),
                xytext=(pd.Timestamp("2026-01-10"), 1200),
                arrowprops=dict(arrowstyle="->"))
check(10, "annotate draws text plus an arrow", (type(a).__name__, a.arrow_patch is not None), ("Annotation", True))
check(10, "the point is the daily spike", daily[pd.Timestamp("2026-01-03")].round(2), 1430.12)
check(10, "xy is in data coordinates by default", a.xycoords, "data")
check(10, "ax.text places free text", type(ax.text(0.5, 0.5, "x")).__name__, "Text")
fig, ax = plt.subplots()
bars = ax.barh(totals.index, totals.values)
labels = [t.get_text() for t in ax.bar_label(bars, fmt="%.0f")]
check(10, "bar_label: 201 ... 1670", (labels[0], labels[-1]), ("201", "1670"))
check(10, "every label", labels, ["201", "468", "474", "659", "880", "955", "1670"])
plt.close("all")


# ── slide 11 · 3D ─────────────────────────────────────────────────────────
x = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, x)
Z = np.sin(np.hypot(X, Y))
check(11, "meshgrid: (50, 50)", (X.shape, Y.shape, Z.shape), ((50, 50),) * 3)
fresh = subprocess.run(
    [sys.executable, "-c",
     "import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt\n"
     "ax = plt.figure().add_subplot(projection='3d')\n"
     "print(type(ax).__name__, type(ax).__module__)"],
    capture_output=True, text=True)
check(11, "projection='3d' gives an Axes3D, no import needed",
      fresh.stdout.strip(), "Axes3D mpl_toolkits.mplot3d.axes3d")
ax = plt.figure().add_subplot(projection="3d")
check(11, "plot_surface", type(ax.plot_surface(X, Y, Z, cmap="viridis")).__name__, "Poly3DCollection")
plt.close("all")


# ── slide 12 · saving ─────────────────────────────────────────────────────
fig, ax = plt.subplots()
ax.plot(daily.index, daily.values)
check(12, "default figure: 6.4 × 4.8 inches at 100 dpi", (fig.get_size_inches().tolist(), fig.dpi), ([6.4, 4.8], 100.0))
fig.savefig(TMP / "a.png")
check(12, "default PNG: 640 × 480", png_size(TMP / "a.png"), (640, 480))
fig.savefig(TMP / "b.png", dpi=300)
check(12, "dpi=300: 1920 × 1440", png_size(TMP / "b.png"), (1920, 1440))
fig.savefig(TMP / "c.png", dpi=300, bbox_inches="tight")
w, h = png_size(TMP / "c.png")
check(12, "bbox_inches='tight' trims the margins", w < 1920 and h < 1440, True)
fig.savefig(TMP / "a.pdf")
check(12, "a PDF file", (TMP / "a.pdf").read_bytes()[:5], b"%PDF-")
fig.savefig(TMP / "a.svg")
fig.savefig(TMP / "b.svg", dpi=300)
check(12, "SVG is text", (TMP / "a.svg").read_text().startswith("<?xml"), True)
check(12, "dpi does not change the SVG's size",
      (TMP / "a.svg").stat().st_size == (TMP / "b.svg").stat().st_size, True)
plt.close("all")


# ── slide 13 · seaborn families (the PAYOFF) ──────────────────────────────
ax = sns.barplot(data=df, x="montant", y="categorie", estimator="sum", errorbar=None)
check(13, "type(ax) is a matplotlib Axes", repr(type(ax)), "<class 'matplotlib.axes._axes.Axes'>")
ax.set_title("Janvier")
check(13, "set_title works on it", ax.get_title(), "Janvier")
widths = {t.get_text(): round(p.get_width(), 2) for t, p in zip(ax.get_yticklabels(), ax.patches)}
check(13, "seaborn sums by itself: same totals as slide 5", widths, totals.round(2).to_dict())
plt.close("all")
families = [sns.scatterplot(data=df, x="date", y="montant"), sns.histplot(small),
            sns.boxplot(data=df, x="montant", y="categorie")]
check(13, "each family call returns an Axes", {type(a).__name__ for a in families}, {"Axes"})
plt.close("all")
check(13, "the four families exist",
      all(hasattr(sns, f) for f in ("scatterplot", "lineplot", "histplot", "kdeplot",
                                    "barplot", "boxplot", "heatmap")), True)
df["semaine"] = df["date"].dt.isocalendar().week
pivot = pd.pivot_table(df, index="categorie", columns="semaine", values="montant", aggfunc="sum")
check(13, "the chapter 13 pivot: 7 categories, 5 weeks", pivot.shape, (7, 5))
check(13, "heatmap returns an Axes", type(sns.heatmap(pivot, annot=True, fmt=".0f")).__name__, "Axes")
plt.close("all")
grids = [type(sns.relplot(data=df, x="date", y="montant", kind="line")).__name__,
         type(sns.displot(df, x="montant")).__name__,
         type(sns.catplot(data=df, x="categorie", y="montant", kind="box")).__name__]
check(13, "relplot, displot, catplot return a FacetGrid", grids, ["FacetGrid"] * 3)
check(13, "errorbar= is the 0.13 argument", "errorbar" in inspect.signature(sns.barplot).parameters, True)
plt.close("all")


# ── slide 14 · seaborn styling ────────────────────────────────────────────
p = inspect.signature(sns.set_theme).parameters
check(14, "defaults: darkgrid, notebook, deep",
      (p["style"].default, p["context"].default, p["palette"].default), ("darkgrid", "notebook", "deep"))
check(14, "font sizes: paper 9.6, notebook 12, talk 18, poster 24",
      [round(sns.plotting_context(c)["font.size"], 1) for c in ("paper", "notebook", "talk", "poster")],
      [9.6, 12, 18, 24])
check(14, "the palettes exist", [len(sns.color_palette(n)) > 0 for n in ("deep", "colorblind", "viridis")], [True] * 3)
check(14, "the styles exist", [isinstance(sns.axes_style(s), dict) for s in ("darkgrid", "whitegrid", "ticks")], [True] * 3)
sns.set_theme(style="whitegrid", context="talk", palette="colorblind")
check(14, "set_theme changes matplotlib's settings", plt.rcParams["font.size"], 18.0)
fig, ax = plt.subplots()
check(14, "a plain matplotlib chart follows", ax.get_facecolor()[:3], (1.0, 1.0, 1.0))
plt.close("all")
matplotlib.rcdefaults()
matplotlib.use("Agg")


# ── slide 15 · Plotly Express ─────────────────────────────────────────────
fig = px.bar(totals.reset_index(), x="montant", y="categorie", orientation="h")
check(15, "type(fig)", repr(type(fig)), "<class 'plotly.graph_objs._figure.Figure'>")
check(15, "not a matplotlib object", isinstance(fig, matplotlib.artist.Artist), False)
check(15, "no set_title on a plotly Figure", hasattr(fig, "set_title"), False)
check(15, "a Figure holds traces and a layout", (len(fig.data), fig.data[0].type, fig.layout is not None), (1, "bar", True))
check(15, "px.bar infers horizontal bars from a numeric x and a text y",
      px.bar(totals.reset_index(), x="montant", y="categorie").data[0].orientation, "h")
check(15, "scatter colored by category: 7 traces",
      len(px.scatter(df, x="date", y="montant", color="categorie").data), 7)


# ── slide 16 · update_layout & update_traces ──────────────────────────────
r1 = fig.update_layout(title_text="Janvier", template="plotly_white")
r2 = fig.update_traces(marker_color="teal", hovertemplate="%{y} : %{x:.2f} €")
check(16, "each returns fig, so they chain", (r1 is fig, r2 is fig), (True, True))
check(16, "the layout holds the title", fig.layout.title.text, "Janvier")
check(16, "the traces hold the color and hover text",
      (fig.data[0].marker.color, fig.data[0].hovertemplate), ("teal", "%{y} : %{x:.2f} €"))
per_bar = ["#C47E44" if c == "Logement" else "#4A82C2" for c in totals.index]
fig.update_traces(marker_color=per_bar)
check(16, "marker_color also takes one colour per bar", list(fig.data[0].marker.color), per_bar)
check(16, "%{x:.2f} is the chapter 02 format spec", format(1670.03, ".2f"), "1670.03")
sc = px.scatter(df, x="date", y="montant", color="categorie")
sc.update_traces(marker_size=12, selector=dict(name="Logement"))
check(16, "selector updates only the matching traces",
      sorted(t.name for t in sc.data if t.marker.size == 12), ["Logement"])


# ── slide 17 · exporting HTML ─────────────────────────────────────────────
fig.write_html(TMP / "full.html")
fig.write_html(TMP / "cdn.html", include_plotlyjs="cdn")
full, cdn = (TMP / "full.html").stat().st_size, (TMP / "cdn.html").stat().st_size
check(17, "full file: ~4.8 MB", round(full / 1e6, 1), 4.8)
check(17, "cdn file: ~8 KB", round(cdn / 1e3), 8)
check(17, "cdn loads plotly.js 4.1.1", "https://cdn.plot.ly/plotly-4.1.1.min.js" in (TMP / "cdn.html").read_text(), True)
check(17, "the full file needs no connection", "cdn.plot.ly" in (TMP / "full.html").read_text()[:2000], False)
err = raises(lambda: fig.write_image(TMP / "x.png"))
check(17, "write_image fails without kaleido >= 1",
      ("RuntimeError" in err and "Kaleido package, v1.0.0 or greater" in err), True)


# ── slide 18 · pitfalls ───────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2)
plt.title("Janvier")
check(18, "plt.title after subplots: only the last Axes", [a.get_title() for a in axes], ["", "Janvier"])
plt.close("all")
fig, ax = plt.subplots()
ax.plot(daily.index, daily.values)
plt.close(fig)  # what closing the show() window does
plt.savefig(TMP / "blank.png")
check(18, "plt.savefig after the figure closed: a blank figure", plt.gcf().axes, [])
plt.close("all")
check(18, "the warning starts past 20 figures", plt.rcParams["figure.max_open_warning"], 20)
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    for _ in range(21):
        plt.figure()
msgs = [(w.category.__name__, str(w.message)[:42]) for w in caught]
check(18, "the 21st figure warns", msgs, [("RuntimeWarning", "More than 20 figures have been opened. Fig")])
plt.close("all")
fig, ax = plt.subplots()
n, _, _ = ax.hist(df["montant"], bins=20)
check(18, "246 expenses crushed into one bar", int(n[0]), 246)
ax.set_xscale("log")
check(18, "a log scale is one call", ax.get_xscale(), "log")
plt.close("all")


print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
