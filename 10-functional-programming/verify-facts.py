"""Chapter 10 — re-run every fact that appears on a slide or in a note.

Verified on CPython 3.12.3. Error-message wording drifts between minor
versions, and slides 05, 07 and 17 quote messages verbatim. Slide 14 quotes
sys.getsizeof figures, which are specific to CPython 3.12 on 64-bit: on
another build they drift by design, and the slide must be updated. Run this
on the recording machine before recording:

    python3 verify-facts.py

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 21-slide deck: 01 cover, 02 divider, 03-20
content, 21 closing card. Slides 03 and 13 read
../00-premier-script/depenses_janvier.csv, the first video's data.

Stdlib only.
"""

import csv
import gc
import math
import operator
import sys
import weakref
from dataclasses import FrozenInstanceError, dataclass
from decimal import Decimal
from functools import cache, cached_property, lru_cache, partial, reduce, singledispatch, total_ordering, wraps
from itertools import accumulate, groupby, islice
from pathlib import Path
from types import MappingProxyType

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


print(f"CPython {sys.version}\n")
CSV = Path(__file__).resolve().parent.parent / "00-premier-script" / "depenses_janvier.csv"


# ── slide 3 · imperative vs functional ────────────────────────────────────
with open(CSV) as f:
    rows = list(csv.DictReader(f))
total = 0
for r in rows:
    if r["categorie"] == "Restaurant":
        total += Decimal(r["montant"])
check(3, "the loop gives 880.41", total, Decimal("880.41"))
check(3, "the expression gives the same",
      sum(Decimal(r["montant"]) for r in rows if r["categorie"] == "Restaurant"), Decimal("880.41"))


# ── slide 4 · pure functions ──────────────────────────────────────────────
def add_fee_impure(prices):
    for i, p in enumerate(prices):
        prices[i] = p + 1
    return prices


def add_fee_pure(prices):
    return [p + 1 for p in prices]


mine = [10, 20]
back = add_fee_impure(mine)
check(4, "the impure version changes the caller's list", mine, [11, 21])
check(4, "... and hands back the same list", back is mine, True)
mine = [10, 20]
back = add_fee_pure(mine)
check(4, "the pure version leaves the original alone", (mine, back, back is mine), ([10, 20], [11, 21], False))


# ── slide 5 · immutability ────────────────────────────────────────────────
tva = MappingProxyType({"taux": 20})


def _assign():
    tva["taux"] = 0


check(5, "MappingProxyType refuses assignment", raises(_assign),
      "TypeError: 'mappingproxy' object does not support item assignment")
t = (1, 2)


def _tuple_assign():
    t[0] = 9


check(5, "a tuple refuses assignment", raises(_tuple_assign).split(":")[0], "TypeError")
check(5, "frozenset has no add and is hashable", (hasattr(frozenset(), "add"), isinstance(hash(frozenset({1})), int)),
      (False, True))


@dataclass(frozen=True)
class Rate:
    taux: int


check(5, "a frozen dataclass refuses assignment",
      raises(lambda: setattr(Rate(20), "taux", 0)).split(":")[0], "FrozenInstanceError")
shallow = ([1],)
shallow[0].append(2)
check(5, "immutability is shallow: the list inside still changes", shallow, ([1, 2],))


# ── slide 6 · map & filter ────────────────────────────────────────────────
check(6, "map(pow, [2, 3], [3, 2])", list(map(pow, [2, 3], [3, 2])), [8, 9])
m = map(str.upper, ["a", "b"])
check(6, "map is consumed once", (list(m), list(m)), (["A", "B"], []))
check(6, "filter(None, ...) keeps truthy values", list(filter(None, [0, 1, "", 2])), [1, 2])
check(6, "map stops at the shortest", list(map(operator.add, [1, 2, 3], [10])), [11])


# ── slide 7 · reduce ──────────────────────────────────────────────────────
check(7, "reduce(add, [1, 2, 3])", reduce(operator.add, [1, 2, 3]), 6)
check(7, "empty without initial", raises(lambda: reduce(operator.add, [])),
      "TypeError: reduce() of empty iterable with no initial value")
