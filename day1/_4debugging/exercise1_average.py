"""
Identify and fix the error in a function that calculates the average
of a list of numbers but raises an exception when the list is empty.
"""

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    print("Code Debugging[1] Average Calculator")

    average = calculate_average([])
    print(f"Empty list average: {average}")

    average = calculate_average([1, 2, 3, 4, 5])
    print(f"Average of [1, 2, 3, 4, 5]: {average}")
