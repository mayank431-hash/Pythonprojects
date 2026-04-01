import random 
import string
letters=string.ascii_letters#a-z and A-Z
digits=string.digits
symbols=string.punctuation
all_characters= letters+digits+symbols
length=int(input("ENTER PASSWORD LENGTH:"))
password=""
for i in range(length):
    password+=random.choice(all_characters)

print("generated password",password)