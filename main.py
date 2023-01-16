import string
import random

# First input to ask for the length of the password
try:
    password_length = int(input("How many characters do you want your password to be? "))
except ValueError:
    raise Exception('Please enter a number') from None

print('What kind of characters do you want in your password? \n1.) Letters \n2.) Digits \n3.) Special characters')

try:
    option = int(input("Select one of the options by entering the corresponding number "))
except ValueError:
    raise Exception('Please enter a number.') from None

character_List = string.digits + string.ascii_letters + string.punctuation
password = ""

for i in range(password_length):
    password += password + random.choice(character_List)
print(password)




