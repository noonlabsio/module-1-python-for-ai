"""Chapter 08 — re-run every fact that appears on a slide.

Verified on CPython 3.12.3. Error-message wording drifts between minor
versions, and slides 08, 12, 15, 17, 18, 20, 21 and 23 quote messages
verbatim. Run this on the recording machine before recording:

    python3 verify-facts.py

Exit code is 1 if anything drifted. Slide numbers refer to the 24-slide
deck: 01 cover, 02 divider, 03-23 content, 24 closing card.
"""

import functools
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

FAILS = []


def check(slide, label, actual, expected):
    ok = actual == expected
    if not ok:
        FAILS.append((slide, label))
    print(f"[{'ok  ' if ok else 'DRIFT'}] s{slide:02} {label}")
    if not ok:
        print(f"         slide says:  {expected!r}")
        print(f"         python says: {actual!r}")


def raises(fn):
    try:
        fn()
    except Exception as e:
        return f"{type(e).__name__}: {e}"
    return "<no exception>"


print(f"CPython {sys.version.split()[0]}\n")

# ── slide 5 · self is a parameter name, not a keyword ────────────────────
class _Renamed:
    def __init__(this, x):  # noqa: N805
        this.x = x


check(5, "self can be renamed", _Renamed(3).x, 3)


# ── slide 6 · a mutable class attribute is one object (the PLANT) ────────
class Account:
    history = []

    def __init__(self, owner):
        self.owner = owner


_a, _b = Account("Amina"), Account("Bruno")
_a.history.append("open")
check(6, "class attr is shared", (_b.history, _a.history is _b.history), (["open"], True))


# ── slide 7 · name mangling ──────────────────────────────────────────────
class Vault:
    def __init__(self):
        self.__pin = 1234


_v = Vault()
check(7, "mangled attribute name", list(vars(_v)), ["_Vault__pin"])
check(7, "reachable via mangled name", _v._Vault__pin, 1234)


# ── slide 8 · read-only computed property ────────────────────────────────
class Rect:
    def __init__(self, w, h):
        self.w, self.h = w, h

    @property
    def area(self):
        return self.w * self.h


check(8, "computed property reads", Rect(5, 3).area, 15)
check(8,
    "no setter means read-only",
    raises(lambda: setattr(Rect(5, 3), "area", 10)),
    "AttributeError: property 'area' of 'Rect' object has no setter",
)


# ── slide 12 · MRO, and cooperative super() ───────────────────────────────
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


check(12, "diamond MRO order", [c.__name__ for c in D.__mro__], ["D", "B", "C", "A", "object"])


def _bad_mro():
    class Impossible(A, B): pass


check(12,
    "inconsistent MRO refused",
    raises(_bad_mro).startswith("TypeError: Cannot create a consistent method resolution"),
    True,
)
# CPython puts a hard newline in that message, after "resolution". Narration
# on slide 12 warns that a live demo wraps differently than the slide.
check(12, "MRO message is two real lines", raises(_bad_mro).count("\n"), 1)


class Base:
    def __init__(self):
        self.base = True


class GoodMixin:
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mixed = True


class BadMixin:
    def __init__(self, **kw):
        self.mixed = True  # never calls super()


class GoodChild(GoodMixin, Base): pass
class BadChild(BadMixin, Base): pass


check(12, "cooperative mixin sets both", sorted(vars(GoodChild())), ["base", "mixed"])
check(12, "mixin skipping super() loses parent state", sorted(vars(BadChild())), ["mixed"])


# ── slide 14 · isinstance respects inheritance, type() does not ───────────
check(14, "isinstance sees the subclass", isinstance(True, int), True)
check(14, "type() does not", type(True) is int, False)
check(14, "issubclass", issubclass(B, A), True)


# ── slide 15 · abstract class refuses to instantiate ──────────────────────
class Loader(ABC):
    @abstractmethod
    def load(self): ...


