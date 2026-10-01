# Project Guidelines

## Project Structure

- Library code lives in `src/django_tasks_pgmq/`.
- Tests live in `tests/` and use the Django project in `tests/testapp/`.
- The testapp requires a running PostgreSQL instance with the PGMQ extension installed.

## Development Commands

- Run focused tests with `hatch run pytest tests/<test_file>.py`.
- Run the full test suite with `hatch run pytest tests/`.
- Run the full test matrix (all Python × Django version combinations) with `hatch test`.
- Run strict type checks with `hatch check types` (runs both Pyrefly and mypy).
- Run linting and code quality checks with `hatch check code`.
- Verify and apply formatting with `hatch check fmt`.

## Python and Django Conventions

- Support Python 3.12+ and Django 6.0/6.1 as declared in `pyproject.toml`.
- Preserve strict typing and existing type annotations; production code is checked with both mypy and Pyrefly.
- Follow the existing Ruff configuration, including a 120-character line limit and PEP 257 docstring style.
- There are no custom Django settings beyond `TASKS`; do not introduce any.

## Backend Implementation

- The PGMQ backend lives in `src/django_tasks_pgmq/backend.py` and implements the `django_tasks.backends.base.BaseTaskBackend` interface.
- Database connection is obtained through Django's standard connection handling — never open raw psycopg connections directly.
- PGMQ queue names should be derived from the `QUEUES` setting in the `TASKS` configuration.

## Testing Expectations

- Integration tests require a real PostgreSQL database with `pgmq` extension; do not mock the database layer.
- Add or update focused tests for every behavior change.
- Group tests for a class in a single `Test<Name>` class; prefix each test method with `test_`.
- Run the focused test file first, then the full suite before finishing.

## Change Scope

- Keep changes minimal and consistent with neighboring code.
- Use Conventional Commits for commit messages: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, or `chore:`.
- Update `README.md` when a change affects documented behavior, public APIs, installation, or usage examples.
- Update `CHANGELOG.md` for every user-visible change under the `[Unreleased]` section before finishing. Follow the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format using the labels `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security`.
