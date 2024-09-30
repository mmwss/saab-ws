def factorial(n):
    """
    Calculates the factorial of n using iteration.
    """
    if n < 0:
        raise ValueError("Negative numbers do not have factorials.")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Example usage
number = 5
print(f"The factorial of {number} is: {factorial(number)}")
