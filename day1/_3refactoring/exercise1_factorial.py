"""
Refactor the recursive factorial function to use iteration instead,
improving efficiency and avoiding maximum recursion depth issues.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    print("Code Refactoring[1] Factorial Calculator")
    number = 5
    print(f"The factorial of {number} is: {factorial(number)}")
