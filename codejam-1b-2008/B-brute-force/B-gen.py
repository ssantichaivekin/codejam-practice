from random import *

print(1000)
for i in range(1000) :
    A = randint(1, 200)
    B = randint(A, 200)
    p = randint(A, B)
    print(A, B, p)