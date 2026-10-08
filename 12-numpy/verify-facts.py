"""Chapter 12 — re-run every fact that appears on a slide or in a note.

The one chapter whose facts are not stdlib behaviour: this script imports
NumPy, by approved exception to the skill's stdlib-only rule. Pin the version
when you run it, without touching the repo:

    uv run --no-project --with numpy==2.5.3 python 12-numpy/verify-facts.py

Verified with NumPy 2.5.3 (current, September 2026) on CPython 3.12.3 and
3.14.2, and with NumPy 2.3.5 on CPython 3.12.3. Facts that changed in NumPy 2.5 — eigvals returning complex numbers,
sort(descending=True), the deprecation of assigning to .shape — are checked
against whichever version is running. Every printed scalar assumes NumPy 2.x
(np.int64(6), not 6); the script refuses to run on 1.x.

Slide 03 times real work and asserts the direction, printing the numbers for
the note. Slide 19 reads ../00-premier-script/depenses_janvier.csv.

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 21-slide deck: 01 cover, 02 divider, 03-20
content, 21 closing card.
"""

import statistics
import sys
import tempfile
import time
import warnings
from pathlib import Path

import numpy as np

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


NP = tuple(int(p) for p in np.__version__.split(".")[:2])
if NP < (2, 0):
    sys.exit(f"NumPy {np.__version__}: this deck assumes NumPy 2.x")
print(f"CPython {sys.version}")
print(f"NumPy {np.__version__}\n")
TMP = Path(tempfile.mkdtemp(prefix="nl-ch12-"))
CSV = Path(__file__).resolve().parent.parent / "00-premier-script" / "depenses_janvier.csv"


# ── slide 3 · vectorization ───────────────────────────────────────────────
data = [i * 0.5 for i in range(1_000_000)]
arr = np.array(data)
t = time.perf_counter()
s_loop = sum(x * x for x in data)
loop = time.perf_counter() - t
t = time.perf_counter()
s_np = (arr * arr).sum()
vec = time.perf_counter() - t
info(3, f"Python loop {loop * 1000:.1f} ms, NumPy {vec * 1000:.2f} ms ({loop / vec:.0f}x)")
check(3, "the two sums agree", bool(np.isclose(s_loop, s_np)), True)
check(3, "NumPy is several times faster (over 3x)", loop / vec > 3, True)
check(3, "an array holds one type, side by side", (arr.dtype, arr.flags["C_CONTIGUOUS"]), (np.dtype("float64"), True))


# ── slide 4 · creating arrays ─────────────────────────────────────────────
check(4, "zeros((2, 3))", (np.zeros((2, 3)).shape, float(np.zeros((2, 3)).sum())), ((2, 3), 0.0))
check(4, "ones(3)", np.ones(3).tolist(), [1.0, 1.0, 1.0])
check(4, "eye(2) is the identity", np.eye(2).tolist(), [[1.0, 0.0], [0.0, 1.0]])
check(4, "arange(0, 10, 2)", np.arange(0, 10, 2).tolist(), [0, 2, 4, 6, 8])
check(4, "linspace(0, 1, 5): 5 points, end included", np.linspace(0, 1, 5).tolist(), [0.0, 0.25, 0.5, 0.75, 1.0])
check(4, "arange(1, 1.3, 0.1) includes 1.3", repr(np.arange(1, 1.3, 0.1)), "array([1. , 1.1, 1.2, 1.3])")
check(4, "arange stops before the end, like range", np.arange(5).tolist(), list(range(5)))


# ── slide 5 · attributes ──────────────────────────────────────────────────
a = np.zeros((3, 4))
check(5, "shape, ndim, dtype", repr((a.shape, a.ndim, a.dtype)), "((3, 4), 2, dtype('float64'))")
check(5, "itemsize, nbytes", (a.itemsize, a.nbytes), (8, 96))
check(5, "nbytes is itemsize times the element count", a.nbytes, a.itemsize * a.size)
check(5, "a scalar prints with its type (2.0+)", repr(np.arange(4).sum()), "np.int64(6)")


