import random

simb = "QWERTYUIOPASDFGHKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890+-!@#$%^&*"
length = int(input("длина: "))
password = ""
for i in range(0,length):
   
    password = password + random.choice(simb)

print(password)