check(7, "empty with initial 0", reduce(operator.add, [], 0), 0)
check(7, "it folds left: (1 + 2) + 3", reduce(lambda a, b: f"({a} + {b})", ["1", "2", "3"]), "((1 + 2) + 3)")
check(7, "math.prod([2, 3, 4])", math.prod([2, 3, 4]), 24)


# ── slide 8 · closures ────────────────────────────────────────────────────
def make_tax(rate):
    def apply(amount):
        return amount * (1 + rate)
    return apply


tax = make_tax(Decimal("0.20"))
check(8, "tva(Decimal('100'))", repr(tax(Decimal("100"))), "Decimal('120.00')")
check(8, "the captured variable is inspectable", tax.__closure__[0].cell_contents, Decimal("0.20"))
lam = (lambda r: lambda a: a * r)(2)
check(8, "a lambda captures the same way", (lam(3), lam.__closure__[0].cell_contents), (6, 2))


# ── slide 9 · late binding (the PLANT) ────────────────────────────────────
fs = [lambda: i for i in range(3)]
check(9, "three lambdas answer 2, 2, 2", [f() for f in fs], [2, 2, 2])
defs = []
for i in range(3):
    def g():
        return i
    defs.append(g)
check(9, "a def in the loop behaves the same", [f() for f in defs], [2, 2, 2])


# ── slide 10 · generator functions ────────────────────────────────────────
def countdown(n):
    while n > 0:
        yield n
        n -= 1


gen = countdown(3)
check(10, "next, next, next", (next(gen), next(gen), next(gen)), (3, 2, 1))
check(10, "then StopIteration", raises(lambda: next(gen)).split(":")[0], "StopIteration")
check(10, "next(g, None) returns the default", next(gen, None), None)
check(10, "a for loop stops at StopIteration", list(countdown(3)), [3, 2, 1])
check(10, "a generator can also receive values (send)", callable(countdown(1).send), True)


# ── slide 11 · generator expressions ──────────────────────────────────────
squares = (x * x for x in range(5))
check(11, "first sum is 30", sum(squares), 30)
check(11, "second sum is 0, silently", sum(squares), 0)
check(11, "no extra parentheses inside a call", sum(x * x for x in range(5)), 30)


# ── slide 12 · infinite sequences & yield from ────────────────────────────
def ids():
    n = 1
    while True:
        yield f"TX-{n:04d}"
        n += 1


check(12, "islice(ids(), 3)", list(islice(ids(), 3)), ["TX-0001", "TX-0002", "TX-0003"])


def inner():
    yield 1
    yield 2


def outer():
    yield 0
    yield from inner()
    yield 3


check(12, "yield from hands over until exhausted", list(outer()), [0, 1, 2, 3])


# ── slide 13 · pipelines ──────────────────────────────────────────────────
with open(CSV) as f:
    rows_it = csv.DictReader(f)
    resto = (r for r in rows_it if r["categorie"] == "Restaurant")
    piped = sum(Decimal(r["montant"]) for r in resto)
check(13, "the lazy pipeline gives Decimal('880.41')", repr(piped), "Decimal('880.41')")


def leaked():
    with open(CSV) as f:
        return (r for r in csv.DictReader(f))


check(13, "a generator taken out of the with reads a closed file",
      raises(lambda: list(leaked())).split(":")[0], "ValueError")


# ── slide 14 · memory ─────────────────────────────────────────────────────
n = range(1_000_000)
as_list = [x * x for x in n]
as_gen = (x * x for x in n)
check(14, "getsizeof(list) is 8448728 (CPython 3.12, 64-bit)", sys.getsizeof(as_list), 8448728)
check(14, "getsizeof(generator) is 200 (CPython 3.12, 64-bit)", sys.getsizeof(as_gen), 200)
check(14, "the list figure is only pointers: under 9 bytes per item, each int is 28+",
      (sys.getsizeof(as_list) / len(as_list) < 9, sys.getsizeof(999_999 * 999_999) >= 28), (True, True))
check(14, "a generator has no len()", raises(lambda: len(as_gen)), "TypeError: object of type 'generator' has no len()")
check(14, "same result", sum(as_gen), sum(as_list))


