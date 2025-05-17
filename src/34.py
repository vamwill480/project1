import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Args:
        length (int): The length of the generated string.
        
    Returns:
        str: A randomly generated string.
    """
    # Ensure the input is an integer
    if not isinstance(length, int):
        raise ValueError("The 'length' parameter should be an integer.")
    
    # Generate a random string of the given length
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

# Example usage:
random_string = generate_random_string(10)
print(random_string)