class Passthrough(Loader):
    pass


check(15,
    "abstract instantiation",
    raises(Passthrough),
    "TypeError: Can't instantiate abstract class Passthrough "
    "without an implementation for abstract method 'load'",
)


# ── slide 16 · str falls back to repr, not the reverse ────────────────────
class OnlyRepr:
    def __repr__(self):
        return "OnlyRepr()"


class OnlyStr:
    def __str__(self):
        return "readable"


check(16, "str() uses __repr__", str(OnlyRepr()), "OnlyRepr()")
check(16, "repr() ignores __str__", repr(OnlyStr()).startswith("<"), True)


# ── slide 17 · ordering, and total_ordering ───────────────────────────────
@functools.total_ordering
class Box:
    def __init__(self, a):
        self.a = a

    def __eq__(self, o):
        return self.a == o.a

    def __lt__(self, o):
        return self.a < o.a


check(17, "total_ordering derives >=", (Box(6) >= Box(4), Box(2) > Box(9)), (True, False))
check(17, "__eq__ gives != for free", Box(1) != Box(2), True)


# ── slide 17 · __eq__ sets __hash__ to None ───────────────────────────────
class Money:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        return self.v == other.v


check(17, "__hash__ is None", Money.__hash__, None)
check(17, "unhashable", raises(lambda: {Money(1)}), "TypeError: unhashable type: 'Money'")
check(17, "total_ordering does not restore hash", Box.__hash__, None)


# ── slide 18 · NotImplemented, not a raised TypeError ─────────────────────
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


check(18, "Vector + Vector", repr(Vector(1, 2) + Vector(3, 4)), "Vector(4, 6)")
check(18,
    "NotImplemented yields Python's own message",
    raises(lambda: Vector(1, 2) + 3),
    "TypeError: unsupported operand type(s) for +: 'Vector' and 'int'",
)


# ── slide 18 · __iadd__ must return self ──────────────────────────────────
class BadCounter:
    def __init__(self, v=0):
        self.value = v

    def __iadd__(self, o):
        self.value += o  # no return


def _forgot_return():
    c = BadCounter(5)
    c += 3
    return c


check(18, "__iadd__ without return gives None", _forgot_return(), None)


class GoodCounter:
    def __init__(self, v=0):
        self.value = v

    def __iadd__(self, o):
        self.value += o
        return self


def _with_return():
    c = GoodCounter(5)
    c += 3
    return c.value


check(18, "__iadd__ returning self", _with_return(), 8)


class OnlyAdd:
    def __init__(self, v):
        self.v = v

    def __add__(self, o):
        return OnlyAdd(self.v + o)


def _rebinds():
    a = OnlyAdd(1)
    before = id(a)
    a += 1
    return before == id(a), a.v


check(18, "+= falls back to __add__ and rebinds", _rebinds(), (False, 2))


# ── slide 19 · container protocol fallbacks ───────────────────────────────
class Deck:
    def __init__(self):
        self.cards = ["A", "K"]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]


check(19, "len / index / in with no __contains__", (len(Deck()), Deck()[0], "K" in Deck()), (2, "A", True))


class OldProtocol:
    def __getitem__(self, i):
        if i > 2:
            raise IndexError
        return i * 10


check(19, "__getitem__ alone is iterable", list(OldProtocol()), [0, 10, 20])


# ── slide 20 · the PAYOFF ─────────────────────────────────────────────────
def _mutable_default():
    @dataclass
    class Bad:
        owner: str
        history: list = []


check(20,
    "dataclass refuses mutable default",
    raises(_mutable_default),
    "ValueError: mutable default <class 'list'> for field history "
    "is not allowed: use default_factory",
)


@dataclass
class Good:
    owner: str
    history: list = field(default_factory=list)


