import random
import string
print("Welcome To Password Genarator")
print("Enter a Lenght of Password")
Length = int(input())
print("Enter a level of Password\n1.Hard\n2.Mediam\n3.Easy")
Level_of = int(input())
# Allowed string constants
if Level_of == 1:
    allowedChars = string.ascii_letters + string.digits + string.punctuation+ string.hexdigits + string.whitespace + string.printable
elif Level_of == 2:
    allowedChars = string.ascii_letters + string.digits + string.hexdigits 
elif Level_of == 3:
    allowedChars = string.ascii_letters
# Genereate password
password = ''.join(random.choice(allowedChars) for _ in range(Length))
print(password)