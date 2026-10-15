def calculate_total(prices):
    """Return the total of a list of non-negative prices."""
    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative")
    return sum(prices)


def is_valid_username(username):
    """Return whether a username has between 3 and 15 characters."""
    return 3 <= len(username) <= 15 and username.isalnum()


def safe_divide(dividend, divisor):
    """Divide two numbers and let Python report division by zero."""
    return dividend / divisor
