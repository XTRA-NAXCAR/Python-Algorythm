from random import randint
import time
Organize = False
Box = []
Final_Box = []
e = 0

for i in range(8000):
    Number = randint(0, 16000000)
    Box.append(Number)

start = time.time()
def  separate (Box, e):
    temp = []
    temp.append(Box[e])
    e = e + 1
    temp.append(Box[e])

    if temp[0] > temp [1]:
        aux = temp[1]
        temp [1] = temp [0]
        temp [0] = aux
    return temp

def result (Final_Box, Organize):
    while Organize == False:
        Organize = True
        for i in range(len(Final_Box) - 1):
            if Final_Box[i] > Final_Box [i + 1]:
                aux = Final_Box[i]
                Final_Box[i] = Final_Box[i + 1]
                Final_Box [i + 1] = aux
                Organize = False
    return(Final_Box)

for i in range(len(Box) // 2):
    temp = separate(Box, e)
    e = e +2
    Final_Box = temp + Final_Box
    Final_Box = result(Final_Box, False)

final = time.time()
print(final - start)
print(len(Final_Box))

