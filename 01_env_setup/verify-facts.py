"""Chapter 01 — re-run every fact that appears on a slide or in a note.

Most of this chapter is tooling, not Python behaviour, so most checks drive
uv through subprocess in a throwaway directory: the exact commands the notes
say to type, and the files and output they say will appear. Python itself
comes from uv, so the recording machine needs uv and Python 3.14
(`uv python install 3.14`).

    python3 01_env_setup/verify-facts.py              # offline checks
    python3 01_env_setup/verify-facts.py --network    # + everything that installs a package

The network checks are the ones that matter for the rebuild demos: a rebuilt
environment only counts once a non-stdlib import (pandas, rich) works in it.
Offline, those checks are skipped and say so.

Run it on the recording machine before recording. uv changes its defaults
between minor versions (0.12 made `uv init` create a packaged src layout,
hence `--no-package` on slide 12), so a check here can drift while the
slides stay the same.

Exit code is 1 if anything drifted. On DRIFT, fix the slide, never the check.
Slide numbers refer to the 21-slide deck: 01 cover, 02 divider, 03-20
content, 21 closing card.

Stdlib only.
"""

import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import tomllib
import urllib.request
from pathlib import Path

FAILS = []
NETWORK = "--network" in sys.argv
PANDAS_VERSION = 'import pandas; print(pandas.__version__)'   # slide 18, typed as is
REPO = Path(__file__).resolve().parent.parent


def check(slide, label, actual, expected):
    ok = actual == expected
    if not ok:
        FAILS.append((slide, label))
    print(f"{'[ok]   ' if ok else '[DRIFT]'} s{slide:02} {label}")
    if not ok:
        print(f"         slide says:  {expected!r}")
        print(f"         python says: {actual!r}")


def skip(slide, label):
    print(f"[skip]  s{slide:02} {label}: re-run with --network")


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


def last_line(proc):
    lines = proc.stderr.strip().splitlines()
    return lines[-1] if lines else ""


def new_project(tmp, name, python="3.14"):
    uv("init", "--no-package", "--python", python, name, cwd=tmp)
    return Path(tmp) / name


def fetch(url):
    """The text at url, or the error, so a network failure reads as drift.

    Sent as curl, the client the slide uses: astral.sh answers Python's
    default user agent with 403 Forbidden.
    """
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.5.0"}), timeout=20) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        return f"<{type(e).__name__}: {e}>"


def curriculum_section(number):
    """The body of '### NN · Title' in the curriculum, up to the next ### heading."""
    text = (REPO / "curriculum-module-1.md").read_text()
    start = text.index(f"### {number:02} ")
    end = text.find("\n### ", start + 1)
    return text[start:end if end != -1 else None]


def lock_packages(proj):
    return {p["name"]: p for p in tomllib.loads((proj / "uv.lock").read_text())["package"]}


# A notebook kernel, driven the way the slide 16 demo drives it: run cell 1,
# run cell 2, edit cell 1 without running it, run cell 2 again, then Restart
# and Run All. Runs inside the project, so the kernel is .venv's Python.
KERNEL_DEMO = r'''
import json
from jupyter_client.manager import start_new_kernel
km, kc = start_new_kernel(kernel_name="python3")
def cell(code):
    out = []
    kc.execute_interactive(code, timeout=60, output_hook=lambda m: out.append(m["content"]["text"]) if m["msg_type"] == "stream" else None)
    return "".join(out)
seen = {"prefix": cell("import sys; print(sys.prefix)").strip()}
cell("x = 1"); seen["run 2"] = cell("print(x)")
seen["edited, not run"] = cell("print(x)")              # cell 1 now says x = 10 on the page
km.restart_kernel(now=True); kc.wait_for_ready(timeout=60)
cell("x = 10"); seen["restart, run all"] = cell("print(x)")
kc.stop_channels(); km.shutdown_kernel(now=True)
print(json.dumps(seen))
'''


print(f"CPython {sys.version}\n")

if shutil.which("uv") is None:
    sys.exit("uv is not on PATH: slides 10-20 cannot be checked. Install uv first.")
print(f"{uv('--version', cwd='.').stdout.strip()}\n")


