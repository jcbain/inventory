import random
import string

def generate_random_string(n_characters):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=n_characters))