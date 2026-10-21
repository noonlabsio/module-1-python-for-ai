"""Chapter 14 — render every figure the deck shows, from the January expenses.

The code is typed live in VS Code, so the slides show the result instead: one
figure per content slide, written to figures/ beside this script. Every number
in a figure is computed here from ../00-premier-script/depenses_janvier.csv;
nothing is typed in by hand.

    uv run --no-project --python 3.12 --with pandas==3.0.6 \\
        --with matplotlib==3.11.2 --with seaborn==0.13.2 --with plotly==7.1.0 \\
        python 14-data-visualization/make-figures.py

Run it from the repo root. The plotly screenshots (slides 15-17) use the
repo's Playwright Chromium, so `npm install` must have run, and they load IBM
Plex from Google Fonts. Matplotlib uses IBM Plex Sans if it can find it: point
NL_FONT_DIR at a folder of IBMPlexSans-*.ttf files, or install the family.
Otherwise it falls back to DejaVu Sans, and the figures still render.

Colours follow the theme: the ink surface #061A2E, text in the theme's fg
tokens, and two marks validated on that surface (normal and colour-blind
vision): bronze #C47E44 for the one thing the slide is about, blue #4A82C2
for everything else. Colormap slides use viridis, because that is the lesson.
"""

import io
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from cycler import cycler
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Rectangle
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
CSV = ROOT / "00-premier-script" / "depenses_janvier.csv"

# ── theme tokens (themes/noonlabs/styles/layout.css) ──────────────────────
INK = "#061A2E"      # slide surface, --nl-ink-900
FG = "#F4F7FA"       # --fg
FG2 = "#A8BACF"      # --fg-2
FG3 = "#8195AD"      # --fg-3
LINE = "#1B4A77"     # --nl-line
HAIR = "#123456"     # one step off the surface: gridlines
ACCENT = "#C47E44"   # bronze, validated on INK
BASE = "#4A82C2"     # blue, validated on INK
MONO_FG = "#E8D3BE"  # --nl-c-fn, code-like labels

for d in filter(None, [os.environ.get("NL_FONT_DIR")]):
    for f in Path(d).glob("*.ttf"):
        font_manager.fontManager.addfont(str(f))
NAMES = {f.name for f in font_manager.fontManager.ttflist}
SANS = "IBM Plex Sans" if "IBM Plex Sans" in NAMES else "DejaVu Sans"
MONO = "JetBrains Mono" if "JetBrains Mono" in NAMES else "DejaVu Sans Mono"

DARK = {
    "figure.facecolor": "none", "axes.facecolor": "none", "savefig.transparent": True,
    "font.family": SANS, "font.size": 11,
    "text.color": FG2, "axes.labelcolor": FG2, "axes.labelsize": 11,
    "axes.titlecolor": FG, "axes.titlesize": 12, "axes.titleweight": "medium",
    "axes.titlelocation": "left", "axes.titlepad": 8,
    "axes.edgecolor": LINE, "axes.linewidth": 1,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": LINE, "ytick.color": LINE, "xtick.labelcolor": FG3, "ytick.labelcolor": FG3,
    "xtick.labelsize": 10, "ytick.labelsize": 10,
    "grid.color": HAIR, "grid.linewidth": 1,
    "lines.linewidth": 2, "lines.solid_capstyle": "round", "lines.solid_joinstyle": "round",
    "axes.prop_cycle": cycler(color=[BASE, ACCENT]),
    "legend.frameon": False, "svg.fonttype": "path",
}
plt.rcParams.update(DARK)

df = pd.read_csv(CSV)
df["date"] = pd.to_datetime(df["date"])
totals = df.groupby("categorie")["montant"].sum().sort_values()
daily = df.set_index("date")["montant"].resample("D").sum()
small = df.loc[df["montant"] < 100, "montant"]
rent = df.loc[df["montant"].idxmax()]
peak_day, peak = daily.idxmax(), daily.max()
df["semaine"] = df["date"].dt.isocalendar().week
pivot = pd.pivot_table(df, index="categorie", columns="semaine", values="montant", aggfunc="sum")
order = totals.index[::-1]          # biggest first, top to bottom


