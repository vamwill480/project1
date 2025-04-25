def square_root(n):
    if n < 0:
        raise ValueError("Square root of negative numbers not defined.")
    guess = 1.0
    while True:
        value = guess * guess
        if abs(value - n) < 1e-6: 
            return guess
        guess = (guess + n / guess) / 2

# Example usage:
print(square_root(4))  # Output: 2.0
