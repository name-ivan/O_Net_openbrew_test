# Open Brewery API Test Automation

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Test Framework](https://img.shields.io/badge/tested%20with-pytest-yellow)
![Allure Reporting](https://img.shields.io/badge/report-Allure-blueviolet)


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
│   └── brewery_api_tests/              # Main package
│       ├── endpoints/                  # API interaction layer
│       │   └── brewery_endpoint.py     # Encapsulated API calls to /breweries
│       ├── utils/                      # Helper functions
│       │   └── generators.py           # Random string generators for test data
│       └── __init__.py                 # Marks the folder as a Python package
├── tests/                              # Test suite
│   └── test_brew.py                    # API test cases for valid/invalid brewery types
├── pytest.ini                          # Pytest config (sets PYTHONPATH to src)
├── pyproject.toml                      # Poetry project config and dependencies
├── .gitignore                          # Ignores virtual env, cache, and test artifacts
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
- `requests` – to send HTTP requests

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

## 📦 Delivery Notes

- This project includes both positive and negative test cases.
- Test code is modular, using endpoint abstraction and parametrization.
- Allure steps and attachments are used for detailed, readable reports.
