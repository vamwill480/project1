import random
def random_code():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code = ''
    for i in range(10):
        code += random.choice(alphabet)
    return code