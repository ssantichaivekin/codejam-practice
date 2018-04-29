from random import randint, choice

num = 1000
print(num)
for i in range(num) :
    r = randint(2, 25)
    l = randint(1, r-1)
    print(r, l)
    l2 = [1 for _ in range(l)]
    r -= l
    for i in range(len(l2)) :
        x = randint(0, r)
        if choice([True, False, False, False]) :
            l2[i] += x
            r -= x
        if r == 0 :
            break
    print(*l2)


    