def euros(x):
    return f"€{x:,.0f}"


JAN = (pd.Timestamp("2025-12-31 12:00"), pd.Timestamp("2026-01-31 12:00"))


def days_axis(ax, label=True, days=(1, 8, 15, 22, 29)):
    ax.set_xlim(*JAN)
    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=list(days)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%-d"))
    if label:
        ax.set_xlabel("January 2026")


def bar_colors(index, hot="Logement"):
    return [ACCENT if c == hot else BASE for c in index]


def save(fig, name):
    """Write the figure, plus a preview on the slide surface for review."""
    path = OUT / name
    fig.savefig(path, dpi=200 if name.endswith(".png") else None)
    prev = Path(tempfile.gettempdir()) / "nl-ch14-preview"
    prev.mkdir(exist_ok=True)
    fig.savefig(prev / (Path(name).stem + ".png"), dpi=150, facecolor=INK, transparent=False)
    plt.close(fig)
    print(f"wrote {path.relative_to(ROOT)}")


# ── s03 · Figure, Axes & Artists ──────────────────────────────────────────
def anatomy():
    fig = plt.figure(figsize=(4.6, 3.45))
    ax = fig.add_axes((0.2, 0.16, 0.52, 0.56))
    ax.plot(daily.index, daily.values, color=BASE)
    ax.set_title("Janvier", loc="left")
    ax.set_ylabel("€ per day")
    days_axis(ax, label=False)
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    ax.grid(axis="y")
    # the Figure: the whole image
    fig.patches.append(FancyBboxPatch((0.012, 0.015), 0.976, 0.97, boxstyle="round,pad=0,rounding_size=0.025",
                                      transform=fig.transFigure, fill=False, ec=ACCENT, lw=1.5))
    fig.text(0.04, 0.915, "Figure", color=ACCENT, family=MONO, fontsize=11, weight="medium")
    # the Axes: one plot, with its ticks, labels and title
    fig.canvas.draw()
    bb = ax.get_tightbbox().transformed(fig.transFigure.inverted())
    fig.patches.append(Rectangle((bb.x0 - 0.02, bb.y0 - 0.02), bb.width + 0.04, bb.height + 0.04,
                                 transform=fig.transFigure, fill=False, ec=FG3, lw=1))
    fig.text(bb.x0 - 0.01, bb.y1 + 0.035, "Axes", color=FG, family=MONO, fontsize=11)
    # three Artists, labelled in the right margin
    kw = dict(xycoords="data", textcoords="figure fraction", color=MONO_FG, family=MONO, fontsize=10,
              va="center", arrowprops=dict(arrowstyle="-", color=FG3, lw=0.8, shrinkB=2))
    ax.annotate("Line2D", xy=(daily.index[20], daily.iloc[20]), xytext=(0.79, 0.52), **kw)
    ax.annotate("Text", xy=(0.17, 1.04), xycoords="axes fraction", xytext=(0.79, 0.76),
                textcoords="figure fraction", color=MONO_FG, family=MONO, fontsize=10, va="center",
                arrowprops=dict(arrowstyle="-", color=FG3, lw=0.8, shrinkB=2))
    ax.annotate("XAxis", xy=(1.0, -0.06), xycoords="axes fraction", xytext=(0.79, 0.17),
                textcoords="figure fraction", color=MONO_FG, family=MONO, fontsize=10, va="center",
                arrowprops=dict(arrowstyle="-", color=FG3, lw=0.8, shrinkB=2))
    fig.text(0.79, 0.34, "all Artists", color=FG3, fontsize=10, style="italic")
    save(fig, "s03-anatomy.svg")