# ── slides 03-04 · what the course covers: Polars in chapter 13, NumPy in 12
section13 = curriculum_section(13)
check(3, "the curriculum covers Polars, in chapter 13", ("Polars" in section13, "Polars" in (REPO / "13-pandas-and-modern-dataframe-libraries" / "slides.md").read_text()), (True, True))
check(4, 'chapter 13 is "pandas & Polars": a dataframe-libraries chapter', section13.splitlines()[0], "### 13 · Pandas & Modern Dataframe Libraries")
check(4, "chapters 07-12 end with NumPy", curriculum_section(12).splitlines()[0], "### 12 · NumPy")


# ── slide 05 · what you write, what the interpreter does ──────────────────
check(5, 'print("Hello, World!") prints Hello, World!', printed(lambda: print("Hello, World!")), "Hello, World!\n")


# ── slide 11 · uv python install 3.14 ─────────────────────────────────────
check(11, "a Python 3.14 is installed for uv", uv("python", "find", "3.14", cwd=".").returncode, 0)


# ── slide 15 · the REPL demo, and the hook for the types chapter ──────────
check(15, ">>> 2 + 3", repr(eval("2 + 3")), "5")
check(15, '>>> "Hello, " + "World!"', repr(eval('"Hello, " + "World!"')), "'Hello, World!'")
check(15, "hook for the types chapter: + between text and a number fails", raises(lambda: "47.20" + 12),
      'TypeError: can only concatenate str (not "int") to str')