_g1, _g2 = Good("Amina"), Good("Bruno")
_g1.history.append("open")
check(20, "default_factory isolates", _g2.history, [])
check(20, "dataclass writes __repr__ and __eq__", (repr(Good("A")), Good("A") == Good("A")),
      ("Good(owner='A', history=[])", True))


# ── slide 21 · dataclass and field options ────────────────────────────────
@dataclass
class Plain:
    name: str


check(21, "plain dataclass is unhashable", Plain.__hash__, None)
check(21, "plain dataclass rejected by set", raises(lambda: {Plain("a")}),
      "TypeError: unhashable type: 'Plain'")


@dataclass(frozen=True)
class Frozen:
    amount: float


check(21, "frozen is hashable", isinstance(hash(Frozen(47.2)), int), True)
check(21,
    "frozen refuses assignment",
    raises(lambda: setattr(Frozen(47.2), "amount", 1)),
    "FrozenInstanceError: cannot assign to field 'amount'",
)


@dataclass(order=True)
class Ranked:
    rank: int


@dataclass(frozen=True)
class FrozenList:
    items: list


_fl = FrozenList([1])
_fl.items.append(2)
check(21, "frozen stops reassignment, not mutation", _fl.items, [1, 2])
check(21, "a list field makes hash() fail", raises(lambda: hash(_fl)), "TypeError: unhashable type: 'list'")
check(21, "order=True sorts", [r.rank for r in sorted([Ranked(3), Ranked(1)])], [1, 3])


@dataclass(unsafe_hash=True)
class Unsafe:
    v: int


check(21, "unsafe_hash=True is hashable", isinstance(hash(Unsafe(1)), int), True)


@dataclass
class Fields:
    a: int
    token: str = field(repr=False)
    created: int = field(default=0, compare=False)


check(21, "field(repr=False) hides it", repr(Fields(1, "secret", 9)), "Fields(a=1, created=9)")
check(21, "field(compare=False) excluded from ==", Fields(1, "s", 1) == Fields(1, "s", 2), True)


# ── slide 22 · functools.wraps ────────────────────────────────────────────
def bare(f):
    def wrapper(*a, **k):
        return f(*a, **k)
    return wrapper


def wrapped(f):
    @functools.wraps(f)
    def wrapper(*a, **k):
        return f(*a, **k)
    return wrapper


@bare
def alpha():
    """doc alpha"""


@wrapped
def beta():
    """doc beta"""


check(22, "without wraps, name is lost", (alpha.__name__, alpha.__doc__), ("wrapper", None))
check(22, "with wraps, name survives", (beta.__name__, beta.__doc__), ("beta", "doc beta"))
check(22, "wraps sets __wrapped__", beta.__wrapped__.__name__, "beta")


@wrapped
def _boom():
    raise ValueError("x")


def _frames(fn):
    import traceback
    try:
        fn()
    except ValueError as e:
        return [f.name for f in traceback.extract_tb(e.__traceback__)][1:]


check(22, "with wraps, the traceback still shows a wrapper frame", _frames(_boom), ["wrapper", "_boom"])


# ── slide 23 · the three closing error messages ───────────────────────────
class Transaction:
    def __init__(self, label, amount):
        self.label = label
        self.amount = amount


check(23,
    "missing positional arg",
    raises(lambda: Transaction("Carrefour")),
    "TypeError: Transaction.__init__() missing 1 required "
    "positional argument: 'amount'",
)


class Refund(Transaction):
    def __init__(self, ref):  # deliberately forgets super().__init__()
        self.ref = ref


check(23,
    "forgotten super()",
    raises(lambda: Refund("R1").label),
    "AttributeError: 'Refund' object has no attribute 'label'",
)

print(
    "\nNOTE  slide 23 shows \"Did you mean: 'ref'?\" — that suffix is added by the\n"
    "      traceback printer, not by str(exception), so it will not appear above.\n"
    "      To confirm it, write the two classes to a file and run it, then read\n"
    "      the printed traceback rather than catching the exception."
)

print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
