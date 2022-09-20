This project implements following concepts:

1) Page Object Model for locators and methods management
2) Webdriver manager to take care of the latest driver installation and maintenance
3) Driver Factory to support different browsers, currently supports Chromium, Chrome and Firefox (--selectbrowser passed from CLI)
4) Basic report generation at Test case level (--template and --report passed from CLI for format and report filename)
5) Parallel execution by multiple browser instances (-n passed through CLI, please note this feature doesn’t work with venv, the interpreter must be set to python.exe file at the system level)
6) Test data is driven from a separate file
7) Suggested execution command from pycharm terminal: pytest --selectbrowser=chrome --template=html1/index.html --report=report.html
8) This test can automatically trigger tests when code is merged to master branch using Git Actions. Executions take place in the Chromium browser. Command used: pytest --selectbrowser=chromium --template=html1/index.html --report=report.html
9) Parallel execution sometimes may cause failure although test cases are independent of each other, as while retrieving a saved result we retrieve the latest result and if a new entry is made meanwhile by another test, the current test may fail.
10) Keywords may not directly appear in the search results, hence this scenario has been automated to click on a random result from a keyword search and then check if the property details page has the searched keyword in any of its sections. This is not a full-proof way to validate this scenario but if this functionality is tested thoroughly during feature testing, we can consider this as one of the ways of automating it in regression.