with tempfile.TemporaryDirectory() as tmp:

    # ── slide 12 · uv init --no-package --python 3.14 hello-ai; uv venv ───
    init = uv("init", "--no-package", "--python", "3.14", "hello-ai", cwd=tmp)
    proj = Path(tmp) / "hello-ai"
    check(12, "uv init succeeds", init.returncode, 0)
    pyproject = (proj / "pyproject.toml").read_text()
    check(12, ".python-version pins 3.14", (proj / ".python-version").read_text().strip(), "3.14")
    check(12, 'requires-python = ">=3.14"', 'requires-python = ">=3.14"' in pyproject, True)
    check(12, "--no-package: no [build-system], no src/", ("[build-system]" in pyproject, (proj / "src").exists()), (False, False))
    venv = uv("venv", cwd=proj)
    check(12, "uv venv: Creating virtual environment at: .venv", "Creating virtual environment at: .venv" in venv.stderr, True)
    check(12, "uv venv uses CPython 3.14", "Using CPython 3.14." in venv.stderr, True)

    # slide 12 note: uv run, uv sync and uv add create .venv when it is missing
    auto_run = new_project(tmp, "auto-run")
    uv("run", "python", "-c", "pass", cwd=auto_run)
    check(12, "uv run creates a missing .venv", (auto_run / ".venv").is_dir(), True)
    auto_sync = new_project(tmp, "auto-sync")
    uv("lock", cwd=auto_sync)
    check(14, "uv lock: uv.lock written, no .venv yet", ((auto_sync / "uv.lock").is_file(), (auto_sync / ".venv").exists()), (True, False))
    uv("sync", cwd=auto_sync)
    check(12, "uv sync creates a missing .venv (slide 14: built from uv.lock)", (auto_sync / ".venv").is_dir(), True)

    # ── slide 13 · hello.py, run with uv, then the setup checks ───────────
    (proj / "hello.py").write_text('# My first program\nprint("Hello, World!")\nprint("Python is ready.")\n')
    check(13, "uv run hello.py", uv("run", "hello.py", cwd=proj).stdout, "Hello, World!\nPython is ready.\n")
    prefix = uv("run", "python", "-c", "import sys; print(sys.prefix)", cwd=proj).stdout.strip()
    check(13, "sys.prefix ends in hello-ai/.venv", Path(prefix).parts[-2:], ("hello-ai", ".venv"))
    check(13, "prnt typo: last traceback line", last_line(uv("run", "python", "-c", "prnt('Hello, World!')", cwd=proj)),
          "NameError: name 'prnt' is not defined. Did you mean: 'print'?")

    # ── slide 19 · symptom 1, in a project that does not have pandas ──────
    check(19, "No module named 'pandas'", last_line(uv("run", "python", "-c", "import pandas", cwd=proj)),
          "ModuleNotFoundError: No module named 'pandas'")

    # ── slide 18 · offline part: what goes into Git, what --locked refuses ─
    check(18, ".venv is in the .gitignore uv init wrote", ".venv" in (proj / ".gitignore").read_text().split(), True)
    stale = new_project(tmp, "stale")
    uv("lock", cwd=stale)
    toml = (stale / "pyproject.toml").read_text()
    (stale / "pyproject.toml").write_text(toml.replace('requires-python = ">=3.14"', 'requires-python = ">=3.13"'))
    check(18, "--locked refuses a lock that no longer matches pyproject.toml", uv("sync", "--locked", cwd=stale).returncode != 0, True)

    if not NETWORK:
        for slide, label in [(10, "ready-made wheels; Miniforge uses conda-forge"), (11, "the install line downloads a shell script"), (12, "auto .venv on uv add; the diagram's versions"),
                             (14, "uv add pandas, tzdata pin and marker"), (16, "ipykernel, --with, the kernel demo"),
                             (18, "rebuild with a pandas import"), (19, "uv add records; .venv size"), (20, "the challenge")]:
            skip(slide, label)
    else:
        # ── slide 14 · uv add pandas ──────────────────────────────────────
        check(14, "uv add pandas succeeds", uv("add", "pandas", cwd=proj).returncode, 0)
        pyproject = (proj / "pyproject.toml").read_text()
        check(14, 'pyproject gets "pandas>=3.0.6", the version on the slide', '    "pandas>=3.0.6",' in pyproject, True)
        lock = lock_packages(proj)
        check(19, "uv add records pandas in pyproject.toml and uv.lock", ('"pandas>=' in pyproject, "pandas" in lock), (True, True))

        # slide 14 · tzdata is Windows-only for pandas, pinned by uv.lock, not by a Linux pip freeze
        requires = json.loads(uv("run", "python", "-c", "import importlib.metadata as m, json; print(json.dumps(m.requires('pandas')))", cwd=proj).stdout)
        check(14, 'pandas metadata: tzdata; sys_platform == "win32"', 'tzdata; sys_platform == "win32"' in requires, True)
        tz_dep = [d for d in lock["pandas"]["dependencies"] if d["name"] == "tzdata"]
        check(14, "uv.lock: pandas needs tzdata on Windows only", [d.get("marker") for d in tz_dep],
              ["sys_platform == 'emscripten' or sys_platform == 'win32'"])
        check(14, "uv.lock pins one tzdata version, for every platform", bool(lock["tzdata"].get("version")), True)
        if sys.platform != "win32":
            freeze = uv("pip", "freeze", cwd=proj).stdout
            check(14, "pip freeze on this machine: pandas pinned, tzdata absent", ("pandas==" in freeze, "tzdata" in freeze), (True, False))
            req = Path(tmp) / "requirements.txt"
            req.write_text(freeze)
            win = uv("pip", "compile", str(req), "--python-platform", "x86_64-pc-windows-msvc", "--python-version", "3.14",
                     "--no-header", "--no-annotate", "-q", cwd=tmp).stdout
            check(14, "on Windows that file still pulls tzdata, at a version it never pinned",
                  ("tzdata==" in win, "tzdata" in freeze), (True, False))

        # slide 10 · every dependency is a ready-made wheel, for the three desktop platforms
        missing = []
        for name, pkg in lock.items():
            if name == "hello-ai":
                continue
            wheels = [Path(w["url"]).name for w in pkg.get("wheels", [])]
            if any("-none-any.whl" in w for w in wheels):
                continue
            for tag in ("win_amd64", "macosx", "manylinux"):
                if not any("cp314" in w and tag in w for w in wheels):
                    missing.append(f"{name}:{tag}")
        check(10, "every dependency has a cp314 wheel for Windows, macOS, Linux (or a pure-Python one)", missing, [])

        # slide 10 note · Miniforge's only channel is conda-forge
        readme = fetch("https://raw.githubusercontent.com/conda-forge/miniforge/main/README.md")
        check(10, "Miniforge: conda-forge is the default (and only) channel",
              "channel is set as the default (and only) channel" in readme and "conda-forge" in readme, True)

        # slide 11 · `curl … | sh` downloads a shell script and runs it; `| less` shows it instead
        check(11, "astral.sh/uv/install.sh is a shell script", fetch("https://astral.sh/uv/install.sh").splitlines()[0], "#!/bin/sh")

        # slide 12 · the diagram's two projects, and uv add creating .venv
        check(12, "diagram: hello-ai's .venv holds pandas 3.0.6", uv("run", "python", "-c", PANDAS_VERSION, cwd=proj).stdout.strip(), "3.0.6")
        old = new_project(tmp, "old-report", python="3.12")
        check(12, "diagram: old-report on Python 3.12 takes pandas 2.2.3", uv("add", "pandas==2.2.3", cwd=old).returncode, 0)
        auto_add = new_project(tmp, "auto-add")
        uv("add", "iniconfig", cwd=auto_add)
        check(12, "uv add creates a missing .venv", (auto_add / ".venv").is_dir(), True)

        # slide 19 · symptom 3: the size of a .venv with pandas
        size = sum(f.stat().st_size for f in (proj / ".venv").rglob("*") if f.is_file() and not f.is_symlink())
        check(19, "a .venv with pandas is 100+ MB", size >= 100_000_000, True)

        # ── slide 16 · Jupyter ─────────────────────────────────────────────
        check(16, "uv add --dev ipykernel", uv("add", "--dev", "ipykernel", cwd=proj).returncode, 0)
        check(16, "ipykernel lands in the dev group", tomllib.loads((proj / "pyproject.toml").read_text())
              .get("dependency-groups", {}).get("dev", [""])[0].startswith("ipykernel"), True)
        script = Path(tmp) / "kernel_demo.py"
        script.write_text(KERNEL_DEMO)
        demo = uv("run", "python", str(script), cwd=proj)
        seen = json.loads(demo.stdout.strip().splitlines()[-1]) if demo.returncode == 0 else {}
        check(16, "the kernel is .venv's Python", Path(seen.get("prefix", "")).parts[-2:], ("hello-ai", ".venv"))
        check(16, "x = 1, then print(x)", seen.get("run 2"), "1\n")
        check(16, "cell 1 edited to x = 10 but not run: print(x) still says 1", seen.get("edited, not run"), "1\n")
        check(16, "Restart, then Run All: print(x) says 10", seen.get("restart, run all"), "10\n")
        before = (proj / "pyproject.toml").read_text()
        with_run = uv("run", "--with", "iniconfig", "python", "-c", "import iniconfig", cwd=proj)
        check(16, "--with: the package imports during the command", with_run.returncode, 0)
        check(16, "--with: pyproject.toml unchanged, .venv still without it",
              ((proj / "pyproject.toml").read_text() == before, last_line(uv("run", "python", "-c", "import iniconfig", cwd=proj))),
              (True, "ModuleNotFoundError: No module named 'iniconfig'"))

        # ── slide 18 · the rebuild, proved by a non-stdlib import ──────────
        check(18, "before the delete: pandas 3.0.6", uv("run", "python", "-c", PANDAS_VERSION, cwd=proj).stdout.strip(), "3.0.6")
        shutil.rmtree(proj / ".venv")
        check(18, "after the delete: no .venv", (proj / ".venv").exists(), False)
        sync = uv("sync", "--locked", cwd=proj)
        check(18, "uv sync --locked rebuilds .venv", (sync.returncode, (proj / ".venv").is_dir()), (0, True))
        check(18, "after the rebuild: the same pandas 3.0.6", uv("run", "python", "-c", PANDAS_VERSION, cwd=proj).stdout.strip(), "3.0.6")

        # ── slide 20 · the challenge, end to end ───────────────────────────
        mine = new_project(tmp, "my-project")
        (mine / "script.py").write_text('print("It runs.")\n')
        check(20, "1-2: a new project runs a script with uv run", uv("run", "script.py", cwd=mine).stdout, "It runs.\n")
        check(20, "3: uv add rich", uv("add", "rich", cwd=mine).returncode, 0)
        check(20, "3: rich is in pyproject.toml and uv.lock",
              ('"rich>=' in (mine / "pyproject.toml").read_text(), "rich" in lock_packages(mine)), (True, True))
        shutil.rmtree(mine / ".venv")
        uv("sync", "--locked", cwd=mine)
        check(20, "4: after the rebuild, rich still imports",
              uv("run", "python", "-c", "import rich; print(rich.__name__)", cwd=mine).stdout.strip(), "rich")


print(f"\n{'ALL FACTS HOLD' if not FAILS else f'{len(FAILS)} DRIFTED — fix the slides:'}")
for slide, label in FAILS:
    print(f"  slide {slide:02}: {label}")
sys.exit(1 if FAILS else 0)
