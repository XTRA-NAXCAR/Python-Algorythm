from random import randint
import time
Organize = False
Box = []
First_half = []
Second_half = []

for i in range(8000):
    Number = randint(0, 16000000)
    Box.append(Number)

start = time.time()

for i in range(4000):
    First_half.append(Box[i])
    Second_half.append(Box[len(Box)-i-1])

Box = []

while Organize == False:
    Organize = True
    for i in range(len(First_half) - 1):
        if First_half[i] > First_half [i + 1]:
            aux = First_half[i]
            First_half[i] = First_half[i + 1]
            First_half [i + 1] = aux
            Organize = False

Organize = False

while Organize == False:
    Organize = True
    for i in range(len(Second_half) - 1):
        if Second_half[i] > Second_half [i + 1]:
            aux = Second_half[i]
            Second_half[i] = Second_half[i + 1]
            Second_half [i + 1] = aux
            Organize = False

Organize = False

for i in range(4000):
    Box.append(First_half[i])
for i in range(4000):
    Box.append(Second_half[i])

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
