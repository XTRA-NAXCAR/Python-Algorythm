from random import randint
import time
Organize = False
Box = []

for i in range(8000):
    Number = randint(0, 16000000)
    Box.append(Number)


start = time.time()


while Organize == False:
    Organize = True
    for i in range(len(Box) - 1):
        if Box[i] > Box [i + 1]:
            aux = Box[i]
            Box[i] = Box[i + 1]
            Box [i + 1] = aux
            Organize = False

final = time.time()
print(final - start)
print(len(Box))

