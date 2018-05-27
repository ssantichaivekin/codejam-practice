def sumarr(x) :
    sumval = 0
    arr = []
    for val in x:
        sumval += val
        arr += [sumval]
    return arr

def reverse_row(A, i, j) :
    return A[:i] + list(reversed(A[i:j])) + A[j:]

def reverse_all(arr, i, j) :
    # reverse each row in arr
    newarr = []
    for A in arr :
        newarr += [reverse_row(A, i, j)]
    return newarr

def reverse_special(arr) :
    des = arr[-2]
    ranges = []
    i = 0
    while i < len(arr) :
        if des[i] == '\\' or des[i] == '/' :
            start = i
            while des[i+1] == des[i] :
                i += 1
            end = i + 1
            ranges += [(start, end)]
        i += 1
    for start, end in ranges:
        arr = reverse_all(arr, start, end)
    return arr


test_cases = int(input())
for case in range(1, test_cases+1) :
    n = int(input())
    final = list(map(int, input().split()))
    curr = [1 for _ in range(n)]
    ans = [['.' for _ in range(n)]]
    impossible = False
    # print('curr:', curr)
    # print('final:', final)
    while final != curr :
        sumcurr = sumarr(curr)
        sumfinal = sumarr(final)
        mutate = ['.' for _ in range(n)]
        for i in range(1, n-1) :
            ansset = []
            # check i-1 position
            # this allows us to put the / sign
            if sumcurr[i-1] < sumfinal[i-1] :
                # add '/'
                ansset += '/'
                # TODO: add case cannot remove
                curr[i-1] += 1
                curr[i] -= 1
            # check i position
            # this allows us to put the \ sign
            if sumcurr[i] > sumfinal[i] :
                # add '\'
                ansset += '\\'
                # TODO: add case cannot remove
                curr[i] -= 1
                curr[i+1] += 1
            # case ansset clashes: doing both / and \
            # if ansset = [] : do nothing
            # print('0', curr)
            # print('A:', sumarr(curr))
            # print('B:', sumarr(final))
            if len(ansset) == 1 :
                mutate[i] = ansset[0]
            if len(ansset) == 2 :
                impossible = True
                break
        # test the impossible case :
        if impossible :
            break
        # test over the limit case (repeating ans) :
        if len(ans) > n + 2:
            impossible = True
            break
        ans += [mutate]
        # print(mutate)
    if impossible :
        print('Case #%d:' % case, 'IMPOSSIBLE')
        continue

    print('Case #%d:' % case, len(ans))
    ans.reverse()
    if len(ans) > 1 :
        ans = reverse_special(ans)
    for row in ans :
        print(''.join(row))
    # print('---')
