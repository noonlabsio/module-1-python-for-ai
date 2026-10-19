"""Chapter 01 — re-run every fact that appears on a slide or in a note.

Most of this chapter is tooling, not Python behaviour, so most checks drive
uv through subprocess in a throwaway directory: the exact commands the notes
say to type, and the files and output they say will appear. Python itself
comes from uv, so the recording machine needs uv and Python 3.14
(`uv python install 3.14`).

    python3 01_env_setup/verify-facts.py              # offline checks
    python3 01_env_setup/verify-facts.py --network    # + slide 13 (uv add pandas)

Run it on the recording machine before recording. uv changes its defaults
between minor versions (0.12 made `uv init` create a packaged src layout,
hence `--no-package` on slide 12), so a check here can drift while the
slides stay the same.

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 20-slide deck: 01 cover, 02 divider, 03-19
content, 20 closing card.

Stdlib only.
"""

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FAILS = []
NETWORK = "--network" in sys.argv


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


def printed(fn):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


def uv(*args, cwd):
    return subprocess.run(["uv", *args], cwd=cwd, capture_output=True, text=True)


print(f"CPython {sys.version}\n")

if shutil.which("uv") is None:
    sys.exit("uv is not on PATH: slides 11-19 cannot be checked. Install uv first.")
print(f"{uv('--version', cwd='.').stdout.strip()}\n")


# ── slide 05 · what you write, what the interpreter does ──────────────────
check(5, 'print("Hello, World!") prints Hello, World!', printed(lambda: print("Hello, World!")), "Hello, World!\n")


# ── slide 11 · uv python install 3.14 ─────────────────────────────────────
found = uv("python", "find", "3.14", cwd=".")
check(11, "a Python 3.14 is installed for uv", found.returncode, 0)


# ── slide 14 · the REPL demo, and the hook for chapter 02 ─────────────────
check(14, ">>> 2 + 3", repr(eval("2 + 3")), "5")
check(14, '>>> "Hello, " + "World!"', repr(eval('"Hello, " + "World!"')), "'Hello, World!'")
check(14, "hook for the types chapter: + between text and a number fails", raises(lambda: "47.20" + 12),
      'TypeError: can only concatenate str (not "int") to str')


with tempfile.TemporaryDirectory() as tmp:
    proj = Path(tmp) / "hello-ai"

    # ── slide 12 · uv init --no-package --python 3.14 hello-ai; uv venv ───
    init = uv("init", "--no-package", "--python", "3.14", "hello-ai", cwd=tmp)
    check(12, "uv init succeeds", init.returncode, 0)
    pyproject = (proj / "pyproject.toml").read_text()
    check(12, ".python-version pins 3.14", (proj / ".python-version").read_text().strip(), "3.14")
    check(12, 'requires-python = ">=3.14"', 'requires-python = ">=3.14"' in pyproject, True)
    check(12, "--no-package: no [build-system], no src/", ("[build-system]" in pyproject, (proj / "src").exists()), (False, False))
    venv = uv("venv", cwd=proj)
    check(12, "uv venv: Creating virtual environment at: .venv", "Creating virtual environment at: .venv" in venv.stderr, True)
    check(12, "uv venv uses CPython 3.14", "Using CPython 3.14." in venv.stderr, True)

    # ── slide 17 · hello.py, run with uv, then the setup checks ───────────
    (proj / "hello.py").write_text('# My first program\nprint("Hello, World!")\nprint("Python is ready.")\n')
    run = uv("run", "hello.py", cwd=proj)
    check(17, "uv run hello.py", run.stdout, "Hello, World!\nPython is ready.\n")
    prefix = uv("run", "python", "-c", "import sys; print(sys.prefix)", cwd=proj).stdout.strip()
    check(17, "sys.prefix ends in hello-ai/.venv", Path(prefix).parts[-2:], ("hello-ai", ".venv"))
    typo = uv("run", "python", "-c", "prnt('Hello, World!')", cwd=proj)
    check(17, "prnt typo: last traceback line", typo.stderr.strip().splitlines()[-1],
          "NameError: name 'prnt' is not defined. Did you mean: 'print'?")

    # ── slide 13 · the diagram: uv lock writes uv.lock, uv sync builds .venv
    demo = Path(tmp) / "lock-demo"
    uv("init", "--no-package", "--python", "3.14", "lock-demo", cwd=tmp)
    uv("lock", cwd=demo)
    check(13, "uv lock: uv.lock written, no .venv yet", ((demo / "uv.lock").is_file(), (demo / ".venv").exists()), (True, False))
    uv("sync", cwd=demo)
    check(13, "uv sync: .venv built from uv.lock", (demo / ".venv").is_dir(), True)

    # ── slide 13 · uv add pandas (needs the network) ──────────────────────
    if NETWORK:
        add = uv("add", "pandas", cwd=proj)
        check(13, "uv add pandas succeeds", add.returncode, 0)
        pyproject = (proj / "pyproject.toml").read_text()
        check(13, 'pyproject gets "pandas>=3.0.6", the version on the slide', '    "pandas>=3.0.6",' in pyproject, True)
        lock = (proj / "uv.lock").read_text()
        check(13, "uv.lock lists tzdata, for Windows only",
              '{ name = "tzdata", marker = "sys_platform == \'emscripten\' or sys_platform == \'win32\'" }' in lock, True)
        version = uv("run", "python", "-c", "import pandas; print(pandas.__version__)", cwd=proj).stdout.strip()
        check(12, "diagram: hello-ai's .venv holds pandas 3.0.6", version, "3.0.6")
        if sys.platform != "win32":
            freeze = uv("pip", "freeze", cwd=proj).stdout
            check(13, "pip freeze here has pandas but not tzdata",
                  ("pandas==" in freeze, "tzdata" in freeze), (True, False))
        old = Path(tmp) / "old-report"
        uv("init", "--no-package", "--python", "3.12", "old-report", cwd=tmp)
        check(12, "diagram: old-report on Python 3.12 takes pandas 2.2.3", uv("add", "pandas==2.2.3", cwd=old).returncode, 0)
    else:
        print("[skip]  s12, s13 uv add pandas: re-run with --network")

    # ── slide 18 · delete .venv, rebuild it from the lock file ────────────
    check(18, ".venv is in the .gitignore uv init wrote", ".venv" in (proj / ".gitignore").read_text().split(), True)
    uv("lock", cwd=proj)
    check(18, "uv.lock exists", (proj / "uv.lock").is_file(), True)
    shutil.rmtree(proj / ".venv")
    sync = uv("sync", "--locked", cwd=proj)
    check(18, "uv sync --locked rebuilds .venv", (sync.returncode, (proj / ".venv").is_dir()), (0, True))
    if NETWORK:
        rebuilt = uv("run", "python", "-c", "import pandas; print(pandas.__version__)", cwd=proj).stdout.strip()
        check(18, "diagram: the rebuilt .venv has the same pandas", rebuilt, version)
    check(18, "uv run hello.py works again", uv("run", "hello.py", cwd=proj).stdout, "Hello, World!\nPython is ready.\n")
    stale = pyproject.replace('requires-python = ">=3.14"', 'requires-python = ">=3.13"')
    (proj / "pyproject.toml").write_text(stale)
    check(18, "--locked refuses a lock that no longer matches", uv("sync", "--locked", cwd=proj).returncode != 0, True)


print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