# ── slide 6 · data types & astype ─────────────────────────────────────────
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    wrapped = np.array([200], dtype=np.uint8) + 100
check(6, "uint8 200 + 100 wraps to 44", repr(wrapped), "array([44], dtype=uint8)")
check(6, "... with no warning", len(caught), 0)
check(6, "int64 2**62 * 4 wraps to 0", repr(np.array([2**62]) * 4), "array([0])")
check(6, "Python's int does not overflow", 2**62 * 4, 18446744073709551616)
check(6, "astype(int) truncates toward zero", np.array([1.7, -1.7]).astype(int).tolist(), [1, -1])
check(6, "astype(float) parses strings", np.array(["1.5", "2"]).astype(float).tolist(), [1.5, 2.0])
check(6, "NEP 50: a Python scalar keeps the array's type (2.0+)", (np.float32(3) + 3.0).dtype, np.dtype("float32"))


# ── slide 7 · reshape, flatten, transpose ─────────────────────────────────
m = np.arange(6).reshape(2, 3)
check(7, "reshape(3, -1)", m.reshape(3, -1).shape, (3, 2))
check(7, ".T swaps the axes", m.T.shape, (3, 2))
check(7, "np.newaxis adds an axis of size 1", np.arange(3)[:, np.newaxis].shape, (3, 1))
check(7, "reshape never changes the numbers", m.reshape(3, 2).ravel().tolist(), list(range(6)))
check(7, "ravel is a view, flatten a copy",
      (np.shares_memory(m, m.ravel()), np.shares_memory(m, m.flatten())), (True, False))
s = np.arange(6)
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    s.shape = (2, 3)
check(7, "assigning to .shape is deprecated (2.5+)",
      any(issubclass(w.category, DeprecationWarning) for w in caught), NP >= (2, 5))


# ── slide 8 · indexing & slicing (the PLANT) ──────────────────────────────
check(8, "m[1, 2], m[:, 1]", repr((m[1, 2], m[:, 1])), "(np.int64(5), array([1, 4]))")
check(8, "fancy indexing picks positions", repr(np.arange(10)[[1, 3, 5]]), "array([1, 3, 5])")
a = np.arange(6)
s = a[2:4]
s[0] = 99
check(8, "editing the slice changed a", repr(a), "array([ 0,  1, 99,  3,  4,  5])")


# ── slide 9 · boolean masks & np.where ────────────────────────────────────
v = np.array([1, 5, 3, 8, 2])
check(9, "v[v > 2]", repr(v[v > 2]), "array([5, 3, 8])")
check(9, "v[(v > 2) & (v < 6)]", repr(v[(v > 2) & (v < 6)]), "array([5, 3])")
check(9, "np.where(v > 2, v, 0)", repr(np.where(v > 2, v, 0)), "array([0, 5, 3, 8, 0])")
check(9, "v > 2 is an array of booleans", (v > 2).tolist(), [False, True, True, True, False])
AMBIGUOUS = ("ValueError: The truth value of an array with more than one element is ambiguous. "
             "Use a.any() or a.all()")
check(9, "without parentheses it raises", raises(lambda: v > 2 & v < 6), AMBIGUOUS)
check(9, "'and' raises the same", raises(lambda: v > 2 and v < 6), AMBIGUOUS)


# ── slide 10 · views vs copies (the PAYOFF) ───────────────────────────────
a = np.arange(6)
check(10, "a slice shares memory", np.shares_memory(a, a[2:4]), True)
check(10, "fancy indexing does not", np.shares_memory(a, a[[2, 3]]), False)
check(10, "a boolean mask copies", np.shares_memory(a, a[a > 2]), False)
check(10, "reshape and .T are views here", (np.shares_memory(a, a.reshape(2, 3)), np.shares_memory(m, m.T)), (True, True))
safe = a[2:4].copy()
safe[0] = -5
check(10, ".copy() is independent", (np.shares_memory(a, safe), int(a[2])), (False, 2))
lst = list(range(6))
part = lst[2:4]
part[0] = 99
check(10, "chapter 05: a list slice copies", lst[2], 2)


# ── slide 11 · element-wise operations & ufuncs ───────────────────────────
a = np.array([1, 4, 9])
check(11, "a + 1, a * a", repr((a + 1, a * a)), "(array([ 2,  5, 10]), array([ 1, 16, 81]))")
check(11, "np.sqrt(a)", repr(np.sqrt(a)), "array([1., 2., 3.])")
check(11, "sqrt, exp, log are ufuncs", all(isinstance(f, np.ufunc) for f in (np.sqrt, np.exp, np.log)), True)
doc = " ".join(np.vectorize.__doc__.split())
check(11, "vectorize's docs: 'essentially a for loop'",
      "provided primarily for convenience, not for performance. The implementation is essentially a for loop." in doc,
      True)