# ── s04 · line & scatter ──────────────────────────────────────────────────
def line_scatter():
    fig, (top, bot) = plt.subplots(2, 1, figsize=(4.6, 3.45), sharex=True, layout="constrained")
    top.plot(daily.index, daily.values, color=BASE)
    top.plot([peak_day], [peak], "o", ms=7, color=ACCENT, mec=INK, mew=2)
    top.annotate(f"Jan 3: {peak:,.2f}", xy=(peak_day, peak), xytext=(10, -4), textcoords="offset points",
                 color=FG2, fontsize=10, va="center")
    top.set_title("plot · 31 daily totals, joined in order")
    top.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    top.grid(axis="y")
    top.set_ylim(0, 1700)
    bot.scatter(df["date"], df["montant"], s=14, color=BASE, alpha=0.8, linewidths=0)
    bot.scatter([rent["date"]], [rent["montant"]], s=30, color=ACCENT, ec=INK, linewidths=1.5, zorder=3)
    bot.set_yscale("log")
    bot.set_title("scatter · 247 expenses, one dot each")
    bot.set_ylabel("€ (log scale)", fontsize=9)
    bot.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    bot.grid(axis="y")
    days_axis(bot)
    save(fig, "s04-line-scatter.svg")


# ── s05 · bar & histogram ─────────────────────────────────────────────────
def bar_hist():
    fig = plt.figure(figsize=(4.6, 3.45), layout="constrained")
    gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1])
    bar = fig.add_subplot(gs[:, 0])
    bar.barh(totals.index, totals.values, height=0.6, color=bar_colors(totals.index))
    for y, v in enumerate(totals.values):
        bar.text(v + 40, y, f"{v:,.0f}", va="center", fontsize=9, color=FG2)
    bar.set_xlim(0, totals.max() * 1.3)
    bar.set_title("barh · totals")
    bar.spines["left"].set_visible(False)
    bar.tick_params(axis="y", length=0)
    bar.set_xticks([])
    bar.spines["bottom"].set_visible(False)

    h1 = fig.add_subplot(gs[0, 1])
    n, bins, patches = h1.hist(df["montant"], bins=20, color=BASE, rwidth=0.85)
    patches[-1].set_facecolor(ACCENT)
    h1.text(bins[1] + 30, n[0] * 0.8, f"{int(n[0])}", color=FG2, fontsize=9)
    mid = (bins[-2] + bins[-1]) / 2
    h1.plot([mid], [n[-1] + 8], "o", ms=6, color=ACCENT, mec=INK, mew=1.5, clip_on=False)
    h1.text(mid, n[-1] + 40, f"{int(n[-1])} · rent", fontsize=9, color=FG2, ha="right")
    h1.set_title("hist · all 247")
    h1.set_yticks([])
    h1.spines["left"].set_visible(False)
    h1.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")

    h2 = fig.add_subplot(gs[1, 1])
    h2.hist(small, bins=20, color=BASE, rwidth=0.85)
    h2.set_title("hist · below €100")
    h2.set_yticks([])
    h2.spines["left"].set_visible(False)
    save(fig, "s05-bar-hist.svg")


# ── s06 · pie & boxplot ───────────────────────────────────────────────────
def pie_box():
    fig = plt.figure(figsize=(4.6, 3.45))
    pie = fig.add_axes((0.06, 0.16, 0.44, 0.62))
    shares = totals[::-1]
    labels = [c if c in ("Sante", "Loisirs") else "" for c in shares.index]
    pie.pie(shares, labels=labels, colors=bar_colors(shares.index), startangle=90, counterclock=False,
            labeldistance=1.1, wedgeprops=dict(edgecolor=INK, linewidth=2),
            textprops=dict(fontsize=9, color=FG2))
    pie.text(0.5, 0.3, f"Logement\n{shares['Logement'] / shares.sum():.1%}", ha="center", va="center",
             color=FG, fontsize=9.5, weight="medium", linespacing=1.3)
    pie.set_title("pie · Sante or Loisirs?", loc="center", y=1.08)

    box = fig.add_axes((0.66, 0.15, 0.32, 0.68))
    groups = [df.loc[df["categorie"] == c, "montant"] for c in order[::-1]]
    r = box.boxplot(groups, tick_labels=order[::-1], orientation="horizontal", widths=0.55, patch_artist=True,
                    boxprops=dict(facecolor="none", edgecolor=BASE, linewidth=1.3),
                    medianprops=dict(color=FG, linewidth=1.5),
                    whiskerprops=dict(color=BASE, linewidth=1.2), capprops=dict(color=BASE, linewidth=1.2),
                    flierprops=dict(marker="o", markerfacecolor=ACCENT, markeredgecolor=INK, markersize=7))
    box.set_xscale("log")
    box.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    box.set_xlabel("€ (log scale)", fontsize=9)
    box.tick_params(axis="y", length=0, labelsize=8.5)
    box.spines["left"].set_visible(False)
    box.set_title("boxplot · spread", loc="right", y=1.03)
    fl = r["fliers"][-1]
    box.annotate("rent", xy=(fl.get_xdata()[0], len(groups)), xytext=(0, -16), textcoords="offset points",
                 ha="center", fontsize=9, color=FG2)
    save(fig, "s06-pie-box.svg")


