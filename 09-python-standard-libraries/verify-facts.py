"""Chapter 09 — re-run every fact that appears on a slide or in a note.

Verified on CPython 3.12.3. Error-message wording drifts between minor
versions, and slides 05, 12 and 14 quote messages verbatim. Run this on the
recording machine before recording:

    python3 verify-facts.py

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 21-slide deck: 01 cover, 02 divider, 03-20
content, 21 closing card. Slide 12's shell checks need a POSIX shell.
Slide 09 reads ../00-premier-script/depenses_janvier.csv, the first video's
data, so a change to that file shows up here.

Stdlib only.
"""

import argparse
import configparser
import csv
import decimal
import contextlib
import gzip
import hashlib
import heapq
import io
import itertools
import logging
import math
import os
import random
import re
import secrets
import shutil
import sqlite3
import statistics
import subprocess
import sys
import tempfile
import time
import tomllib
import warnings
import zipfile
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from datetime import datetime, timedelta, timezone
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from itertools import chain, combinations, count, islice, takewhile
from logging.handlers import RotatingFileHandler
from pathlib import Path

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


def child(code):
    """Run code in a fresh, isolated interpreter; return (stdout, stderr)."""
    r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True)
    return r.stdout, r.stderr


print(f"CPython {sys.version}\n")
TMP = Path(tempfile.mkdtemp(prefix="nl-ch09-"))


# ── slide 3 · every module on the map ships with CPython ──────────────────
MAP = ["datetime", "time", "collections", "itertools", "math", "random", "decimal", "re", "os", "sys",
       "subprocess", "shutil", "configparser", "tomllib", "sqlite3", "argparse", "logging", "hashlib", "secrets"]
check(3, "all 19 modules on the map are standard library", [m for m in MAP if m not in sys.stdlib_module_names], [])


# ── slide 4 · datetime: parse, shift, format ──────────────────────────────
d = datetime.strptime("31/01/2026", "%d/%m/%Y")
check(4, "strptime parses 31/01/2026", d, datetime(2026, 1, 31))
check(4, "one day later prints 2026-02-01 00:00:00", str(d + timedelta(days=1)), "2026-02-01 00:00:00")
check(4, "strftime %Y-%m-%d", d.strftime("%Y-%m-%d"), "2026-01-31")
check(4, "timedelta handles a leap day", datetime(2028, 2, 28) + timedelta(days=1), datetime(2028, 2, 29))
check(4, "fromisoformat needs no format string", datetime.fromisoformat("2026-01-31"), d)
check(4, "fromisoformat accepts a trailing Z (3.11+)",
      raises(lambda: datetime.fromisoformat("2026-01-31T10:00:00Z")) == "<no exception>"
      and datetime.fromisoformat("2026-01-31T10:00:00Z").tzinfo is not None, True)


# ── slide 5 · timezones and the time module ───────────────────────────────
check(5, "naive vs aware comparison is refused",
      raises(lambda: datetime.now() < datetime.now(timezone.utc)),
      "TypeError: can't compare offset-naive and offset-aware datetimes")
try:
    from zoneinfo import ZoneInfo
    paris = ZoneInfo("Europe/Paris")
    check(5, "Paris is UTC+2 in July", datetime(2026, 7, 1, 9, tzinfo=paris).utcoffset(), timedelta(hours=2))
    check(5, "Paris is UTC+1 in January", datetime(2026, 1, 15, 9, tzinfo=paris).utcoffset(), timedelta(hours=1))
    check(5, "astimezone converts UTC to Paris",
          datetime(2026, 7, 1, 7, tzinfo=timezone.utc).astimezone(paris).hour, 9)
except Exception as e:  # no tz database (Windows without tzdata)
    check(5, "zoneinfo has a timezone database", f"{type(e).__name__}: {e}", "available")
info = time.get_clock_info("perf_counter")
check(5, "perf_counter is monotonic and not adjustable", (info.monotonic, info.adjustable), (True, False))
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    naive = datetime.utcnow()
check(5, "utcnow() returns a naive datetime", naive.tzinfo, None)
check(5, "utcnow() is deprecated (3.12+)",
      any(issubclass(w.category, DeprecationWarning) for w in caught), sys.version_info >= (3, 12))


