# Python UI Automation Challenge

This repository contains Selenium and Playwright end-to-end tests for Sauce Demo and Zoopla flows.
See `docs/QA_STRATEGY.md` for the testing policy and definition of done.

## QA Standards

- Page Object Model classes live under `page_objects/` and keep locators/actions out of test cases.
- Pytest fixtures in `tests/conftest.py` own browser startup, teardown, credentials, and failure artifacts.
- Allure result files can be generated with `--alluredir Results/allure-results`.
- Tests are grouped with explicit pytest markers so CI can run fast smoke checks and keep credentialed live-site checks separate.
- Browser runs support `--headless` for CI and headed mode for local debugging.
- Failed browser tests save screenshots in `Results/screenshots/` and attach them to Allure reports.
- Parallel execution is supported through `pytest-xdist`.
- Secrets are read from environment variables, not committed in test code.
- Critical linting is enforced with Ruff; Black configuration is included for consistent formatting.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
```

For Zoopla login flows, create a local `.env` or set these variables in your shell:

```powershell
$env:ZOOPLA_USERNAME="your-email@example.com"
$env:ZOOPLA_PASSWORD="your-password"
```

## Common Commands

```powershell
black .
ruff check .
pytest -m smoke --headless --alluredir Results/allure-results
pytest -m "sauce_labs and playwright" --headless -n auto --alluredir Results/allure-results
pytest -m zoopla --selectbrowser=chrome --headless -n 2 --alluredir Results/allure-results
```

If the Allure command line is installed locally, generate an HTML report with:

```powershell
allure serve Results/allure-results
```

## CI

GitHub Actions runs linting and parallel smoke tests on pushes and pull requests. It uploads browser artifacts and Allure result files. Zoopla tests are available as a manual workflow because they require live-site credentials and are more likely to be affected by third-party site changes.