# ── s07 · subplots ────────────────────────────────────────────────────────
def subplots():
    fig, axes = plt.subplots(2, 2, figsize=(4.6, 3.45), layout="constrained")
    for (r, c), ax in np.ndenumerate(axes):
        ax.set_title(f"axes[{r}, {c}]", family=MONO, color=MONO_FG, fontsize=10, weight="normal")
        ax.tick_params(labelsize=8)
    axes[0, 0].plot(daily.index, daily.values, color=BASE, lw=1.6)
    days_axis(axes[0, 0], label=False, days=(1, 15, 29))
    axes[0, 0].yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    axes[0, 1].barh(totals.index, totals.values, height=0.6, color=bar_colors(totals.index))
    axes[0, 1].tick_params(axis="y", labelsize=7, length=0)
    axes[0, 1].set_xticks([])
    axes[0, 1].spines[["left", "bottom"]].set_visible(False)
    axes[1, 0].hist(small, bins=20, color=BASE, rwidth=0.85)
    axes[1, 0].set_yticks([])
    axes[1, 0].spines["left"].set_visible(False)
    axes[1, 1].scatter(df["date"], df["montant"], s=6, color=BASE, linewidths=0)
    axes[1, 1].set_yscale("log")
    days_axis(axes[1, 1], label=False, days=(1, 15, 29))
    axes[1, 1].yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    save(fig, "s07-subplots.svg")


# ── s08 · GridSpec ────────────────────────────────────────────────────────
def gridspec():
    fig = plt.figure(figsize=(4.6, 3.45))
    gs = fig.add_gridspec(2, 3, left=0.04, right=0.96, bottom=0.05, top=0.95, wspace=0.08, hspace=0.12)
    for r in range(2):
        for c in range(3):
            b = gs[r, c].get_position(fig)
            fig.patches.append(Rectangle((b.x0, b.y0), b.width, b.height, transform=fig.transFigure,
                                         fill=False, ec=LINE, lw=1))
    specs = {"gs[0, :]": gs[0, :], "gs[1, :2]": gs[1, :2], "gs[1, 2]": gs[1, 2]}
    axs = {}
    for key, spec in specs.items():
        b = spec.get_position(fig)
        pad_l, pad_r, pad_top, pad_bot = 0.1, 0.03, 0.1, 0.08
        ax = fig.add_axes((b.x0 + pad_l, b.y0 + pad_bot, b.width - pad_l - pad_r, b.height - pad_top - pad_bot))
        ax.set_title(key, family=MONO, color=MONO_FG, fontsize=10, weight="normal")
        ax.tick_params(labelsize=8)
        axs[key] = ax
    a = axs["gs[0, :]"]
    a.plot(daily.index, daily.values, color=BASE)
    a.plot([peak_day], [peak], "o", ms=6, color=ACCENT, mec=INK, mew=1.5)
    days_axis(a, label=False)
    a.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    b = axs["gs[1, :2]"]
    b.hist(small, bins=20, color=BASE, rwidth=0.85)
    b.set_yticks([])
    b.spines["left"].set_visible(False)
    c = axs["gs[1, 2]"]
    c.pie(totals[::-1], colors=bar_colors(totals.index[::-1]), startangle=90, counterclock=False,
          wedgeprops=dict(edgecolor=INK, linewidth=1.5))
    save(fig, "s08-gridspec.svg")


