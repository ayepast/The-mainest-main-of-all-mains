for i in range(1,6):
    print("*" * i)

name = str(input("имя: "))
print("*" * (len(name) + 2))
print("*" + name + "*")
print("*" * (len(name) + 2))

stri = str(input("текст:"))
ns = 0
for i in range(0,len(stri)):
    if stri[i] == "n":
        ns += 1


print(ns)
