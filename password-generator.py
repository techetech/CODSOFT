import string
from random import *

letters=string.ascii_letters
digits=string.digits
symbol=string.punctuation
char=letters+digits+symbol

length=int(input("Enter the desired length of password : "))
password= "".join(choice(chars) for x in range(randint(length)))
print(password)
