import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#%&*+<>"

all = lower + upper + numbers + symbols

length = 15

password = "".join(random.sample(all, length))
passwordfile = open("password.txt","w")
passwordfile.write(password)