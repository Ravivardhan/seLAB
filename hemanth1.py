def prog1():
    for i in range(2):
        print("+",end="")
        for i in range(4):
            print("-",end="")
    print("+")
def prog2():
    for i in range(2):
        print("|",end="     ")
    print("|")
for i in range(2):
            prog1()
            for i in range(4):
                prog2()
prog1()