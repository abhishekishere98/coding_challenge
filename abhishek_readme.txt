Hello Zoopla,

Thank you for considering me for this opportunity. I would like to add some basic details aout this project for ease validation/analysis.

This project implements following concepts:

1) Page Object Model for locators and methods management
2) Webdriver manager to take care of latest driver installation and maintaianance
3) Driver Factory to support different browsers, currently support chrome and firefox(--selectbrowser passed from CLI)
4) Basic report generation at Testcase level (--template and --report passed from CLI for format and report filename)
5) Parallel execution by multiple browser instances (-n passed through CLI)
6) Test data is driven from a separate file
7) Remote Execution
7) suggested execution command from pycharm terminal : pytest --selectbrowser=chrome --template=html1/index.html --report=report.html -n 2
