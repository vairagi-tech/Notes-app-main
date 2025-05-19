# Notes App – Test Automation Framework

## Overview

This project is a full-stack Notes Application with a robust, scalable test automation framework. The framework is designed to ensure high-quality releases by automating API, UI, and mobile testing, and is fully integrated with CI/CD pipelines.

## Features

- **API Testing:** Automated tests for all backend endpoints (CRUD operations, validation, error handling).
- **UI Testing:** Selenium-based tests for all major user flows in the React frontend.
- **Mobile Testing:** Appium-based tests for Android (native app scenarios).
- **CI/CD Integration:** Automated test execution and reporting via GitHub Actions.
- **Test Reporting:** Generates HTML and Allure reports for every test run.

## Tech Stack

- **Frontend:** React, JavaScript
- **Backend:** Node.js, Express, MongoDB
- **Test Automation:** Python, pytest, Selenium, Appium, requests, pytest-html, Allure
- **CI/CD:** GitHub Actions

## Directory Structure

```
Notes-app-main/
├── NotesApp_project/
│   └── Notes-App-main/
│       ├── src/                  # React frontend source
│       ├── notes-app-backend/    # Node.js backend
│       └── tests/                # Test automation framework
│           ├── api/              # API test cases
│           ├── ui/               # UI test cases
│           ├── mobile/           # Mobile test cases
│           ├── conftest.py       # Pytest configuration
│           └── requirements.txt  # Python dependencies
└── .github/
    └── workflows/
        └── test.yml              # CI/CD workflow
```

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js & npm
- Chrome browser (for UI tests)
- Android emulator & Appium server (for mobile tests)
- MongoDB (for backend)

### Setup

1. **Clone the repository**
2. **Install backend dependencies:**
   ```bash
   cd NotesApp_project/Notes-App-main/notes-app-backend
   npm install
   npm start
   ```
3. **Install frontend dependencies:**
   ```bash
   cd ../
   npm install
   npm start
   ```
4. **Set up test environment:**
   ```bash
   cd tests
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. **Configure environment variables:**
   - Create a `.env` file in `tests/`:
     ```
     BASE_URL=http://localhost:3000
     API_URL=http://localhost:5000
     ```

## Running Tests

- **API Tests:**  
  `pytest tests/api/ -v`
- **UI Tests:**  
  `pytest tests/ui/ -v`
- **Mobile Tests:**  
  Start Appium and Android emulator, then:  
  `pytest tests/mobile/ -v`
- **All Tests:**  
  `pytest tests/ -v`

Test reports are generated in `test-results/`.

## CI/CD

- Automated tests run on every push and pull request via GitHub Actions.
- Results and reports are uploaded as workflow artifacts.

## Best Practices

- Page Object Model for UI tests
- Data-driven and independent test cases
- Parallel test execution
- Comprehensive reporting and error handling

## Contribution

1. Fork and branch for your feature/fix.
2. Add or update tests as needed.
3. Ensure all tests pass.
4. Submit a pull request for review.

## Contact

For questions or support, please contact the QA team. 