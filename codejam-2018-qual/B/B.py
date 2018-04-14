def firstlarger(l) :
    for i in range(len(l)-1) :
        if l[i] > l[i+1] :
            return i

test_cases = int(input())
for case in range(1, test_cases+1) :
    n = int(input())
    l = list(map(int, input().split()))

    lx = [[], []]
    for i in range(n) :
        if i % 2 == 0 :
            lx[0] += [l[i]]
        else :
            lx[1] += [l[i]]
    
    lx[0].sort()
    lx[1].sort()

    last = []

    for i in range(n) :
        where = i % 2
        at = i // 2
        last += [lx[where][at]]

    print('Case #%d:' % (case), end=' ')
    if sorted(last) == last :
        print('OK')
    else :
        print(firstlarger(last))


