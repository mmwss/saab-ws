def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to the n-th term.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n_terms = 10
fib_sequence = generate_fibonacci(n_terms)
print(f"Fibonacci sequence up to {n_terms} terms: {fib_sequence}")
