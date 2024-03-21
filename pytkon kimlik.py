import random

def generate_turkish_id():
    return random.randint(10 ** 10, 10 ** 11 - 1)

print(generate_turkish_id())