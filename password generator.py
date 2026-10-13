import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR SYSTEM")
print("=" * 40)

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = string.ascii_lowercase

if use_upper:
    characters += string.ascii_uppercase

if use_digits:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

if len(characters) == 0:
    print("No characters selected!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\nGenerated Password:")
    print(password)
    input("\nPress Enter to Exit...")