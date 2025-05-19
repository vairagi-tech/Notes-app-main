# Notes App Test Automation Framework

This directory contains the test automation framework for the Notes App. The framework is built using Python and includes tests for API, UI, and mobile platforms.

## Framework Structure

```
tests/
├── api/                    # API test cases
│   └── test_notes_api.py
├── ui/                     # UI test cases
│   └── test_notes_ui.py
├── mobile/                 # Mobile test cases
│   └── test_notes_mobile.py
├── conftest.py            # Test configuration and fixtures
└── requirements.txt       # Python dependencies
```

## Prerequisites

- Python 3.9 or higher
- Chrome browser (for UI tests)
- Android SDK and emulator (for mobile tests)
- Appium server (for mobile tests)

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the tests directory with the following variables:
   ```
   BASE_URL=http://localhost:3000
   API_URL=http://localhost:5000
   ```

## Running Tests

### API Tests
```bash
pytest tests/api/ -v
```

### UI Tests
```bash
pytest tests/ui/ -v
```

### Mobile Tests
1. Start Appium server:
   ```bash
   appium
   ```

2. Start Android emulator

3. Run tests:
   ```bash
   pytest tests/mobile/ -v
```

### Run All Tests
```bash
pytest tests/ -v
```

## Test Reports

Test results are generated in XML format and can be found in the `test-results/` directory after test execution. These reports are also uploaded as artifacts in the CI/CD pipeline.

## CI/CD Integration

The framework is integrated with GitHub Actions. Tests are automatically run on:
- Push to main branch
- Pull requests to main branch

The workflow can be found in `.github/workflows/test.yml`.

## Best Practices

1. **Test Data Management**
   - Use fixtures for test data setup and cleanup
   - Avoid hardcoding test data in test cases

2. **Page Object Model**
   - UI tests follow the Page Object Model pattern
   - Keep selectors in a separate configuration file

3. **Test Independence**
   - Each test should be independent and not rely on other tests
   - Clean up test data after each test

4. **Error Handling**
   - Use explicit waits instead of implicit waits
   - Implement proper error handling and logging

5. **Code Review**
   - All test code changes must be reviewed
   - Follow PEP 8 style guide for Python code

## Contributing

1. Create a new branch for your changes
2. Write tests for new features
3. Ensure all tests pass
4. Submit a pull request

## Troubleshooting

### Common Issues

1. **Chrome Driver Issues**
   - Ensure Chrome browser is installed
   - Check Chrome driver version compatibility

2. **Appium Issues**
   - Verify Appium server is running
   - Check Android emulator is running
   - Verify device capabilities in test configuration

3. **Test Failures**
   - Check test environment setup
   - Verify test data
   - Check application logs

For more help, please contact the QA team. 