import numpy as np

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        return sequence + [sequence[-1] + sequence[-2]]

print(fibonacci(10))