# ── slide 15 · groupby & accumulate ───────────────────────────────────────
data = ["Resto", "Courses", "Resto"]
check(15, "unsorted groupby repeats Resto", [k for k, _ in groupby(data)], ["Resto", "Courses", "Resto"])
check(15, "sorted groupby groups once", [k for k, _ in groupby(sorted(data))], ["Courses", "Resto"])
check(15, "accumulate on Decimals",
      list(accumulate([Decimal("13.16"), Decimal("5.5"), Decimal("23.62")])),
      [Decimal("13.16"), Decimal("18.66"), Decimal("42.28")])
check(15, "accumulate on these floats prints the same", list(accumulate([13.16, 5.5, 23.62])), [13.16, 18.66, 42.28])


# ── slide 16 · partial & operator (the PAYOFF) ────────────────────────────
def show(i):
    return i


fs = [partial(show, i) for i in range(3)]
check(16, "partial freezes 0, 1, 2", [f() for f in fs], [0, 1, 2])
fs = [lambda i=i: i for i in range(3)]
check(16, "the default-argument fix gives 0, 1, 2", [f() for f in fs], [0, 1, 2])
check(16, "itemgetter(1) is lambda r: r[1]", operator.itemgetter(1)(("a", 9)), 9)


class Row:
    total = 42


check(16, "attrgetter('total')", operator.attrgetter("total")(Row()), 42)
check(16, "methodcaller('upper')", operator.methodcaller("upper")("abc"), "ABC")
check(16, "sorted with key=itemgetter",
      sorted([("b", 2), ("a", 9)], key=operator.itemgetter(1)), [("b", 2), ("a", 9)])


# ── slide 17 · caching ────────────────────────────────────────────────────
@cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


check(17, "fib(100)", fib(100), 354224848179261915075)
info = fib.cache_info()
check(17, "cache_info: 98 hits, 101 misses", (info.hits, info.misses, info.maxsize), (98, 101, None))
check(17, "naive fib(100) needs over 10**21 calls", 2 * fib(101) - 1 > 10**21, True)


@lru_cache
def ident(x):
    return x


check(17, "lru_cache keeps 128 by default", ident.cache_info().maxsize, 128)
check(17, "a list argument is unhashable", raises(lambda: ident([1])), "TypeError: unhashable type: 'list'")


class Holder:
    @lru_cache
    def value(self):
        return 1


h = Holder()
h.value()
ref = weakref.ref(h)
del h
gc.collect()
check(17, "a cached method keeps self alive", ref() is not None, True)


class Report:
    calls = 0

    def __init__(self, rows):
        self.rows = rows

    @cached_property
    def total(self):
        Report.calls += 1
        return sum(self.rows)


rep = Report([1, 2])
rep.total, rep.total
check(17, "cached_property computes once per object", Report.calls, 1)
check(17, "cache exists (3.9+), cached_property (3.8+)", sys.version_info >= (3, 9), True)


# ── slide 18 · wraps, total_ordering, singledispatch ──────────────────────
def deco(fn):
    @wraps(fn)
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper


@deco
def alpha():
    pass


check(18, "wraps keeps the name", alpha.__name__, "alpha")


@total_ordering
class Box:
    def __init__(self, a):
        self.a = a

    def __eq__(self, o):
        return self.a == o.a

    def __lt__(self, o):
        return self.a < o.a


check(18, "total_ordering derives >= from two", Box(3) >= Box(2), True)


@singledispatch
def fmt(x):
    return repr(x)


@fmt.register
def _(x: Decimal):
    return f"{x:.2f} €"


check(18, "fmt(Decimal('13.16'))", fmt(Decimal("13.16")), "13.16 €")
check(18, "anything else falls back to repr", (fmt("a"), fmt(3)), ("'a'", "3"))


# ── slide 19 · composition ────────────────────────────────────────────────
def pipe(*fns):
    return lambda x: reduce(lambda acc, f: f(acc), fns, x)


clean = pipe(str.strip, str.lower, str.title)
check(19, "clean('  LA FONTAINE ')", clean("  LA FONTAINE "), "La Fontaine")
check(19, "pipe() with no functions returns its input", pipe()(5), 5)


print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
