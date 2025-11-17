print("_____________________")
print("|PASSWORD GENERATOR |")
print("|___________________|")

import random
import string
chars = string.ascii_letters + string.digits + string.punctuation
password = "" .join(random.choice(chars) for _ in range (12))
print("your generated password:")
print(password)