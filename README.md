# Open Brewery API Test Automation

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Test Framework](https://img.shields.io/badge/tested%20with-pytest-yellow)
![Allure Reporting](https://img.shields.io/badge/report-Allure-blueviolet)
![CI](https://github.com/name-ivan/O_Net_openbrew_test/actions/workflows/pytest.yml/badge.svg?branch=main)

This project demonstrates API test automation using [Open Brewery DB](https://www.openbrewerydb.org/) — a public REST API that returns brewery information by filters like type, city, or name.

The test suite is written in **Python** using **pytest**, with **Allure** for reporting and a modular structure inspired by the Page Object Model (POM).

---

## 📋 Test Cases

| Test Case ID | Title                                    | Type     | Steps                                                                                                          | Expected Result                                                                 | Validation                                           |
|--------------|------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------|
| TC_01        | Filter breweries by valid type           | Positive | 1. Set a valid `by_type` value (e.g. `micro`) <br> 2. Send GET request to `/breweries?by_type=<type>` <br> 3. Parse JSON response <br> 4. Verify `brewery_type` of each item matches input | 200 OK <br> List of breweries with matching `brewery_type`                      | `status_code == 200`, each item has `brewery_type == input` |
| TC_02        | Filter breweries by invalid random types | Negative | 1. Generate invalid `by_type` value (letters, numbers, mixed) <br> 2. Send GET request to `/breweries?by_type=<invalid>` <br> 3. Parse JSON response <br> 4. Verify it's not a list and contains `"message"` | 200 OK <br> Not a list <br> Contains `"message"` field                          | `not isinstance(response.json(), list)` and `"message" in response` |

---

## 🧪 Project Structure

```
brewery_api_tests/
├── src/                                 # Source code root
│   └── brewery_api_tests/              
│       ├── endpoints/                  # API interaction layer
│       │   └── brewery_endpoint.py     # Encapsulated API calls to /breweries
│       ├── utils/                      # Helper functions
│       │   └── generators.py           # Random string generators for test data
│       └── __init__.py                 
├── tests/                              
│   └── test_brew.py                    # API test cases for valid/invalid brewery types
├── pytest.ini                          # Pytest config (sets PYTHONPATH to src)
├── pyproject.toml                      # Poetry project config and dependencies
├── .gitignore                          
```

---

## ✅ Validation Strategy

| Checkpoint                   | Reason                                                                 |
|-----------------------------|------------------------------------------------------------------------|
| `status_code == 200`        | Confirms endpoint is reachable and returns HTTP OK                     |
| `isinstance(response, list)`| Ensures valid query returns iterable data                              |
| `brewery_type == expected`  | Verifies the filtering behavior of the API                             |
| `"message" in response`     | Detects and confirms API error handling for invalid query parameters   |
| `Allure attach`             | Adds visibility into responses for debugging or report review          |

---

## 🧰 Tools & Libraries Used

- [Python 3.12+](https://www.python.org/)
- [Poetry](https://python-poetry.org/) for dependency management
- [Pytest](https://docs.pytest.org/)
- [Allure](https://docs.qameta.io/allure/) for test reporting
- [requests](https://pypi.org/project/requests/) – to send HTTP requests

---

## 🚀 How to Run

### 1. Install dependencies (with Poetry)
```bash
poetry install
```

### 2. Run tests
```bash
poetry run pytest --alluredir=allure-results
```

### 3. Serve Allure report
```bash
allure serve allure-results
```
---
## 📊 Sample Allure Report

Below is a screenshot of the **Allure report** generated after running the test suite:

![Allure Report](assets/allure_report.png)

✅ The report highlights:

- **Logical grouping** of test cases via Allure annotations (`@allure.feature`, `@allure.story`)
- Clearly **parameterized test names** like `test_by_type_invalid[letters_only]`
- Detailed **step-by-step logging**:
  - The exact GET request made (with parameters)
  - HTTP status code
  - Response body and JSON parsing
- For invalid input types, the API returns a consistent message:  
  `{"message": "Welcome to the Breweries API, see the documentation at https://www.openbrewerydb.org/documentation"}`

🧾 This rich, visual breakdown of test execution provides easy debugging and validation for developers, testers, and reviewers alike.

---

## 📦 Delivery Notes

- This project includes both positive and negative test cases.
- Test code is modular, using endpoint abstraction and parametrization.
- Allure steps and attachments are used for detailed, readable reports.
