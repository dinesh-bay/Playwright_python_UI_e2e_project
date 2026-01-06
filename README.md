# Playwright Python Test Automation Framework

A robust, scalable test automation framework built with **Playwright** and **Python** following industry best practices. This framework demonstrates **Page Object Model (POM)** design pattern, data-driven testing, parallel execution, and comprehensive reporting capabilities.

---

## Table of Contents

- [Features](#-features)
- [Framework Architecture](#-framework-architecture)
- [Technologies & Tools](#-technologies--tools)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [Running Tests](#-running-tests)
- [Configuration](#-configuration)
- [Reporting](#-reporting)
- [Best Practices Implemented](#-best-practices-implemented)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## Features

### Core Capabilities
- **Page Object Model (POM)** - Clean separation of test logic and page interactions
- **Data-Driven Testing** - Support for CSV and JSON data sources
- **Parallel Execution** - Faster test execution using pytest-xdist
- **Cross-Browser Testing** - Chromium, Firefox, and WebKit support
- **Headed/Headless Modes** - Flexible browser visibility options
- **Auto-Wait Mechanisms** - Playwright's built-in smart waiting
- **Screenshot on Failure** - Automatic capture of failed test states
- **Video Recording** - Record test execution for debugging
- **Trace Viewer Support** - Playwright trace files for detailed debugging
- **Rerun Failed Tests** - Automatic retry mechanism for flaky tests
- **Test Markers** - Organize tests by categories (sanity, regression, etc.)
- **Random Test Data Generation** - Using Faker library for dynamic data
- **Multiple Reporting Formats** - HTML and Allure reports
- **Centralized Configuration** - Easy management of test data and settings

### Advanced Features
- **Configurable via pytest.ini** - Centralized test configuration
- **Command-line Overrides** - Flexibility to override settings on-the-fly
- **Custom Fixtures** - Reusable browser and page setup
- **Utility Classes** - Data readers and random data generators
- **End-to-End Test Scenarios** - Complete user journey testing
- **Comprehensive Logging** - Detailed logs for debugging

---

## Framework Architecture

```
┌─────────────────────────────────────────────────────┐
│                  TEST LAYER                         │
│  (tests/test_*.py - Business logic & assertions)    │
└─────────────────┬───────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────┐
│               PAGE OBJECT LAYER                     │
│  (pages/*_page.py - Locators & Page actions)        │
└─────────────────┬───────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────┐
│              UTILITIES LAYER                        │
│  (utilities/ - Helper functions & data utilities)   │
└─────────────────┬───────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────┐
│            CONFIGURATION LAYER                      │
│  (config.py, conftest.py, pytest.ini)               │
└─────────────────────────────────────────────────────┘
```

---

## Technologies & Tools

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Programming language |
| **Playwright** | Browser automation library |
| **Pytest** | Testing framework |
| **pytest-xdist** | Parallel test execution |
| **pytest-html** | HTML report generation |
| **Allure** | Advanced reporting and analytics |
| **pytest-rerunfailures** | Retry failed tests |
| **Faker** | Random test data generation |
| **openpyxl** | Excel file handling |

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **IDE** - VS Code, PyCharm, or any Python IDE

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/playwright-python-framework.git
cd playwright-python-framework
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

Or install specific browsers:
```bash
playwright install chromium
playwright install firefox
playwright install webkit
```

### 5. Verify Installation

```bash
pytest --version
playwright --version
```

---

## Project Structure

```
practise_pw_python_project/
│
├── config.py                      # Test configuration and credentials
├── conftest.py                    # Pytest fixtures and hooks
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
│
├── pages/                         # Page Object Model classes
│   ├── __init__.py
│   ├── home_page.py              # Home page actions & locators
│   ├── login_page.py             # Login page actions & locators
│   ├── registration_page.py      # Registration page actions & locators
│   ├── product_page.py           # Product page actions & locators
│   ├── shopping_cart_page.py    # Shopping cart actions & locators
│   ├── checkout_page.py          # Checkout page actions & locators
│   ├── my_account_page.py        # My account page actions & locators
│   ├── logout_page.py            # Logout page actions & locators
│   └── search_results_page.py    # Search results actions & locators
│
├── tests/                         # Test cases
│   ├── __init__.py
│   ├── test_login.py             # Login functionality tests
│   ├── test_login_data_driven.py # Data-driven login tests
│   ├── test_user_registration.py # User registration tests
│   ├── test_product_search.py    # Product search tests
│   ├── test_add_product_to_cart.py # Shopping cart tests
│   ├── test_user_logout.py       # Logout functionality tests
│   └── test_end_to_end.py        # End-to-end scenarios
│
├── utilities/                     # Helper utilities
│   ├── __init__.py
│   ├── data_reader_util.py       # Read data from CSV/JSON files
│   └── random_data_util.py       # Generate random test data
│
├── testdata/                      # Test data files
│   ├── logindata.json            # Login test data (JSON)
│   └── logindata.csv             # Login test data (CSV)
│
└── reports/                       # Test execution reports
    ├── myreport.html             # HTML report
    ├── screenshots/              # Failed test screenshots
    ├── videos/                   # Test execution videos
    ├── traces/                   # Playwright trace files
    ├── allure-results/           # Allure raw results
    └── allure-report/            # Allure HTML report
```

---

## Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run specific test function
pytest tests/test_login.py::test_valid_user_login

# Run tests with verbose output
pytest -v

# Run tests with print statements visible
pytest -s
```

### Browser Selection

```bash
# Run with Chromium (default)
pytest --browser=chromium

# Run with Firefox
pytest --browser=firefox

# Run with WebKit (Safari)
pytest --browser=webkit
```

### Headed vs Headless Mode

```bash
# Run in headless mode (default)
pytest

# Run in headed mode (visible browser)
pytest --headed
```

### Parallel Execution

```bash
# Run tests in parallel using 4 workers
pytest -n 4

# Run tests in parallel using auto-detected CPU count
pytest -n auto
```

### Test Markers

```bash
# Run only sanity tests
pytest -m sanity

# Run only regression tests
pytest -m regression

# Run sanity OR regression tests
pytest -m "sanity or regression"

# Run tests excluding certain markers
pytest -m "not sanity"
```

### Data-Driven Tests

```bash
# Run data-driven tests
pytest -m datadriven

# Run specific data-driven test
pytest tests/test_login_data_driven.py
```

### Rerun Failed Tests

```bash
# Rerun failed tests 2 times with 1 second delay
pytest --reruns 2 --reruns-delay 1
```

### Custom Test Run Examples

```bash
# Run with specific base URL
pytest --base-url=https://your-app-url.com

# Run with video recording
pytest --video=on

# Run with screenshot on failure
pytest --screenshot=only-on-failure

# Run with tracing enabled
pytest --tracing=on

# Combination example
pytest -v -n 4 --browser=firefox --headed -m sanity
```

---

## Configuration

### pytest.ini Configuration

The `pytest.ini` file contains default test execution settings:

```ini
[pytest]
addopts =
    -v                                          # Verbose output
    --browser=chromium                          # Default browser
    --base-url=https://tutorialsninja.com/demo/ # Base URL
    --video=retain-on-failure                   # Video recording
    --screenshot=only-on-failure                # Screenshot capture
    --tracing=retain-on-failure                 # Trace files
    --html=reports/myreport.html                # HTML report
    --alluredir=reports/allure-results          # Allure results
```

### config.py - Test Data

Update `config.py` with your test credentials and data:

```python
class Config:
    email = "your_email@example.com"
    password = "your_password"
    product_name = "MacBook"
    # Add more configuration as needed
```

### Command-Line Overrides

Any pytest.ini setting can be overridden via command line:

```bash
pytest --browser=firefox --base-url=https://staging.example.com
```

---

## Reporting

### HTML Report

After test execution, open the HTML report:

```bash
# Report location
reports/myreport.html
```

Features:
- Test execution summary
- Pass/fail statistics
- Test duration
- Error details and stack traces
- Embedded screenshots

### Allure Report

Generate and view Allure report:

```bash
# Generate Allure report from results
allure generate reports/allure-results --clean -o reports/allure-report

# Open Allure report in browser
allure open reports/allure-report

# Or serve the report
allure serve reports/allure-results
```

Allure Report Features:
- Trends and statistics
- Test case duration graphs
- Screenshots and attachments
- Video recordings
- Detailed test steps
- Test categorization
- Retry information

### Debug Artifacts

When tests fail, the following artifacts are automatically captured:

- **Screenshots**: `reports/screenshots/`
- **Videos**: `reports/videos/`
- **Traces**: `reports/traces/` (open with `playwright show-trace <trace-file>`)

---

## Best Practices Implemented

### 1. **Page Object Model (POM)**
- Separation of concerns
- Reusable page components
- Easy maintenance

### 2. **DRY Principle**
- Reusable fixtures in conftest.py
- Utility classes for common operations
- Centralized configuration

### 3. **Naming Conventions**
- Descriptive test names
- Clear variable naming
- Consistent file structure

### 4. **Error Handling**
- Try-except blocks in page objects
- Meaningful error messages
- Graceful failure handling

### 5. **Documentation**
- Inline code comments
- Docstrings for classes and methods
- Comprehensive README

### 6. **Version Control**
- .gitignore for Python projects
- Requirements.txt for dependencies
- Clean commit history

### 7. **Scalability**
- Modular architecture
- Easy to add new tests
- Support for multiple environments

### 8. **CI/CD Ready**
- Command-line configuration
- Parallel execution support
- Multiple report formats

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Ensure all tests pass before submitting PR

---

## Contact & Support

If you have any questions or need help with the framework:

- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- **GitHub**: [@yourusername](https://github.com/yourusername)

---

## Author

**Dinesh Gujarathi**

Test Automation Engineer with experience in building scalable test frameworks with Tricentis Tosca and Playwright and implementing best practices in quality engineering.

For more, here is my LinkedIn - www.linkedin.com/in/dineshgujarathi

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- Testing community for inspiration and best practices

---

## Future Enhancements

- [ ] API testing integration
- [ ] Visual regression testing
- [ ] CI/CD pipeline examples (GitHub Actions, Jenkins)
- [ ] Docker containerization
- [ ] Performance testing integration
- [ ] Mobile testing support
- [ ] Cloud execution support (BrowserStack, Sauce Labs)
- [ ] Advanced reporting with custom metrics
- [ ] Integration with test management tools (TestRail, Zephyr)

---

## Learning Resources

### Recommended for Beginners

1. **Playwright Official Tutorial**: [playwright.dev/python](https://playwright.dev/python/)
2. **Pytest Documentation**: [docs.pytest.org](https://docs.pytest.org/)
3. **Python Testing with Pytest** by Brian Okken
4. **Page Object Model Pattern**: [Martin Fowler's Blog](https://martinfowler.com/bliki/PageObject.html)

### Key Concepts Demonstrated

- Test automation framework design
- Page Object Model implementation
- Pytest fixtures and hooks
- Data-driven testing approaches
- Test reporting and analytics
- Browser automation best practices
- Code organization and maintainability

---

**If you find this project helpful, please give it a star!**
