import string
import random

def random_letter(length):
    print(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') * length)
    return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') * length
random_letter(7)

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
print(random_string(29))

