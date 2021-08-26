import random

long_password = int(input('Enter lenght of your password: '))
password = ""

for x in range(long_password):
    int_character = random.randint(33, 127)
    password += str(chr(int_character))

print(password)