# ── s09 · colors & colormaps ──────────────────────────────────────────────
def lightness(rgb):
    """CIE L* of sRGB colours in [0, 1], 0 (black) to 100 (white)."""
    rgb = np.asarray(rgb)[..., :3]
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    y = lin @ np.array([0.2126, 0.7152, 0.0722])
    return np.where(y > 216 / 24389, 116 * np.cbrt(y) - 16, y * 24389 / 27)


def colormaps():
    fig = plt.figure(figsize=(4.6, 3.45))
    sw = fig.add_axes((0.04, 0.78, 0.92, 0.1))
    cyc = plt.rcParamsDefault["axes.prop_cycle"].by_key()["color"]
    for i, col in enumerate(cyc):
        sw.add_patch(FancyBboxPatch((i + 0.08, 0.1), 0.84, 0.8, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=col, ec="none"))
        sw.text(i + 0.5, -0.45, f"C{i}", ha="center", va="center", family=MONO, fontsize=8.5, color=FG3)
    sw.set_xlim(0, 10)
    sw.set_ylim(-0.8, 1)
    sw.axis("off")
    fig.text(0.04, 0.925, "Categories · the default cycle, C0 to C9", color=FG, fontsize=11, weight="medium")

    fig.text(0.04, 0.615, "Quantities · a colormap, and its lightness", color=FG, fontsize=11, weight="medium")
    x = np.linspace(0, 1, 256)
    for row, (name, verdict, col) in enumerate([("viridis", "even steps", "#7FA694"),
                                                 ("jet", "bright bands", "#D2837A")]):
        y0 = 0.33 - row * 0.29
        strip = fig.add_axes((0.04, y0, 0.66, 0.2))
        strip.imshow(x[None, :], aspect="auto", cmap=name, extent=(0, 1, 0, 100))
        strip.plot(x, lightness(plt.colormaps[name](x)), color="white", lw=1.6)
        strip.set_ylim(0, 100)
        strip.set_xticks([])
        strip.set_yticks([])
        for s in strip.spines.values():
            s.set_visible(False)
        fig.text(0.74, y0 + 0.13, name, family=MONO, color=MONO_FG, fontsize=11, va="center")
        fig.text(0.74, y0 + 0.05, verdict, color=col, fontsize=10, va="center")
    fig.text(0.04, 0.005, "white line = perceived lightness, 0 to 100", color=FG3, fontsize=8.5)
    save(fig, "s09-colormaps.svg")


# ── s10 · annotations & text ──────────────────────────────────────────────
def annotations():
    fig, (top, bot) = plt.subplots(2, 1, figsize=(4.6, 3.45), layout="constrained",
                                   gridspec_kw=dict(height_ratios=[1.1, 1]))
    top.plot(daily.index, daily.values, color=BASE)
    top.plot([peak_day], [peak], "o", ms=7, color=ACCENT, mec=INK, mew=2)
    top.annotate(f"Loyer : {rent['montant']:.0f} €", xy=(peak_day, peak),
                 xytext=(pd.Timestamp("2026-01-10"), 1200), color=FG, fontsize=10.5,
                 arrowprops=dict(arrowstyle="->", color=FG2, lw=1.1, shrinkA=3, shrinkB=6))
    top.set_title("annotate · the point, the text, an arrow")
    top.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    top.set_ylim(0, 1650)
    top.grid(axis="y")
    days_axis(top, label=False)
    bars = bot.barh(totals.index, totals.values, height=0.62, color=bar_colors(totals.index))
    bot.bar_label(bars, fmt="%.0f", padding=4, fontsize=9, color=FG2)
    bot.set_xlim(0, totals.max() * 1.15)
    bot.set_xticks([])
    bot.spines[["left", "bottom"]].set_visible(False)
    bot.tick_params(axis="y", length=0, labelsize=9)
    bot.set_title("bar_label · each value at the tip")
    save(fig, "s10-annotations.svg")


