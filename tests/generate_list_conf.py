import random

def generated_list():
    n = random.randint(0, 100)
    arr = [random.randint(-10000, 10000) for _ in range(n)]
    return arr
