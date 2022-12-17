from random import sample
import string

def get_random_password() -> str:
    return "".join(sample(string.ascii_uppercase+string.ascii_lowercase+string.digits, 8))

print(get_random_password())
