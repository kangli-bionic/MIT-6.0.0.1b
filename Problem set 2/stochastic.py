import random

def genEven():
    evens = [x for x in range(0,99) if x % 2 == 0]
    return random.choice(evens)

print(genEven())