import random
attempts = 5
a = random.randrange(1,20)
won = False
for i in range(0,attempts):
    guess = int(input("Число: "))
    if guess > a:print("Число больше загаданного") 
    elif guess < a:print("Число меньше загаданного")
    elif guess == a: 
        print("Ты угадал!") 
        won = True
        break
if won == False: print("Ты проиграл...")