vf = np.vectorize(lambda x: x * 2)
big = np.arange(200_000)
t = time.perf_counter()
vf(big)
slow = time.perf_counter() - t
t = time.perf_counter()
big * 2
fast = time.perf_counter() - t
info(11, f"np.vectorize {slow * 1000:.1f} ms, big * 2 {fast * 1000:.2f} ms")
check(11, "np.vectorize is much slower than the array expression", slow / fast > 3, True)


# ── slide 12 · broadcasting ───────────────────────────────────────────────
col = np.arange(3).reshape(3, 1)
row = np.arange(4)
check(12, "col + row is (3, 4)", (col + row).tolist(), [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
check(12, "(3,) + (4,) fails",
      raises(lambda: np.arange(3) + np.arange(4)).rstrip(),
      "ValueError: operands could not be broadcast together with shapes (3,) (4,)")
check(12, "a scalar reaches every element", (np.array([1, 2, 3]) + 10).tolist(), [11, 12, 13])


# ── slide 13 · aggregation along axes ─────────────────────────────────────
g = np.array([[1, 2, 3], [4, 5, 6]])
check(13, "g.sum()", repr(g.sum()), "np.int64(21)")
check(13, "g.sum(axis=0)", repr(g.sum(axis=0)), "array([5, 7, 9])")
check(13, "g.sum(axis=1)", repr(g.sum(axis=1)), "array([ 6, 15])")
check(13, "g.argmax(), g.argmin(axis=1)", repr((g.argmax(), g.argmin(axis=1))), "(np.int64(5), array([0, 0]))")
check(13, "keepdims keeps a size-1 axis", g.mean(axis=1, keepdims=True).shape, (2, 1))
check(13, "centering rows with keepdims and broadcasting",
      (g - g.mean(axis=1, keepdims=True)).tolist(), [[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]])


# ── slide 14 · NaN ────────────────────────────────────────────────────────
n = np.array([1.0, np.nan, 3.0])
check(14, "n.mean() is nan", repr(n.mean()), "np.float64(nan)")
check(14, "np.nanmean(n)", repr(np.nanmean(n)), "np.float64(2.0)")
check(14, "nan == nan is False", np.nan == np.nan, False)
check(14, "== np.nan finds nothing; isnan does", ((n == np.nan).any(), np.isnan(n).tolist()),
      (np.False_, [False, True, False]))
check(14, "nansum and nanmax skip it", (float(np.nansum(n)), float(np.nanmax(n))), (4.0, 3.0))
check(14, "np.NaN was removed in 2.0", raises(lambda: np.NaN).split(":")[0], "AttributeError")
check(14, "np.isclose for floats (chapter 02)", bool(np.isclose(0.1 + 0.2, 0.3)), True)


# ── slide 15 · combining, sorting & unique ────────────────────────────────
check(15, "concatenate([[1, 2], [3]])", repr(np.concatenate([[1, 2], [3]])), "array([1, 2, 3])")
check(15, "stack makes a new axis", np.stack([[1, 2], [3, 4]]).shape, (2, 2))
check(15, "argsort([3, 1, 2])", repr(np.argsort([3, 1, 2])), "array([1, 2, 0])")
names = np.array(["c", "a", "b"])
amounts = np.array([3, 1, 2])
check(15, "argsort keeps another array aligned", names[np.argsort(amounts)].tolist(), ["a", "b", "c"])
vals, counts = np.unique(["Resto", "Courses", "Resto"], return_counts=True)
check(15, "unique with counts: Courses 1, Resto 2", (vals.tolist(), counts.tolist()), (["Courses", "Resto"], [1, 2]))
if NP >= (2, 5):
    check(15, "sort(descending=True) exists (2.5+)", np.sort(np.array([3, 1, 2]), descending=True).tolist(), [3, 2, 1])


# ── slide 16 · random with default_rng ────────────────────────────────────
rng = np.random.default_rng(42)
check(16, "default_rng(42).integers(1, 7, size=5)", repr(rng.integers(1, 7, size=5)), "array([1, 5, 4, 3, 3])")
check(16, "normal(size=3).shape", rng.normal(0, 1, size=3).shape, (3,))
check(16, "same seed, same numbers",
      np.random.default_rng(42).integers(1, 7, size=5).tolist(), [1, 5, 4, 3, 3])
rolls = np.random.default_rng(0).integers(1, 7, size=10_000)
check(16, "integers(1, 7) excludes 7: a six-sided die", (int(rolls.min()), int(rolls.max())), (1, 6))
check(16, "default_rng returns a Generator", isinstance(rng, np.random.Generator), True)
check(16, "np.random.seed still exists, as the legacy API", callable(np.random.seed), True)


# ── slide 17 · statistics ─────────────────────────────────────────────────
check(17, "median", repr(np.median([13.16, 5.5, 23.62])), "np.float64(13.16)")
check(17, "percentile 50", repr(np.percentile([1, 2, 3, 4], 50)), "np.float64(2.5)")
check(17, "np.std divides by n", repr(np.std([1, 2, 3, 4])), "np.float64(1.118033988749895)")
check(17, "statistics.stdev divides by n - 1", statistics.stdev([1, 2, 3, 4]), 1.2909944487358056)
check(17, "ddof=1 matches statistics.stdev", float(np.std([1, 2, 3, 4], ddof=1)), statistics.stdev([1, 2, 3, 4]))
check(17, "the same median as chapter 09", float(np.median([13.16, 5.5, 23.62])),
      statistics.median([13.16, 5.5, 23.62]))
check(17, "corrcoef: 1 together, -1 opposite",
      (round(float(np.corrcoef([1, 2, 3], [2, 4, 6])[0, 1]), 12), round(float(np.corrcoef([1, 2, 3], [3, 2, 1])[0, 1]), 12)),
      (1.0, -1.0))


# ── slide 18 · linear algebra ─────────────────────────────────────────────
A = np.array([[2., 1.], [1., 3.]])
b = np.array([3., 5.])
check(18, "solve(A, b)", repr(np.linalg.solve(A, b)), "array([0.8, 1.4])")
check(18, "A @ x gives b back", repr(A @ np.linalg.solve(A, b)), "array([3., 5.])")
check(18, "det(A)", repr(np.linalg.det(A)), "np.float64(5.000000000000001)")
check(18, "det compares with isclose", bool(np.isclose(np.linalg.det(A), 5)), True)
check(18, "* is element-wise, @ is the matrix product", bool((A * A == A @ A).all()), False)
check(18, "inv(A) @ b agrees with solve", bool(np.allclose(np.linalg.inv(A) @ b, np.linalg.solve(A, b))), True)
check(18, "eigvals is complex (2.5+), real before", np.iscomplexobj(np.linalg.eigvals(A)), NP >= (2, 5))
check(18, "eigvalsh returns reals", (np.iscomplexobj(np.linalg.eigvalsh(A)), np.round(np.linalg.eigvalsh(A), 8).tolist()),
      (False, [1.38196601, 3.61803399]))
check(18, "inv of a singular matrix", raises(lambda: np.linalg.inv(np.array([[1., 2.], [2., 4.]]))),
      "LinAlgError: Singular matrix")


# ── slide 19 · saving & loading ───────────────────────────────────────────
scores = np.arange(6, dtype=np.int32).reshape(2, 3)
np.save(TMP / "scores.npy", scores)
back = np.load(TMP / "scores.npy")
check(19, ".npy keeps dtype and shape", (back.dtype, back.shape, back.tolist()), (np.dtype("int32"), (2, 3), scores.tolist()))
np.savez(TMP / "run.npz", x=np.array([1, 2]), y=np.array([3]))
check(19, ".npz bundles arrays by name", np.load(TMP / "run.npz")["x"].tolist(), [1, 2])
np.save(TMP / "obj.npy", np.array([{"a": 1}], dtype=object))
check(19, "np.load refuses pickled objects by default", raises(lambda: np.load(TMP / "obj.npy")),
      "ValueError: Object arrays cannot be loaded when allow_pickle=False")
montants = np.loadtxt(CSV, delimiter=",", skiprows=1, usecols=2)
check(19, "loadtxt reads 247 floats from the January CSV", (montants.shape, montants.dtype), ((247,), np.dtype("float64")))
check(19, "their float sum is 5308.389999999999", repr(montants.sum()), "np.float64(5308.389999999999)")


# ── slide 20 · pitfalls ───────────────────────────────────────────────────
check(20, "np.float_ was removed in 2.0", raises(lambda: np.float_).split(":")[0], "AttributeError")


print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