# ── slide 6 · collections ─────────────────────────────────────────────────
check(6, "Counter counts", Counter("abracadabra")["a"], 5)
check(6, "defaultdict creates the missing key", defaultdict(list)["missing"], [])
Point = namedtuple("Point", "x y")
check(6, "namedtuple has field names", Point(1, 2).y, 2)
last = deque(maxlen=3)
for x in [1, 2, 3, 4, 5]:
    last.append(x)
check(6, "deque(maxlen=3) keeps the last three", repr(last), "deque([3, 4, 5], maxlen=3)")
q = deque([1, 2, 3])
check(6, "popleft takes from the front", (q.popleft(), list(q)), (1, [2, 3]))
check(6, "plain dict keeps insertion order", list({"b": 1, "a": 2}), ["b", "a"])
check(6, "plain dict == ignores order", {"a": 1, "b": 2} == {"b": 2, "a": 1}, True)
check(6, "OrderedDict == compares order",
      OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1), False)
od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")
check(6, "move_to_end", list(od), ["b", "c", "a"])


# ── slide 7 · itertools ───────────────────────────────────────────────────
check(7, "islice(count(10, 5), 4)", list(islice(count(10, 5), 4)), [10, 15, 20, 25])
check(7, "combinations('ABC', 2)", list(combinations("ABC", 2)), [("A", "B"), ("A", "C"), ("B", "C")])
it = combinations("ABC", 2)
check(7, "an iterator is consumed once", (len(list(it)), list(it)), (3, []))
check(7, "chain", list(chain([1, 2], [3])), [1, 2, 3])
check(7, "takewhile stops at the first failure", list(takewhile(lambda x: x < 3, [1, 2, 3, 1])), [1, 2])
check(7, "all four families exist",
      all(hasattr(itertools, n) for n in ["count", "cycle", "repeat", "product", "permutations",
                                          "combinations", "chain", "islice", "takewhile", "filterfalse"]), True)


# ── slide 8 · math, random, statistics (the PLANT) ────────────────────────
def dice():
    random.seed(42)
    return [random.randint(1, 6) for _ in range(5)]


check(8, "seed 42 rolls 6 1 1 6 3", dice(), [6, 1, 1, 6, 3])
check(8, "and again, the same", dice(), [6, 1, 1, 6, 3])
check(8, "0.1 + 0.2 == 0.3 is False", 0.1 + 0.2 == 0.3, False)
check(8, "math.isclose is True", math.isclose(0.1 + 0.2, 0.3), True)
check(8, "median of 13.16, 5.5, 23.62", statistics.median([13.16, 5.5, 23.62]), 13.16)
check(8, "mean and stdev exist", (callable(statistics.mean), callable(statistics.stdev)), (True, True))


# ── slide 9 · decimal: money without rounding errors ─────────────────────
total = 0
for _ in range(10):
    total += 0.10
check(9, "ten += 0.10 in floats", total, 0.9999999999999999)
check(9, "Decimal('0.10') * 10", repr(Decimal("0.10") * 10), "Decimal('1.00')")
check(9, "Decimal('1.00') equals 1", Decimal("0.10") * 10 == 1, True)

# The first video's script, exactly: float += per category, then :.2f.
CSV = Path(__file__).resolve().parent.parent / "00-premier-script" / "depenses_janvier.csv"
f_tot, d_tot = {}, {}
with open(CSV) as fh:
    for row in csv.DictReader(fh):
        cat = row["categorie"]
        f_tot[cat] = f_tot.get(cat, 0) + float(row["montant"])
        d_tot[cat] = d_tot.get(cat, Decimal(0)) + Decimal(row["montant"])
check(9, "Restaurant as a float is 880.4100000000003", repr(f_tot["Restaurant"]), "880.4100000000003")
check(9, ":.2f hid it as 880.41", f"{f_tot['Restaurant']:.2f}", "880.41")
check(9, "Restaurant as Decimal is exactly 880.41", d_tot["Restaurant"], Decimal("880.41"))
check(9, "quantize rounds half to even: 13.16", Decimal("13.165").quantize(Decimal("0.01")), Decimal("13.16"))
check(9, "ROUND_HALF_UP: 13.17",
      Decimal("13.165").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), Decimal("13.17"))
