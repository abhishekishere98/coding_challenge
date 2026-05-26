# QA Strategy

## Test Pyramid

- Smoke: fast browser checks that prove login and cart basics still work.
- Regression: broader Sauce Demo flows across Selenium and Playwright.
- Live-site E2E: Zoopla tests that depend on third-party availability, account state, and credentials.

## Framework Features

- Page Object Model: page classes in `page_objects/` expose readable business actions and assertions.
- Pytest fixtures: `tests/conftest.py` manages Selenium drivers, Playwright pages, credentials, and artifacts.
- Allure reporting: test runs can write results to `Results/allure-results`.
- Screenshot capture: failed Selenium and Playwright tests save screenshots and attach them to Allure.
- Parallel execution: `pytest-xdist` supports `-n auto` or fixed workers for browser suites.
- GitHub Actions CI: `.github/workflows/qa.yml` runs linting, parallel smoke tests, artifact upload, and manual Zoopla tests.

## Execution Policy

- Pull requests run lint and smoke tests.
- Manual CI runs can execute Zoopla tests with repository secrets.
- Authenticated tests must read credentials from environment variables.
- Failed browser tests must capture artifacts under `Results/`.
- Parallel runs should use markers to avoid mixing tests that mutate the same external account state.

## Stability Practices

- Prefer explicit waits and user-facing selectors over sleeps.
- Keep tests independent; avoid relying on existing remote account state when possible.
- Add `smoke` only to tests that are stable enough to block every pull request.
- Mark third-party tests separately so live-site instability does not hide product regressions.

## Definition of Done

- Relevant pytest markers are applied.
- Tests can run headless in CI.
- No secrets or generated artifacts are committed.
- New page-object methods hide locator details from tests.
- Failure artifacts are available for debugging.
