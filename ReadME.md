# Python Selenium-Pytest Hybrid Framework

This repository contains a hybrid test automation framework using Python, Selenium, and Pytest. The framework combines the powerful features of Selenium for web automation and Pytest for efficient test organization and execution.

## Features:
> **Page Object Model (POM)**: Organizes the code into reusable page objects for each web page.

> **Fixture-based Setup and Teardown**: Uses Pytest fixtures to manage the setup and teardown processes efficiently.

> **Locators Management**: Centralized locators directory to manage changes easily.

> **Configuration Management**: Centralized configuration using a configurations.ini file for easy maintenance.

> **Cross-Browser Testing**: Supports Chrome, and can be expanded to support other browsers.

> **Data-Driven Testing**: Supports data driven testing using pytest parameterization fixture. 

> **Parallel Execution**: Optional parallel mode execution for faster test runs.


## Additional Considerations
> **Logging**: Utilized Python logging to capture detailed information during test execution.

> **Reporting**: Implemented a reporting mechanism for better visualization of test results (e.g., HTML reports).


## Framework Structure
1. **tests**: This directory contains test scripts organized into classes.
2. **pages**: This directory contains page objects representing the different pages of the application.
3. **utilities**: This directory holds utility functions.
4. **configurations**: This directory contains configuration files.
5. **resources**: This directory contains test data files.
6. **locators**: This directory contains locators from pages.
7. **reports**: This is where your test reports will be stored.
8. **logs**: Store log files generated during test execution.
9. **conftest.py**: Pytest configuration file, which includes fixture definitions, setup, and teardown methods.
10. **pytest.ini**: Pytest Setup details
11. **requirements.txt**: List of project dependencies.
12. **Runner.py**: The main script to run your tests.


