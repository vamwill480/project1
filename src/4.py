import random

def random_python_code():
    return ''.join(random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(random.randint(1, 100)))