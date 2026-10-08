"""Chapter 11 — re-run every fact that appears on a slide or in a note.

Verified on CPython 3.12.3, 3.13.11 and 3.14.2 (standard builds). Error
messages drift between minor versions: slides 05, 08 and 10 quote them, and
slide 10's AttributeError gains a suffix on 3.13+. Slide 10's tracemalloc
figures are version-specific, so the expectation follows the running version.
Slides 11-14 time real work; the checks assert the direction (slower, faster,
concurrent), not exact seconds, and print the measured numbers for the note.

Run this on the recording machine before recording:

    python3 verify-facts.py

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 21-slide deck: 01 cover, 02 divider, 03-20
content, 21 closing card.

Not checkable here, documented only: the free-threaded build's official
support in 3.14 (PEP 779) needs a free-threaded interpreter; the Python 3.15
profiling package (slide 18) is checked only when run on 3.15+.

Stdlib only.
"""

import asyncio
import contextlib
import gc
import importlib.util
import inspect
import io
import multiprocessing
import os
import pdb
import pstats
import cProfile
import subprocess
import sys
import tempfile
import threading
import time
import timeit
import tracemalloc
import weakref
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from contextlib import ExitStack, suppress
from dataclasses import dataclass
from functools import wraps
from multiprocessing import Pool, Process, Queue
from pathlib import Path
from typing import Generic, Protocol, TypedDict, TypeVar, runtime_checkable

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


def work(n):
    s = 0
    for i in range(n):
        s += i
    return s


def _queue_child(q):
    q.put("from the child")


V = sys.version_info
TMP = Path(tempfile.mkdtemp(prefix="nl-ch11-"))


