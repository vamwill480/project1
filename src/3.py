import random 
def get_random_int(n): 
    """Returns a random integer between 1 and n.""" 
    return random.randint(1, n) 

def get_random_float(n): 
    """Returns a random float between 0 and n.""" 
    return random.uniform(0, n)