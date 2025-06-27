import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_specials=True):
    if length < 8 or length > 20:
        raise ValueError ("Password lenght must be between 8 and 20 characters")
        
    char_pools = []

    if use_uppercase:
        char_pools.append(string.ascii_uppercase)
    if use_lowercase:
        char_pools.append(string.ascii_lowercase)
    if use_numbers:
        char_pools.append(string.digits)
    if use_specials:
        char_pools.append(string.punctuation)
    if not char_pools:
        raise ValueError ("At leasr one character type must be selected")
    
    password = [random.choice(pool) for pool in char_pools]

    all_chars = ''.join(char_pools)
    password.extend(random.choice(all_chars, k=length - len(password)))