check(9, "Decimal(0.1) carries 55 decimals of float error", len(str(Decimal(0.1)).split(".")[1]), 55)
check(9, "sum() of floats compensates (3.12+)", sum([0.1] * 10) == 1.0, sys.version_info >= (3, 12))
check(9, "Fraction keeps tenths exact; float does not",
      (Fraction(1, 10) * 3 == Fraction(3, 10), 0.1 * 3 == 0.3), (True, False))


# ── slide 10 · re: match, search, findall ──────────────────────────────────
check(10, "match is anchored: None", re.match(r"\d+", "Total: 42"), None)
check(10, "search scans: '42'", re.search(r"\d+", "Total: 42").group(), "42")
check(10, "findall amounts", re.findall(r"\d+\.\d+", "13.16 et 5.50"), ["13.16", "5.50"])
check(10, '"\\b" is a backspace', "\b", "\x08")
check(10, 'r"\\b" reaches re intact', len(r"\b"), 2)
check(10, "re.IGNORECASE ignores case", bool(re.search(r"total", "TOTAL: 42", re.IGNORECASE)), True)
check(10, "a compiled pattern has the same methods", re.compile(r"\d+").findall("13 et 5"), ["13", "5"])
check(10, "word boundary works only with the raw string",
      (bool(re.search(r"\bet\b", "13.16 et 5.50")), bool(re.search("\bet\b", "13.16 et 5.50"))), (True, False))


# ── slide 11 · re: groups and sub ─────────────────────────────────────────
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "paid 2026-01-31")
check(11, "groups 1 and 3", (m.group(1), m.group(3)), ("2026", "31"))
check(11, "sub reorders with back-references",
      re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", "2026-01-31"), "31/01/2026")
check(11, "named group by key", re.search(r"(?P<year>\d{4})", "paid 2026-01-31")["year"], "2026")


# ── slide 12 · os, sys, subprocess ────────────────────────────────────────
r = subprocess.run([sys.executable, "-c", "print(6 * 7)"], capture_output=True, text=True, check=True)
check(12, "run captures '42\\n'", r.stdout, "42\n")
check(12, "check=True raises on a non-zero exit",
      raises(lambda: subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True)).split(":")[0],
      "CalledProcessError")
