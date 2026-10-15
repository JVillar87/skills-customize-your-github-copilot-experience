# 📘 Assignment: Testing Python Programs with pytest

## 🎯 Objective

Learn how to use pytest to write automated tests for Python functions, check edge cases, and verify that expected errors are handled correctly.

## 📝 Tasks

### 🛠️ Write Basic Unit Tests

#### Description

Create a pytest test file for the functions in `starter-code.py` and verify their normal behavior.

#### Requirements

Completed program should:

- Create a test file named `test_starter_code.py`.
- Test `calculate_total()` with multiple item prices.
- Test `is_valid_username()` with valid and invalid usernames.
- Test `safe_divide()` with two numbers that divide evenly.

### 🛠️ Cover Edge Cases

#### Description

Expand the test suite to check boundary values and unusual but valid inputs.

#### Requirements

Completed program should:

- Test an empty list and a single-item list with `calculate_total()`.
- Test usernames at the minimum and maximum allowed lengths.
- Test decimal values with `safe_divide()`.
- Include at least one test that uses `pytest.mark.parametrize`.

### 🛠️ Test Expected Errors

#### Description

Use pytest's exception assertions to verify that the functions reject invalid input in a predictable way.

#### Requirements

Completed program should:

- Verify that `calculate_total()` raises `ValueError` for a negative price.
- Verify that `safe_divide()` raises `ZeroDivisionError` when the divisor is zero.
- Run the complete test suite with `pytest` and confirm that all tests pass.
- Use clear test names that describe the behavior being checked.
