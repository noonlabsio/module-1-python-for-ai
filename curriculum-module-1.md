## Module I — Fundamentals of Python Programming

**Tagline:** *Master the language of data and AI.*

Covers the core Python language, essential concepts, data structures, object-oriented programming, and an introduction to libraries and frameworks. (Je n'ai pas la pretention de t'apprendre tout Python, mais j'ai selectionne les element essentiels pour te donne la fondation la plus solide que tu as besoin pour travailler entant que DS, ML, wep, AI, ou alors construstruire ton propre project.)

### 01 · Getting Started

- What is Python & why learn it — market context
- Python 3.12+ installation: python.org and Anaconda/Mamba
- Virtual environments intro: venv, conda
- VS Code setup & essential extensions (Pylance, Error Lens)
- Jupyter Notebooks & Google Colab overview
- Running Python: script vs REPL
- Hello, World! and `print()` basics
- Comments and `.py` file structure

### 02 · Syntax & Data Types

- Indentation rules — syntax, not style
- Inline, block comments, and docstrings
- Variables, dynamic typing, naming conventions
- Numeric types: `int`, `float`, `complex`
- Strings: creation, immutability, indexing & slicing
- String methods deep dive
- f-strings: all features incl. `{x=}`, alignment, format specs
- Boolean, comparison & logical operators
- `NoneType` and falsy/truthy values
- Type conversion & casting
- Walrus operator `:=` (Python 3.8+)
- Python keywords reference

### 03 · Control Flow & Loops

- `if` / `elif` / `else` conditionals
- Ternary (conditional) expressions
- Structural pattern matching — `match`/`case` (Python 3.10+)
- `for` loops and the iterable protocol
- `range()` deep dive: start, stop, step
- `while` loops and sentinel patterns
- `break`, `continue`, `pass`
- `else` clause on loops
- Nested loops and time complexity intro
- `enumerate()` for index + value iteration
- `zip()` for parallel iteration

### 04 · Functions & Scope

- Defining functions: `def`, `return`, docstrings
- Positional, keyword, and default arguments
- `*args` and `**kwargs`
- Argument ordering rules
- Lambda (anonymous) functions
- LEGB scope rule: Local → Enclosing → Global → Built-in
- `global` and `nonlocal` keywords
- Type hints basics: `int`, `str`, `Optional`, `List`
- `__name__ == "__main__"` pattern
- Intro to `map()`, `filter()`, `reduce()`

### 05 · Data Structures

- Lists: creation, indexing, slicing, all methods
- List comprehensions with filtering
- Tuples: immutability, unpacking, `namedtuple`
- Dictionaries: creation, access, methods, dict comprehensions
- Sets & frozensets, operations, set comprehensions
- Slicing mastery: step, negative indices, slice objects
- Mutable vs immutable — why it matters
- Python memory model: names, objects, references
- `is` vs `==` (identity vs equality)
- Shallow vs deep copy

### 06 · File I/O & Data Formats

- File opening modes: `r`, `w`, `a`, `rb`, and combinations
- Context manager — `with` statement and why it matters
- Reading: `read()`, `readline()`, `readlines()`, iteration
- Writing: `write()`, `writelines()`, `print(file=)`
- CSV: `csv.reader`, `DictReader`, `csv.writer`, `DictWriter`
- JSON: `loads`/`dumps`, `load`/`dump`, custom encoders
- Binary files and `pickle` (with security warning)
- File system: `os.path` vs `pathlib` (modern approach)
- Temporary files and directories
- Environment variables: `os.getenv` and `python-dotenv`

### 07 · Error Handling & Exceptions

- Python exception hierarchy
- `try` / `except` / `else` / `finally` full structure
- Catching specific exceptions — not bare `except`
- Accessing exception info with `as e`
- Catching multiple exceptions in one clause
- Raising exceptions with `raise`
- Re-raising and exception chaining (`raise … from`)
- Custom exception classes with extra context
- EAFP vs LBYL philosophy
- Best practices and anti-patterns

### 08 · Object-Oriented Programming

- The 4 pillars: encapsulation, inheritance, polymorphism, abstraction
- Class definition, `__init__`, `self` parameter
- Instance vs class attributes and methods
- Encapsulation: public, protected (`_`), private (`__`), name mangling
- `@property` for managed attributes with validation
- Inheritance, `super()`, method overriding
- Multiple inheritance and MRO (C3 linearization)
- Polymorphism and duck typing
- Abstract Base Classes (`abc` module)
- Magic/dunder methods: `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, etc.
- Operator overloading
- `@classmethod` and `@staticmethod`
- Dataclasses (Python 3.7+)

### 09 · Python Standard Library

- `datetime` & `time`: formatting, parsing, timezones, `timedelta`
- `collections`: `Counter`, `deque`, `defaultdict`, `namedtuple`, `OrderedDict`
- `itertools`: infinite, combinatoric, chaining, filtering
- `math`, `random`, `secrets`, `statistics`
- `re`: regular expressions — search, match, findall, groups, sub
- `os`, `sys`, `subprocess`
- `argparse`: command-line argument parsing
- `json`, `csv`, `configparser`
- `sqlite3`: embedded database basics
- `logging`: levels, handlers, formatters, rotation
- `hashlib` & `secrets`: hashing and cryptographic tokens

### 10 · Functional Programming

- Pure functions and immutability
- Imperative vs functional style — side-by-side comparison
- `map()`, `filter()`, `reduce()` deep dive
- Lambda in depth: closures, late binding gotcha
- Generator functions with `yield`
- Generator expressions (lazy evaluation)
- Infinite sequences and pipeline patterns
- Memory efficiency: generators vs lists
- `functools`: `partial`, `wraps`, `lru_cache`, `total_ordering`
- `operator` module: `itemgetter`, `attrgetter`, `methodcaller`
- Function composition patterns

### 11 · Advanced Python

- Function decorators: structure, `@functools.wraps`
- Decorators with arguments (factory pattern)
- Class decorators and the Singleton pattern
- Context managers: `__enter__` / `__exit__` protocol
- `contextlib`: `@contextmanager`, `suppress`
- Descriptors: `__get__`, `__set__`, `__delete__`
- `__getattr__` vs `__getattribute__`
- Metaclasses: `type()`, creating custom metaclasses
- `__slots__` for memory optimization
- `threading`: `Thread`, `Lock`, `Semaphore`, `Event`
- `multiprocessing`: `Pool`, `Queue`, `Process`
- `asyncio`: `async`/`await`, `gather`, `create_task`
- Type hints advanced: `TypeVar`, `Generic`, `Protocol`, `TypedDict`
- Memory management: reference counting, `gc`, `weakref`
- Performance profiling: `cProfile`, `pstats`, `timeit`
- Debugging: `pdb`, `breakpoint()`, VS Code debugger

### 12 · NumPy

- Array creation: `zeros`, `ones`, `eye`, `arange`, `linspace`, `random`
- Array attributes: `shape`, `ndim`, `dtype`, `itemsize`, `nbytes`
- Reshaping, flattening, transpose
- Data types and `astype` conversion
- Basic, fancy, and boolean indexing & slicing
- `np.where` for conditional selection
- Views vs copies — critical distinction
- Element-wise operations and vectorization benefits
- Broadcasting rules and examples
- Aggregation along axes: `sum`, `mean`, `std`, `argmin`/`argmax`
- Linear algebra: `@`, `inv`, `det`, `solve`, `eigvals`
- Random generation with `default_rng`
- Statistical functions

### 13 · Pandas & Modern Dataframe Libraries

**Pandas**

- Series: creation, indexing, attributes
- DataFrame: creation, `info()`, `describe()`
- Data selection: `loc`, `iloc`, boolean indexing, `query()`
- Adding and modifying columns
- Handling missing data: `isnull`, `dropna`, `fillna`, `interpolate`
- Type conversion: `astype`, `to_datetime`, `to_numeric`
- String operations via `.str` accessor
- Renaming, reindexing, `set`/`reset` index
- Removing duplicates
- `apply`, `map`, `transform`
- GroupBy: aggregation, transform, filter
- Pivot tables and crosstab
- Merging: `merge` (SQL-style) and `join` (index-based)
- Concatenation: `concat` vertical and horizontal
- Time series: `DatetimeIndex`, `resample`, `rolling`, `shift`, `pct_change`
- Reading/writing: `read_csv`, `read_json`, `to_csv`, `read_parquet`

**Polars** *(modern columnar DataFrame library)*

- Why Polars: lazy evaluation, columnar format, multithreading, Rust core
- `LazyFrame` vs `DataFrame`; the `.lazy()` / `.collect()` pattern
- Expressions API: `pl.col()`, `pl.lit()`, method chaining
- Filtering, groupby, joins, window functions
- `scan_csv`, `scan_parquet`, `scan_ipc` for out-of-core processing
- Interoperability with Pandas and Arrow
- Performance comparison: when to use Polars vs Pandas

**DuckDB** *(in-process analytical SQL engine)*

- What is DuckDB and why it replaces "do I need Spark?"`
- Running SQL on DataFrames, CSV, Parquet, and JSON directly
- Aggregations and window functions at scale
- Reading from S3 and cloud storage
- Integration with Pandas, Polars, and Arrow
- When DuckDB fits vs Polars vs Spark

### 14 · Data Visualization

- Matplotlib architecture: Figure, Axes, Artist hierarchy
- Common plots: line, scatter, bar, histogram, pie, boxplot
- Subplots grid and GridSpec for complex layouts
- Colors, colormaps, annotations and text
- 3D plotting with `mpl_toolkits`
- Saving figures: PNG, PDF, SVG with dpi settings
- Seaborn: categorical, relational, distribution, matrix plots
- Seaborn styling: themes, contexts, palettes
- Plotly Express: interactive charts in one line
- Plotly customization: `update_layout`, `update_traces`
- Exporting interactive HTML plots

### 15 · Working with APIs

- HTTP methods: GET, POST, PUT, PATCH, DELETE
- Status codes: 2xx, 3xx, 4xx, 5xx
- `requests` library: get, post, headers, params, json, timeout
- Error handling: `raise_for_status`, exception types
- Sessions for connection pooling
- Authentication: API key, Bearer token, Basic auth, OAuth2
- Pagination handling strategies
- Rate limiting and response caching
- Building APIs with Flask: routes, methods, `jsonify`
- Request validation and custom error handlers
- CRUD API example end-to-end
- Intro to FastAPI (modern async alternative)
- MLflow, LanGraph, LangChain, LlamaIndex, Haystack, DSPy, LangGraph, RAGFlow, EmbedChain

### 16 · Testing & Quality

- Why testing matters — and why it saves time
- `unittest`: structure, assertions, setUp/tearDown
- Running and discovering tests
- `pytest`: simpler syntax, plain assert with rich messages
- Fixtures: function, module, and session scope
- Parametrized tests with `@pytest.mark.parametrize`
- TDD cycle: Red → Green → Refactor
- `unittest.mock`: `Mock`, `MagicMock`, `patch` decorator
- `pytest-mock`: mocker fixture, spying on methods
- Test coverage: `pytest-cov`, HTML reports
- CI integration with GitHub Actions

### 17 · Best Practices & Tooling

- PEP 8: naming, layout, imports, line length
- Formatters: Black and isort
- Linters: flake8, pylint, ruff
- Type checkers: mypy and pyright
- Security scanners: bandit and safety
- Pre-commit hooks
- Virtual environments: venv, conda, Poetry, uv
- `requirements.txt` vs `pyproject.toml`
- Git workflow: branching, commit messages, `.gitignore`
- Debugging in practice: `pdb`, `breakpoint()`, VS Code debugger
- Environment variables: `.env` and `python-dotenv`
- Documentation: docstrings, Sphinx, ReadTheDocs
- CI/CD: GitHub Actions full pipeline
- Package publishing: PyPI, twine, build


### 18 . Projects.
Build complete, tested Python tools before introducing model training.
FOUNDATION BUILD
CSV Expense Analyzer
Turn the first useful Python script into a dependable local reporting tool.
BUILDEVIDENCE TO SUBMIT
Parse CSV files with decimal-safe amounts, validate
records, group categories and dates, and export a
clean summary. Add a CLI, configuration and useful
error messages.Deliver a packaged repository, sample
data, README and pytest suite. Check
totals, malformed rows, duplicate
handling and reproducible outputs.
Synthetic bank-style CSV files; no private account data required.
FOUNDATION BUILD
Public Data Collector & EDA Reporter
Collect a public dataset and produce a repeatable descriptive report.
BUILDEVIDENCE TO SUBMIT
Fetch paginated API/CSV data with retries and
caching. Clean types, join reference tables and
generate missing-value, summary-statistic and chart
reports.Deliver a reusable pipeline, data
dictionary and report. Verify schema
changes, missing values, request failures
and deterministic reruns.
A small public dataset from the supplied EDA project list.
LEARN FUNDAMENTALS. BUILD MODERN AI.
C-INOONLABS
MODULE I / FEATURED CAPSTONE
PYTHON / END-TO-END APPLICATION
Personal Expense
Tracking Platform
Build and deploy a complete expense-management application that brings together the module's
Python skills in an interview-ready portfolio project.
FROM THE CSV EXPENSE ANALYZER TO A DEPLOYED APPLICATION
Architecture & project setup
01
Design a modular CLI, API and storage layer, and explain each architectural choice. Configure
pyproject.toml, initialize Git with meaningful commits, and write tests from the start.
Command-line expense management
02
Build a Click CLI with add, list, edit and delete commands. Begin with JSON file storage,
validate amounts, dates and categories, and test normal operations and error cases.
FastAPI backend & SQLite migration
03
Migrate existing JSON records into SQLite without losing data. Create FastAPI endpoints
matching the CLI commands, validate requests with Pydantic, and refactor the CLI to call the
API.
Analytics, visualization & code quality
04
Use Pandas to expose category totals and monthly spending trends through analytics
endpoints; create Matplotlib charts. Add structured logging, complete test coverage, and
resolve Ruff and mypy findings.
Deployment, CI/CD & final demonstration
05
Deploy the API with persistent SQLite storage, targeting a free cloud allowance. Run tests and
quality checks through GitHub Actions on every push; deploy passing releases and publish a
clear README and recorded demo.
PORTFOLIO DELIVERABLES
A working CLI and deployed API; versioned source code; migration script; analytics and charts;
automated tests with a coverage report; CI/CD workflow; setup guide and demonstration.
STACK
Python, Click, FastAPI, Pydantic, SQLite, Pandas, Matplotlib, pytest, Ruff, mypy, Git, GitHub Actions.
Hosting: Railway is one free-tier candidate; stay within its current usage allowance and use a persistent volume. Confirm
plan limits before deployment. Use sample expenses for the public demo.
