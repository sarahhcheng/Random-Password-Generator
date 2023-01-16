import string
import random

# Variables:
character_list = ""
password = ""

# First input to ask for the length of the password
try:
    password_length = int(input("How many characters do you want your password to be? "))
except ValueError:
    raise Exception('Please enter a number') from None

print(
    'What kind of characters do you want in your password? \n1.) Letters \n2.) Digits \n3.) Special characters \n4.) All of the above')

# Input for an option selection
try:
    option = int(input("Select one of the options by entering the corresponding number "))
except ValueError:
    raise Exception('Please enter a number.') from None

# Second option selection
try:
    ask = input("Would you like to make another selection? Enter Y/N ")
except ValueError:
    raise Exception('Please enter Y/N ') from None

# Code block to determine what types of characters are going to be used in the password
if option == 4:
    character_List = string.digits + string.ascii_letters + string.punctuation
elif option == 1:
    character_list = character_list + string.ascii_letters
    if ask == 'Y':
        second_option = int(input("Select one of the options by entering the corresponding number "))
        if second_option == 2:
            character_list = character_list + string.digits
        elif second_option == 3:
            character_list = character_list + string.punctuation
elif option == 2:
    character_list = character_list + string.digits
    if ask == 'Y':
        second_option = int(input("Select one of the options by entering the corresponding number "))
        if second_option == 1:
            character_list = character_list + string.ascii_letters
        elif second_option == 3:
            character_list = character_list + string.punctuation
elif option == 3:
    character_list = character_list + string.punctuation
    if ask == 'Y':
        second_option = int(input("Select one of the options by entering the corresponding number "))
        if second_option == 2:
            character_list = character_list + string.digits
        elif second_option == 1:
            character_list = character_list + string.ascii_letters

for i in range(password_length):
    password += password + random.choice(character_list)
print(password)
