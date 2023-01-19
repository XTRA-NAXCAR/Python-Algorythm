from random import randint
import time

Box = []

for i in range(4000000):
    Number = randint(0, 16000000)
    Box.append(Number)


def Organize(Box):
    if len(Box) > 1:
        half = len(Box) // 2
        First_half = Box[:half]
        Second_half = Box[half:]

        Organize(First_half)
        Organize(Second_half)
        First_indicational = 0
        Second_indicational = 0
        Third_indicational = 0

        while First_indicational< len(First_half) and Second_indicational < len(Second_half):
            if First_half[First_indicational] < Second_half[Second_indicational]:
                Box[Third_indicational] = First_half[First_indicational]
                First_indicational += 1
            else:
                Box[Third_indicational] = Second_half[Second_indicational]
                Second_indicational += 1
            Third_indicational += 1
        
        while First_indicational < len(First_half):
            Box[Third_indicational] = First_half[First_indicational]
            First_indicational += 1
            Third_indicational += 1
        
        while Second_indicational < len(Second_half):
            Box[Third_indicational] = Second_half[Second_indicational]
            Second_indicational += 1
            Third_indicational += 1

start = time.time()

Organize(Box)

final = time.time()
print(final - start)
print(len(Box))