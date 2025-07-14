import random
import string

random.seed(42)


def random_letters(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_numbers(length=8):
    return ''.join(random.choices(string.digits, k=length))


def random_mixed(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
