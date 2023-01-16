import string
import random

password_length = int(input("How many characters do you want your password to be? "))

character_List = string.digits + string.ascii_letters + string.punctuation

print('What kind of characters do you want in your password? \n1.) Letters \n2.) Digits \n3.) Special characters')

password = ""

int(input("Select one of the options by entering the corresponding number "))

print(random.choice(character_List))

for i in range(password_length):
    password += password + random.choice(character_List)
print(password)