# ── s11 · 3D ──────────────────────────────────────────────────────────────
def surface():
    x = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, x)
    Z = np.sin(np.hypot(X, Y))
    fig = plt.figure(figsize=(4.6, 3.45))
    ax = fig.add_axes((-0.02, -0.02, 1.0, 1.0), projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", rstride=1, cstride=1, linewidth=0, antialiased=True)
    ax.set_box_aspect((1, 1, 0.55))
    ax.view_init(elev=28, azim=-55)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((0, 0, 0, 0))
        axis.line.set_color(LINE)
        axis._axinfo["grid"]["color"] = HAIR
        axis._axinfo["tick"]["color"] = LINE
    ax.tick_params(labelsize=8, colors=FG3)
    ax.set_xticks([-3, 0, 3])
    ax.set_yticks([-3, 0, 3])
    ax.set_zticks([-1, 0, 1])
    fig.text(0.05, 0.92, "z = sin(√(x² + y²)) · 50 × 50 grid", color=FG2, fontsize=10, family=SANS)
    save(fig, "s11-surface.png")


# ── s12 · saving: the same corner, zoomed, three ways ─────────────────────
def render_crop(dpi):
    """The rent annotation of the s10 chart, rendered at `dpi`, cropped around its text."""
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot(daily.index, daily.values, color=BASE)
    ax.plot([peak_day], [peak], "o", ms=6, color=ACCENT, mec=INK, mew=1.5)
    note = ax.annotate(f"Loyer : {rent['montant']:.0f} €", xy=(peak_day, peak),
                       xytext=(pd.Timestamp("2026-01-10"), 1200), color=FG, fontsize=10,
                       arrowprops=dict(arrowstyle="->", color=FG2, lw=1, shrinkA=3, shrinkB=6))
    days_axis(ax)
    fig.canvas.draw()
    # the Text's own extent: an Annotation's window extent also covers its arrow
    t = matplotlib.text.Text.get_window_extent(note).transformed(fig.transFigure.inverted())
    box = (t.x0 - 0.01, t.y0 - 0.02, t.x0 + 0.075, t.y1 + 0.02)
    buf = io.BytesIO()
    fig.savefig(buf, dpi=dpi, facecolor=INK, transparent=False, format="png")
    plt.close(fig)
    img = Image.open(buf)
    w, h = img.size
    x0, y0, x1, y1 = box
    return img.crop((int(x0 * w), int((1 - y1) * h), int(x1 * w), int((1 - y0) * h)))


def dpi_zoom():
    crops = [("PNG · 100 dpi", render_crop(100)),
             ("PNG · 300 dpi", render_crop(300)),
             ("SVG · vector", render_crop(1200))]
    size = crops[-1][1].size
    fig, axes = plt.subplots(1, 3, figsize=(4.6, 2.2), layout="constrained")
    for ax, (label, img) in zip(axes, crops):
        ax.imshow(np.asarray(img.resize(size, Image.NEAREST)))
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(True)
            s.set_color(LINE)
        ax.set_title(label, fontsize=10, loc="center")
    fig.text(0.5, 0.0, "the same corner, zoomed in", ha="center", va="bottom", color=FG3, fontsize=9)
    fig.get_layout_engine().set(h_pad=0.12)
    save(fig, "s12-dpi.png")


# ── s13 · seaborn's four families ─────────────────────────────────────────
def seaborn_families():
    fig, axes = plt.subplots(2, 2, figsize=(4.6, 3.45), layout="constrained")
    (a, b), (c, d) = axes
    sns.scatterplot(data=df, x="date", y="montant", s=12, color=BASE, linewidth=0, ax=a)
    a.set_yscale("log")
    days_axis(a, label=False, days=(1, 15, 29))
    a.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    a.set_title("relational")
    sns.histplot(small, bins=20, kde=True, color=BASE, edgecolor=INK, linewidth=0.6, ax=b,
                 line_kws=dict(color=ACCENT, lw=2))
    b.set_yticks([])
    b.spines["left"].set_visible(False)
    b.set_title("distribution")
    sns.boxplot(data=df, x="montant", y="categorie", order=order, log_scale=True, ax=c, width=0.6,
                color=BASE, fill=False, linewidth=1.1, fliersize=3,
                flierprops=dict(markerfacecolor=ACCENT, markeredgecolor=ACCENT))
    c.tick_params(axis="y", labelsize=7, length=0)
    c.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    c.set_title("categorical")
    sns.heatmap(pivot.loc[order], cmap="viridis", ax=d, cbar=False, linewidths=1.5, linecolor=INK,
                yticklabels=False)
    d.set_xlabel("ISO week")
    d.set_title("matrix")
    for ax in axes.flat:
        ax.set_ylabel("")
        ax.tick_params(labelsize=8)
        if ax is not d:
            ax.set_xlabel("")
    save(fig, "s13-seaborn.svg")


# ── s14 · seaborn contexts, in seaborn's own light style ──────────────────
def seaborn_contexts():
    panels = []
    with plt.rc_context():
        for ctx in ("paper", "notebook", "talk", "poster"):
            plt.rcdefaults()
            sns.set_theme(style="whitegrid", context=ctx, palette="colorblind", font=SANS)
            fig, ax = plt.subplots(figsize=(4.2, 2.6), layout="constrained")
            top3 = totals[::-1].head(3)
            sns.barplot(x=top3.values, y=top3.index, ax=ax, color=sns.color_palette()[0])
            ax.set_title(ctx, loc="left")
            ax.set_xlabel("€")
            ax.set_ylabel("")
            buf = io.BytesIO()
            fig.savefig(buf, dpi=200, format="png", transparent=False)
            plt.close(fig)
            panels.append(Image.open(buf).convert("RGBA"))
        sns.reset_orig()
    plt.rcParams.update(DARK)
    w, h = panels[0].size
    gap = 36
    sheet = Image.new("RGBA", (2 * w + gap, 2 * h + gap), (0, 0, 0, 0))
    for i, p in enumerate(panels):
        sheet.paste(p, ((i % 2) * (w + gap), (i // 2) * (h + gap)))
    sheet.save(OUT / "s14-contexts.png")
    prev = Path(tempfile.gettempdir()) / "nl-ch14-preview"
    bg = Image.new("RGBA", sheet.size, INK)
    bg.alpha_composite(sheet)
    bg.convert("RGB").save(prev / "s14-contexts.png")
    print("wrote", (OUT / "s14-contexts.png").relative_to(ROOT))


# ── s15-s17 · plotly, screenshot in the repo's Chromium ───────────────────
SHOOT = r"""
import { chromium } from 'playwright-chromium'
const [html, out, hover, w, h] = process.argv.slice(1)
const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 3 })
await page.goto('file://' + html)
await page.waitForSelector('.main-svg')
await page.evaluate(() => document.fonts.ready)
await page.waitForTimeout(400)
if (hover !== 'none') {
  const bars = await page.$$('g.point path')
  const box = await bars[+hover].boundingBox()
  await page.mouse.move(box.x + box.width * 0.7, box.y + box.height / 2)
  await page.waitForTimeout(500)
}
await page.screenshot({ path: out })
await browser.close()
"""

FONT_LINK = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             'family=IBM+Plex+Sans:wght@400;500&display=swap">')


def shoot(fig, name, hover_bar, w=440, h=330, frame=None):
    """Write the plotly figure to HTML, hover one bar, and screenshot it."""
    tmp = Path(tempfile.mkdtemp(prefix="nl-ch14-plotly-"))
    page = tmp / "chart.html"
    fig.write_html(page, include_plotlyjs=True, full_html=True,
                   config=dict(displayModeBar=frame is not None))
    html = page.read_text().replace("<head>", "<head>" + FONT_LINK, 1)
    html = html.replace("<body>", '<body style="margin:0">', 1)
    if frame:
        html = html.replace('<body style="margin:0">', '<body style="margin:0">' + frame, 1)
    page.write_text(html)
    out = OUT / name
    subprocess.run(["node", "--input-type=module", "-e", SHOOT, str(page), str(out), str(hover_bar), str(w), str(h)],
                   cwd=ROOT, check=True)
    print("wrote", out.relative_to(ROOT))


def plotly_figures():
    data = totals.reset_index()
    hot = data["categorie"].tolist().index("Logement")
    font = dict(family="IBM Plex Sans, sans-serif", size=13)

    base = px.bar(data, x="montant", y="categorie", orientation="h")
    base.update_layout(width=440, height=330, margin=dict(l=10, r=16, t=16, b=10), font=font)
    shoot(base, "s15-plotly-express.png", hover_bar=hot)

    custom = px.bar(data, x="montant", y="categorie", orientation="h")
    custom.update_layout(title_text="Janvier", template="plotly_white", width=440, height=330,
                         margin=dict(l=10, r=16, t=44, b=10), font=font,
                         xaxis_title="€", yaxis_title=None)
    custom.update_traces(marker_color=bar_colors(data["categorie"]),
                         hovertemplate="%{y} : %{x:.2f} €<extra></extra>")
    shoot(custom, "s16-plotly-custom.png", hover_bar=hot)

    bar = ('<div style="font:13px IBM Plex Sans,sans-serif;background:#E9EDF2;color:#40505F;'
           'padding:8px 12px;border-bottom:1px solid #D4DAE1;display:flex;gap:10px;align-items:center">'
           '<span style="display:flex;gap:6px"><i style="width:11px;height:11px;border-radius:50%;'
           'background:#D2837A;display:block"></i><i style="width:11px;height:11px;border-radius:50%;'
           'background:#E2C27A;display:block"></i><i style="width:11px;height:11px;border-radius:50%;'
           'background:#7FA694;display:block"></i></span>'
           '<span style="background:#fff;border-radius:6px;padding:3px 10px;flex:1">depenses.html</span></div>')
    custom.update_layout(height=294, margin=dict(l=10, r=16, t=52, b=10))
    shoot(custom, "s17-export-html.png", hover_bar=hot, frame=bar)


# ── s18 · pitfall: one outlier, one axis ──────────────────────────────────
def pitfall():
    fig, (a, b) = plt.subplots(2, 1, figsize=(4.6, 3.45), layout="constrained")
    n, bins, patches = a.hist(df["montant"], bins=20, color=BASE, rwidth=0.85)
    patches[-1].set_facecolor(ACCENT)
    mid = (bins[-2] + bins[-1]) / 2
    a.plot([mid], [12], "o", ms=6, color=ACCENT, mec=INK, mew=1.5)
    a.text(mid, 40, "rent", ha="center", fontsize=9, color=FG2)
    a.set_title("Before · 246 expenses crushed into one bar", color="#D2837A")
    a.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    a.set_yticks([0, 100, 200])
    a.grid(axis="y")
    edges = np.logspace(np.log10(df["montant"].min()), np.log10(df["montant"].max() * 1.01), 25)
    n2, _, p2 = b.hist(df["montant"], bins=edges, color=BASE, rwidth=0.85)
    p2[-1].set_facecolor(ACCENT)
    b.set_xscale("log")
    b.plot([rent["montant"]], [4], "o", ms=6, color=ACCENT, mec=INK, mew=1.5)
    b.text(rent["montant"], 10, "rent", ha="center", fontsize=9, color=FG2)
    b.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
    b.set_title("After · a log scale shows the shape, and the rent", color="#7FA694")
    b.set_xlabel("€ (log scale)")
    b.set_yticks([0, 20, 40])
    b.grid(axis="y")
    save(fig, "s18-pitfall.svg")


if __name__ == "__main__":
    print(f"fonts: {SANS} / {MONO}")
    anatomy()
    line_scatter()
    bar_hist()
    pie_box()
    subplots()
    gridspec()
    colormaps()
    annotations()
    surface()
    dpi_zoom()
    seaborn_families()
    seaborn_contexts()
    plotly_figures()
    pitfall()
