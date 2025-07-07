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
        raise ValueError ("At least one character type must be selected")
    
    password = [random.choice(pool) for pool in char_pools]

    all_chars = ''.join(char_pools)
    password.extend(random.choices(all_chars, k=length - len(password)))

    random.shuffle(password)

    return "" .join(password)

def main():
    print("Welcoome to the password generator")
    try:
        length = int(input("Enter desired password lenght (8-20):  ")) 
        use_uppercase = input("include uppercase letters? Yes/No:  ") == "yes"
        use_lowercase = input("Inlude lowercase letters? Yes/No:  ") == "yes"
        use_numbers = input("Include Numbers? Yes/ No:  ") == "yes"
        use_specials = input("Include special characters? Yes/No:  ") == "yes"
    
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials)

        print(f'Generated Password: {password}')
        print("Password copied to clipboard")

        try:
            import pyperclip
            pyperclip.copy(password)
        except ImportError:
            print('You need to install pyperclip to have this feature!')
            #pip install pyperclip

    except ValueError as e:
            print(f'Error: {e}')

main()