check(12, "without check, the failure is only a return code",
      subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"]).returncode, 3)
if os.name == "posix":
    check(12, "shell=True: the ; starts a second command",
          subprocess.run("echo a; echo b", shell=True, capture_output=True, text=True).stdout, "a\nb\n")
    check(12, "a list keeps the ; inside one argument",
          subprocess.run(["echo", "a; echo b"], capture_output=True, text=True).stdout, "a; echo b\n")
check(12, "sys has argv, exit, path, executable",
      all(hasattr(sys, n) for n in ["argv", "exit", "path", "executable"]), True)
check(12, "os has environ and getcwd", (hasattr(os, "environ"), callable(os.getcwd)), (True, True))


# ── slide 13 · shutil & archives ──────────────────────────────────────────
work = TMP / "shutil"
(work / "data").mkdir(parents=True)
(work / "backup").mkdir()
(work / "archive").mkdir()
src = work / "data" / "depenses.csv"
src.write_text("date,montant\n2026-01-01,13.16\n")
os.utime(src, (1_767_225_600, 1_767_225_600))  # 2026-01-01, ZIP needs >= 1980
copied = Path(shutil.copy2(src, work / "backup"))
check(13, "copy2 into a folder keeps the name", copied, work / "backup" / "depenses.csv")
check(13, "copy2 keeps the timestamp", os.path.getmtime(copied), 1_767_225_600.0)
(work / "export.csv").write_text("x")
shutil.move(work / "export.csv", work / "archive")
check(13, "move puts it in the folder", ((work / "archive" / "export.csv").exists(), (work / "export.csv").exists()),
      (True, False))
made = Path(shutil.make_archive(str(work / "janvier"), "zip", work / "data"))
check(13, "make_archive creates janvier.zip", made.name, "janvier.zip")
check(13, "the zip holds the folder's files", zipfile.ZipFile(made).namelist(), ["depenses.csv"])
with gzip.open(work / "log.csv.gz", "wt") as fh:
    fh.write("date,montant\n2026-01-01,13.16\n")
with gzip.open(work / "log.csv.gz", "rt") as fh:
    check(13, "gzip.open 'rt' reads lines like a text file", [line.strip() for line in fh],
          ["date,montant", "2026-01-01,13.16"])
shutil.rmtree(work / "backup")
check(13, "rmtree removes the whole tree", (work / "backup").exists(), False)


# ── slide 14 · argparse ───────────────────────────────────────────────────
def parser():
    p = argparse.ArgumentParser(prog="depenses.py")  # the prog a script named depenses.py gets
    p.add_argument("--top", type=int, default=5)
    return p


def parse(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            return parser().parse_args(argv), None, out.getvalue(), err.getvalue()
        except SystemExit as e:
            return None, e.code, out.getvalue(), err.getvalue()


_, code, _, err = parse(["--top", "trois"])
check(14, "bad value: exact message",
      err, "usage: depenses.py [-h] [--top TOP]\n"
           "depenses.py: error: argument --top: invalid int value: 'trois'\n")
check(14, "bad value: exit status 2", code, 2)
_, code, out, _ = parse(["--help"])
check(14, "--help is generated", ("-h, --help" in out, "--top TOP" in out, code), (True, True, 0))
check(14, "default is 5, an int", parse([])[0].top, 5)
check(14, "'--top 3' arrives as int 3", parse(["--top", "3"])[0].top, 3)
check(14, "heapq.nlargest gives the top three", heapq.nlargest(3, [5, 1, 8, 3, 9]), [9, 8, 5])


# ── slide 15 · configparser ───────────────────────────────────────────────
ini = TMP / "app.ini"
ini.write_text("[database]\npath = depenses.db\ntimeout = 30\n"
               "[flags]\na = yes\nb = on\nc = true\nd = 1\n")
cfg = configparser.ConfigParser()
cfg.read(ini)
check(15, "values come back as strings", cfg["database"]["timeout"], "30")
check(15, "getint converts", cfg.getint("database", "timeout"), 30)
check(15, "getboolean reads yes, on, true, 1", [cfg.getboolean("flags", k) for k in "abcd"], [True] * 4)
check(15, "read() of a missing file raises nothing, returns []", configparser.ConfigParser().read(TMP / "absent.ini"), [])
toml = TMP / "pyproject.toml"
toml.write_text('[tool.app]\ntimeout = 30\n')
with open(toml, "rb") as fh:
    check(15, "tomllib keeps TOML's types", tomllib.load(fh)["tool"]["app"]["timeout"], 30)
check(15, "tomllib needs a binary file",
      raises(lambda: tomllib.load(open(toml))).split(":")[0], "TypeError")
check(15, "tomllib only reads", (hasattr(tomllib, "dump"), hasattr(tomllib, "dumps")), (False, False))


# ── slide 16 · sqlite3 ────────────────────────────────────────────────────
con = sqlite3.connect(":memory:")
con.execute("create table depenses (description text, categorie text)")
con.executemany("insert into depenses values (?, ?)",
                [("La Fontaine", "Restaurant"), ("Carrefour Market", "Courses"), ("Amazon Prime", "Abonnements")])
x = "Loisirs' OR '1'='1"
check(16, "f-string query returns the whole table",
      len(con.execute(f"select * from depenses where categorie = '{x}'").fetchall()), 3)
check(16, "placeholder query returns nothing",
      len(con.execute("select * from depenses where categorie = ?", (x,)).fetchall()), 0)

db = TMP / "depenses.db"
con = sqlite3.connect(db)
con.execute("create table depenses (description text, categorie text)")
with con:
    con.execute("insert into depenses values (?, ?)", ("La Fontaine", "Restaurant"))
check(16, "with con: commits on success",
      sqlite3.connect(db).execute("select count(*) from depenses").fetchone()[0], 1)


def _fails_inside():
    with con:
        con.execute("insert into depenses values (?, ?)", ("Carrefour Market", "Courses"))
        raise RuntimeError("boom")


raises(_fails_inside)
check(16, "with con: rolls back on an exception",
      sqlite3.connect(db).execute("select count(*) from depenses").fetchone()[0], 1)
check(16, "with con: does not close the connection",
      raises(lambda: con.execute("select 1").fetchone()), "<no exception>")
con.close()
con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row
con.execute("create table depenses (description text, categorie text)")
con.execute("insert into depenses values (?, ?)", ("La Fontaine", "Restaurant"))
check(16, "sqlite3.Row reads by column name", con.execute("select * from depenses").fetchone()["categorie"],
      "Restaurant")
con.close()


# ── slide 17 · logging levels ─────────────────────────────────────────────
out, err = child("import logging; logging.info('fichier chargé'); logging.warning('disque presque plein')")
check(17, "info is silent, warning prints", (out, err), ("", "WARNING:root:disque presque plein\n"))
check(17, "the five levels",
      [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL], [10, 20, 30, 40, 50])
out, _ = child("import logging; print(logging.getLogger().level)")
check(17, "the default threshold is WARNING", out.strip(), "30")
check(17, "getLogger(__name__) is named after the module",
      logging.getLogger("depenses.import").name, "depenses.import")


# ── slide 18 · handlers, formatters, rotation ─────────────────────────────
log_path = TMP / "app.log"
h = RotatingFileHandler(log_path, maxBytes=200, backupCount=3)
h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
lg = logging.getLogger("nl.rotation")
lg.propagate = False
lg.addHandler(h)
lg.setLevel(logging.INFO)
for i in range(100):
    lg.info("line %d of the rotation check", i)
h.close()
check(18, "rotation keeps app.log plus .1 to .3, deletes older",
      sorted(p.name for p in TMP.glob("app.log*")), ["app.log", "app.log.1", "app.log.2", "app.log.3"])
out, _ = child("import logging; logging.basicConfig(level='INFO'); print(logging.getLogger().level)")
check(18, "basicConfig accepts level='INFO'", out.strip(), "20")
out, _ = child("import logging; logging.getLogger().addHandler(logging.StreamHandler());"
               "logging.basicConfig(level='DEBUG'); print(logging.getLogger().level)")
check(18, "basicConfig does nothing if a handler exists", out.strip(), "30")
out, _ = child("import logging; logging.getLogger().addHandler(logging.StreamHandler());"
               "logging.basicConfig(level='DEBUG', force=True); print(logging.getLogger().level)")
check(18, "... unless force=True", out.strip(), "10")


# ── slide 19 · hashlib & secrets (the PAYOFF) ─────────────────────────────
def token_from_random():
    random.seed(42)
    return f"{random.getrandbits(128):032x}"


check(19, "seeded random token", token_from_random(), "bdd640fb06671ad11c80317fa3b1799d")
check(19, "replayed exactly", token_from_random(), "bdd640fb06671ad11c80317fa3b1799d")
check(19, "token_hex(16) is 32 characters", len(secrets.token_hex(16)), 32)
check(19, "two secrets tokens differ", secrets.token_hex(16) != secrets.token_hex(16), True)
check(19, "sha256 hexdigest is 64 hex characters", len(hashlib.sha256(b"noonlabs").hexdigest()), 64)
check(19, "same bytes, same digest", hashlib.sha256(b"noonlabs").hexdigest(),
      "5a41e9d1f5b26655b06d90ab413fc5175ba06fad686af1acfddb44f36a2a278c")
a, b = hashlib.sha256(b"noonlabs").hexdigest(), hashlib.sha256(b"noonlabt").hexdigest()
check(19, "one byte changes the digest completely", sum(x == y for x, y in zip(a, b)) < 16, True)
check(19, "hashlib.scrypt is available", hasattr(hashlib, "scrypt"), True)
check(19, "secrets.compare_digest compares tokens",
      (secrets.compare_digest("abc", "abc"), secrets.compare_digest("abc", "abd")), (True, False))


# ── slide 20 · pitfalls ───────────────────────────────────────────────────
check(20, "secrets.token_urlsafe exists", callable(secrets.token_urlsafe), True)


shutil.rmtree(TMP, ignore_errors=True)

print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