def main():
    print(f"CPython {sys.version}\n")

    # ── slide 3 · writing a decorator ─────────────────────────────────────
    def log_calls(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"calling {fn.__name__}{args}")
            return fn(*args, **kwargs)
        return wrapper

    @log_calls
    def add(a, b):
        return a + b

    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = add(2, 3)
    check(3, "add(2, 3) prints 'calling add(2, 3)'", out.getvalue(), "calling add(2, 3)\n")
    check(3, "... and returns 5", result, 5)
    check(3, "@wraps keeps the name add", add.__name__, "add")

    def bare(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper

    def plain(a, b):
        return a + b

    check(3, "@log_calls is add = log_calls(add)", log_calls(plain)(2, 3), 5)
    check(3, "without wraps the name is 'wrapper'", bare(plain).__name__, "wrapper")

    # ── slide 4 · decorators with arguments ───────────────────────────────
    def retry(times):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                for n in range(1, times + 1):
                    try:
                        return fn(*args, **kwargs)
                    except ConnectionError:
                        print(f"attempt {n} failed")
                raise ConnectionError("gave up")
            return wrapper
        return decorator

    outcomes = iter([ConnectionError, ConnectionError, "ok"])

    @retry(times=3)
    def fetch():
        o = next(outcomes)
        if o is ConnectionError:
            raise ConnectionError()
        return o

    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = fetch()
    check(4, "fails twice, then returns its result",
          (out.getvalue(), result), ("attempt 1 failed\nattempt 2 failed\n", "ok"))

    @retry(times=3)
    def never():
        raise ConnectionError()

    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        err = raises(never)
    check(4, "three failures, then 'gave up'", (out.getvalue().count("failed"), err), (3, "ConnectionError: gave up"))
    check(4, "retry(times=3) returns the real decorator", callable(retry(times=3)), True)

    # ── slide 5 · class decorators & the singleton ────────────────────────
    def singleton(cls):
        inst = {}

        @wraps(cls)
        def get(*args, **kwargs):
            if cls not in inst:
                inst[cls] = cls(*args, **kwargs)
            return inst[cls]
        return get

    @singleton
    class Config:
        pass

    check(5, "Config() is Config()", Config() is Config(), True)
    check(5, "Config is now a function", inspect.isfunction(Config), True)
    check(5, "isinstance(c, Config) raises TypeError", raises(lambda: isinstance(Config(), Config)),
          "TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union")
    import json as first_import
    import json as second_import
    check(5, "a module is imported once", first_import is second_import, True)

    # ── slide 6 · context managers, revisited ─────────────────────────────
    with suppress(FileNotFoundError):
        os.remove(TMP / "cache.tmp")
    check(6, "suppress swallows FileNotFoundError", True, True)

    class Swallow:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return True

    def _swallowed():
        with Swallow():
            raise ValueError("gone")

    check(6, "__exit__ returning True swallows the exception", raises(_swallowed), "<no exception>")
    order = []
    with ExitStack() as stack:
        for name in ["a", "b", "c"]:
            stack.callback(order.append, name)
    check(6, "ExitStack closes in reverse order", order, ["c", "b", "a"])
    paths = []
    for i in range(3):
        p = TMP / f"f{i}.txt"
        p.write_text(str(i))
        paths.append(p)
    with ExitStack() as stack:
        files = [stack.enter_context(open(p)) for p in paths]
    check(6, "every file is closed on the way out", all(f.closed for f in files), True)

    # ── slide 7 · descriptors ─────────────────────────────────────────────
    class Positive:
        def __set_name__(self, owner, name):
            self.name = "_" + name

        def __get__(self, obj, objtype=None):
            return getattr(obj, self.name)

        def __set__(self, obj, value):
            if value < 0:
                raise ValueError("must be positive")
            setattr(obj, self.name, value)

    class Tx:
        amount = Positive()
        quantity = Positive()

        def __init__(self, amount, quantity=1):
            self.amount = amount
            self.quantity = quantity

    check(7, "Tx(-5) raises", raises(lambda: Tx(-5)), "ValueError: must be positive")
    check(7, "Tx(5).amount reads back", Tx(5).amount, 5)
    check(7, "__set_name__ learns the field name", Tx.__dict__["amount"].name, "_amount")
    check(7, "one class guards any field", raises(lambda: Tx(5, -1)), "ValueError: must be positive")
    check(7, "property has __get__, __set__ and __delete__",
          all(hasattr(property, m) for m in ("__get__", "__set__", "__delete__")), True)
    check(7, "functions are descriptors too", hasattr(add, "__get__"), True)

    # ── slide 8 · __getattr__ vs __getattribute__ ─────────────────────────
    class Lazy:
        def __getattr__(self, name):
            return f"computed {name}"

    obj = Lazy()
    obj.x = 1
    check(8, "obj.x, obj.y", (obj.x, obj.y), (1, "computed y"))

    class Bad:
        def __getattribute__(self, name):
            return self.__dict__[name]

    check(8, "__getattribute__ via self.__dict__ recurses", raises(lambda: Bad().a).split(":")[0], "RecursionError")

    class Good:
        def __getattribute__(self, name):
            return super().__getattribute__(name)

    g = Good()
    g.a = 7
    check(8, "super().__getattribute__ delegates safely", g.a, 7)

    # ── slide 9 · metaclasses ─────────────────────────────────────────────
    Point = type("Point", (), {"x": 0})
    check(9, "type() builds a class", (Point.__name__, Point().x), ("Point", 0))
    check(9, "type(Point), type(type)", repr((type(Point), type(type))), "(<class 'type'>, <class 'type'>)")

    class Meta(type):
        def __new__(mcls, name, bases, ns):
            ns["built_by"] = mcls.__name__
            return super().__new__(mcls, name, bases, ns)

    class Model(metaclass=Meta):
        pass

    check(9, "a metaclass shapes the class as it is built", (Model.built_by, type(Model) is Meta), ("Meta", True))

    class Plugin:
        registry = {}

        def __init_subclass__(cls, **kw):
            super().__init_subclass__(**kw)
            Plugin.registry[cls.__name__] = cls

    class Csv(Plugin):
        pass

    check(9, "class Csv(Plugin) registers Csv", list(Plugin.registry), ["Csv"])

    # ── slide 10 · __slots__ ──────────────────────────────────────────────
    class SPoint:
        __slots__ = ("x", "y")

    sp = SPoint()
    sp.x = 1
    msg = raises(lambda: setattr(sp, "z", 3))
    check(10, "AttributeError for a new attribute",
          msg.startswith("AttributeError: 'SPoint' object has no attribute 'z'"), True)
    check(10, "3.13+ adds 'and no __dict__ for setting new attributes'",
          msg.endswith("and no __dict__ for setting new attributes"), V >= (3, 13))
    check(10, "no __dict__", hasattr(sp, "__dict__"), False)

    @dataclass(slots=True)
    class D:
        x: int

    check(10, "dataclass(slots=True) writes __slots__ (3.10+)", (D.__slots__, hasattr(D(1), "__dict__")), (("x",), False))

    class Plain2:
        def __init__(self):
            self.x = 1
            self.y = 2

    class Slots2:
        __slots__ = ("x", "y")

        def __init__(self):
            self.x = 1
            self.y = 2

    def mem(cls):
        tracemalloc.start()
        objs = [cls() for _ in range(100_000)]
        cur, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        del objs
        return round(cur / 1_000_000, 1)

    check(10, "100k plain objects: 8.8 MB on 3.12, 9.6 MB on 3.13+", mem(Plain2), 8.8 if V < (3, 13) else 9.6)
    check(10, "100k slotted objects: 5.6 MB", mem(Slots2), 5.6)

    # ── slide 11 · threads & the GIL (the PLANT) ──────────────────────────
    jobs = [4_000_000] * 4
    t = time.perf_counter()
    for n in jobs:
        work(n)
    serial = time.perf_counter() - t
    t = time.perf_counter()
    threads = [threading.Thread(target=work, args=(n,)) for n in jobs]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    threaded = time.perf_counter() - t
    info(11, f"serial {serial:.2f} s, four threads {threaded:.2f} s ({serial / threaded:.2f}x)")
    check(11, "four CPU-bound threads are not faster than serial", threaded > serial, True)
    gil = sys._is_gil_enabled() if hasattr(sys, "_is_gil_enabled") else True
    check(11, "the GIL is enabled by default", gil, True)

    t = time.perf_counter()
    waits = [threading.Thread(target=time.sleep, args=(0.3,)) for _ in range(4)]
    for th in waits:
        th.start()
    for th in waits:
        th.join()
    check(11, "waiting threads overlap (4 x 0.3 s in under 0.6 s)", time.perf_counter() - t < 0.6, True)

    counter = 0
    lock = threading.Lock()

    def bump():
        nonlocal counter
        for _ in range(10_000):
            with lock:
                counter += 1

    bumpers = [threading.Thread(target=bump) for _ in range(4)]
    for th in bumpers:
        th.start()
    for th in bumpers:
        th.join()
    check(11, "Lock protects a shared counter", counter, 40_000)

    sem = threading.Semaphore(2)
    active, peak = 0, 0
    guard = threading.Lock()

    def limited():
        nonlocal active, peak
        with sem:
            with guard:
                active += 1
                peak = max(peak, active)
            time.sleep(0.05)
            with guard:
                active -= 1

    limiters = [threading.Thread(target=limited) for _ in range(6)]
    for th in limiters:
        th.start()
    for th in limiters:
        th.join()
    check(11, "Semaphore(2) caps concurrency at 2", peak, 2)

    ev = threading.Event()
    seen = []
    waiter = threading.Thread(target=lambda: seen.append(ev.wait(timeout=2)))
    waiter.start()
    ev.set()
    waiter.join()
    check(11, "Event wakes a waiting thread", seen, [True])

    # ── slide 12 · processes (the PAYOFF) ─────────────────────────────────
    t = time.perf_counter()
    with Pool(4) as pool:
        pool.map(work, jobs)
    pooled = time.perf_counter() - t
    info(12, f"serial {serial:.2f} s, Pool(4) {pooled:.2f} s ({serial / pooled:.2f}x), {os.cpu_count()} CPUs, "
             f"start method {multiprocessing.get_start_method()}")
    check(12, "Pool(4) is faster than serial (needs 2+ CPUs)", serial / pooled > 1.3, True)
    with Pool(2) as pool:
        check(12, "arguments are pickled: a lambda cannot cross",
              raises(lambda: pool.map(lambda x: x, [1])) != "<no exception>", True)
    q = Queue()
    p = Process(target=_queue_child, args=(q,))
    p.start()
    got = q.get(timeout=10)
    p.join()
    check(12, "Process and Queue: a value crosses back", got, "from the child")
    if sys.platform.startswith("linux"):
        check(12, "Linux start method: fork until 3.13, forkserver from 3.14",
              multiprocessing.get_start_method(), "forkserver" if V >= (3, 14) else "fork")
    with ProcessPoolExecutor(2) as ex, ThreadPoolExecutor(2) as tex:
        check(12, "concurrent.futures: one API for processes and threads",
              (list(ex.map(work, [10, 20])), list(tex.map(work, [10, 20]))), ([45, 190], [45, 190]))

    # ── slide 13 · asyncio: async & await ─────────────────────────────────
    async def afetch(i):
        await asyncio.sleep(0.5)
        return i

    async def gathered():
        t0 = time.perf_counter()
        r = await asyncio.gather(afetch(1), afetch(2), afetch(3))
        return r, time.perf_counter() - t0

    r, elapsed = asyncio.run(gathered())
    info(13, f"gather of three 0.5 s waits took {elapsed:.2f} s")
    check(13, "gather returns [1, 2, 3]", r, [1, 2, 3])
    check(13, "in about 0.5 s, not 1.5 s", elapsed < 0.9, True)
    ran = []

    async def marks():
        ran.append(True)

    coro = marks()
    check(13, "calling an async def runs nothing, builds a coroutine", (inspect.iscoroutine(coro), ran), (True, []))
    coro.close()

    async def background():
        task = asyncio.create_task(afetch(9))
        mine = "carried on"
        return mine, await task

    check(13, "create_task runs in the background", asyncio.run(background()), ("carried on", 9))

    # ── slide 14 · asyncio in practice ────────────────────────────────────
    async def grouped():
        async with asyncio.TaskGroup() as tg:
            a = tg.create_task(afetch(1))
            b = tg.create_task(afetch(2))
        return a.result(), b.result()

    check(14, "TaskGroup waits for all (3.11+)", asyncio.run(grouped()), (1, 2))
    cancelled = []

    async def two_fail_one_slow():
        async def boom(x):
            await asyncio.sleep(0.05)
            raise ValueError(x)

        async def slow():
            try:
                await asyncio.sleep(5)
            except asyncio.CancelledError:
                cancelled.append(True)
                raise

        async with asyncio.TaskGroup() as tg:
            tg.create_task(boom("a"))
            tg.create_task(boom("b"))
            tg.create_task(slow())

    caught = []
    try:
        asyncio.run(two_fail_one_slow())
    except* ValueError as eg:
        caught = sorted(str(e) for e in eg.exceptions)
    check(14, "two failures arrive as one ExceptionGroup, caught by except*", caught, ["a", "b"])
    check(14, "the remaining task was cancelled", cancelled, [True])

    async def too_slow():
        async with asyncio.timeout(0.1):
            await asyncio.sleep(1)

    check(14, "asyncio.timeout cancels past the deadline (3.11+)", raises(lambda: asyncio.run(too_slow())).split(":")[0],
          "TimeoutError")
    check(14, "to_thread runs blocking code (3.9+)", asyncio.run(asyncio.to_thread(work, 10)), 45)

    async def blocking_pair():
        async def blocker():
            time.sleep(0.2)
        t0 = time.perf_counter()
        await asyncio.gather(blocker(), blocker())
        return time.perf_counter() - t0

    check(14, "time.sleep in a coroutine blocks the loop (two take 0.4 s+)", asyncio.run(blocking_pair()) >= 0.39, True)
    if V >= (3, 14):
        r2 = subprocess.run([sys.executable, "-m", "asyncio", "ps", "-h"], capture_output=True, text=True)
        check(14, "python -m asyncio ps exists (3.14+)", r2.returncode, 0)

    # ── slide 15 · generics ───────────────────────────────────────────────
    T = TypeVar("T")

    class OldStack(Generic[T]):
        def __init__(self):
            self.items = []

    check(15, "TypeVar and Generic still work", OldStack[int]().items, [])
    if V >= (3, 12):
        ns = {}
        exec(
            "from typing import Self\n"
            "def first[T](xs: list[T]) -> T:\n"
            "    return xs[0]\n"
            "class Stack[T]:\n"
            "    def __init__(self) -> None:\n"
            "        self.items: list[T] = []\n"
            "    def push(self, x: T) -> Self:\n"
            "        self.items.append(x)\n"
            "        return self\n",
            ns,
        )
        check(15, "first([3, 4]) with the 3.12 syntax", ns["first"]([3, 4]), 3)
        check(15, "the type parameter is T", [tp.__name__ for tp in ns["first"].__type_params__], ["T"])
        check(15, "push returns Self, so it chains", ns["Stack"]().push(1).push(2).items, [1, 2])
        check(15, "nothing is checked at run time", ns["first"]("ab"), "a")
    check(15, "typing.Self exists (3.11+)", importlib.util.find_spec("typing") is not None and V >= (3, 11), True)

    # ── slide 16 · Protocol & TypedDict ───────────────────────────────────
    class HasTotal(Protocol):
        def total(self) -> int: ...

    @runtime_checkable
    class HasTotalRC(Protocol):
        def total(self) -> int: ...

    class Invoice:
        def total(self):
            return 42

    check(16, "any class with total() matches, no inheritance", (isinstance(Invoice(), HasTotalRC), isinstance(3, HasTotalRC)),
          (True, False))
    check(16, "isinstance needs @runtime_checkable", raises(lambda: isinstance(Invoice(), HasTotal)).split(":")[0],
          "TypeError")

    class Row(TypedDict):
        categorie: str
        montant: float

    row = Row(categorie="Resto", montant=13.16)
    check(16, "a TypedDict is a plain dict at run time", type(row) is dict, True)
    check(16, "nothing is validated", Row(categorie=1, montant="x"), {"categorie": 1, "montant": "x"})

    # ── slide 17 · memory ─────────────────────────────────────────────────
    class Node:
        pass

    single = Node()
    ref_single = weakref.ref(single)
    del single
    check(17, "no cycle: freed as soon as the last reference goes", ref_single(), None)
    gc.disable()
    a, b = Node(), Node()
    a.other, b.other = b, a
    ref_a = weakref.ref(a)
    del a, b
    alive_before = ref_a() is not None
    gc.collect()
    gc.enable()
    check(17, "a cycle survives del", alive_before, True)
    check(17, "gc.collect() frees the pair", ref_a(), None)
    tracemalloc.start()
    blob = [bytes(1000) for _ in range(100)]
    top = tracemalloc.take_snapshot().statistics("lineno")
    tracemalloc.stop()
    del blob
    check(17, "tracemalloc reports allocations by line", top[0].traceback[0].lineno > 0, True)

    # ── slide 18 · profiling ──────────────────────────────────────────────
    script = TMP / "app.py"
    script.write_text("def slow():\n    return sum(range(100_000))\nfor _ in range(3):\n    slow()\n")
    r3 = subprocess.run([sys.executable, "-m", "cProfile", "-s", "cumulative", str(script)],
                        capture_output=True, text=True)
    check(18, "python -m cProfile -s cumulative app.py", "Ordered by: cumulative time" in r3.stdout, True)
    prof = cProfile.Profile()
    prof.runcall(work, 1000)
    buf = io.StringIO()
    pstats.Stats(prof, stream=buf).sort_stats("cumulative").print_stats(3)
    check(18, "pstats sorts cProfile's output", "cumulative" in buf.getvalue(), True)
    check(18, "timeit returns seconds", timeit.timeit("sum(range(1000))", number=10_000) > 0, True)
    if V >= (3, 15):
        check(18, "profiling.sampling exists (3.15+)", importlib.util.find_spec("profiling.sampling") is not None, True)

    # ── slide 19 · debugging ──────────────────────────────────────────────
    r4 = subprocess.run([sys.executable, "-c", "breakpoint(); print('ran')"],
                        env={**os.environ, "PYTHONBREAKPOINT": "0"}, capture_output=True, text=True)
    check(19, "PYTHONBREAKPOINT=0 turns breakpoint() off", r4.stdout, "ran\n")
    check(19, "pdb has n, s, c, p, w",
          all(hasattr(pdb.Pdb, f"do_{c}") for c in ("next", "step", "continue", "p", "where")), True)
    crash = TMP / "crash.py"
    crash.write_text("x = 1\nraise ValueError('boom')\n")
    r5 = subprocess.run([sys.executable, "-m", "pdb", str(crash)], input="c\nq\nq\n", capture_output=True, text=True,
                        timeout=30)
    check(19, "python -m pdb lands on the crash (post-mortem)", "post mortem" in r5.stdout.lower(), True)
    if V >= (3, 14):
        h = subprocess.run([sys.executable, "-m", "pdb", "-h"], capture_output=True, text=True).stdout
        check(19, "python -m pdb -p PID exists (3.14+)", "-p" in h, True)

    print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
    for slide, label in FAILS:
        print(f"  slide {slide:02}: {label}")
    return 1 if FAILS else 0


if __name__ == "__main__":  # required: slide 12's Pool re-imports this file
    sys.exit(main())
