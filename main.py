import string
import random

password_length = int(input("How long do you want your password to be?"))

character_List = string.digits + string.ascii_letters + string.punctuation

password = ""

for i in range(len(password_length)):
    password += password + random.choice(character_List)
print(password)

