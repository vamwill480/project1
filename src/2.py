import random

def get_random_number(n):
    return random.randint(1, n)

def get_random_string(n):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(n):
        result += random.choice(letters)
    return result
