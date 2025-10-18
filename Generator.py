import random

simb = "QWERTYUIOPASDFGHKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890+-!@#$%^&*"
length = int(input("длина: "))
password = ""
cur = 0

while cur < length:
    cur += 1
    password = password + random.choice(simb)

print(password)
