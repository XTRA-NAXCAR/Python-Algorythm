from random import randint
import time
Organize = False
Average = 0
Box = []
First_half = []
Second_half = []

for i in range(1000):
    Number = randint(0, 16000000)
    Box.append(Number)

start = time.time()

for i in range(len(Box)):
    Average = Average + Box[i]

Average = Average / len(Box)


for i in range(len(Box)):
    if Box[i] < Average:
        First_half.append(Box[i])
    else:
        Second_half.append(Box[i])

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

for i in range(len(First_half)):
    Box.append(First_half[i])
for i in range(len(Second_half)):
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
print(len(Box))