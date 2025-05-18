import random

def draw_random_string(length):
    """
    Generate a random string of specified length.
    
    Example usage:
    >>> print(draw_random_string(5))
    "aBcD"
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

# Test the function with a specific length
random_string = draw_random_string(10)
print(random_string)
