from random import randint
import time
Organize = False
Average = 0
Box = []

First_part = []
Second_part = []
Third_part = []
Fourth_part = []

First_half = []
Second_half = []

for i in range(4000000):
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

Average = 0
Box = []

for i in range(len(First_half)):
    Average = Average + First_half[i]

Average = Average / len(First_half)

for i in range(len(First_half)):
    if First_half[i] < Average:
        First_part.append(First_half[i])
    else:
        Second_part.append(First_half[i])

First_half = []
Average = 0

for i in range(len(Second_half)):
    Average = Average + Second_half[i]

Average = Average / len(Second_half)
for i in range(len(Second_half)):
    if Second_half[i] < Average:
        Third_part.append(Second_half[i])
    else:
        Fourth_part.append(Second_half[i])

Second_half = []

while Organize == False:
    Organize = True
    for i in range(len(First_part) - 1):
        if First_part[i] > First_part [i + 1]:
            aux = First_part[i]
            First_part[i] = First_part[i + 1]
            First_part [i + 1] = aux
            Organize = False

Organize = False

while Organize == False:
    Organize = True
    for i in range(len(Second_part) - 1):
        if Second_part[i] > Second_part [i + 1]:
            aux = Second_part[i]
            Second_part[i] = Second_part[i + 1]
            Second_part [i + 1] = aux
            Organize = False

Organize = False

while Organize == False:
    Organize = True
    for i in range(len(Third_part) - 1):
        if Third_part[i] > Third_part [i + 1]:
            aux = Third_part[i]
            Third_part[i] = Third_part[i + 1]
            Third_part [i + 1] = aux
            Organize = False

Organize = False

while Organize == False:
    Organize = True
    for i in range(len(Fourth_part) - 1):
        if Fourth_part[i] > Fourth_part [i + 1]:
            aux = Fourth_part[i]
            Fourth_part[i] = Fourth_part[i + 1]
            Fourth_part [i + 1] = aux
            Organize = False

Organize = False

for i in range(len(First_part)):
    First_half.append(First_part[i])
for i in range(len(Second_part)):
    First_half.append(Second_part[i])
for i in range(len(Third_part)):
    Second_half.append(Third_part[i])
for i in range(len(Fourth_part)):
    Second_half.append(Fourth_part[i]) 

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