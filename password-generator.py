import string

letters=string.ascii_letters
digits=string.digits
symbol=string.punctuation
char=letters+digits+symbol

length=int(input("Enter the desired length of password : "))
password= "".join(choice(char) for x in range(0,length))
print(password)
