import random

pc = random.randint(1, 100)
print(pc)
i=0

while True:
    a=int(input("noumero:"))
    if a == pc:
        print("mpravo")
        i += 1
        print("prospathises",i,"fores")
        break

    if a>pc:
        print("kateva")
        i += 1

    elif a<pc:
        print("aneva")
        i += 1

