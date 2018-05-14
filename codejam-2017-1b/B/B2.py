from itertools import zip_longest

test_cases = int(input())
for case in range(1, test_cases+1) :
    n, r, o, y, g, b, v = list(map(int, input().split()))
    normalcol = [r, y, b]
    speccol = [g, o, v]
    col_list = [('R', 'G'), ('Y', 'O'), ('B', 'V')]
    end = False
    for n1, n2, cols in zip(normalcol, speccol, col_list) :
        if n1 == n2 and sum(normalcol) == sum(speccol) == n1 :
            col1, col2 = cols
            col = col1+col2
            ans = col * n1
            print('Case #%d:' % case, ans)
            end = True
            break
    if end :
        continue
    alllist = []
    for n_normal, n_spec, cols in zip(normalcol, speccol, col_list) :
        if n_normal != 0 and n_normal <= n_spec :
            print('Case #%d:' % case, 'IMPOSSIBLE')
            end = True
            break
        n_normal -= n_spec + 1
        normalcol, speccol = cols
        specstring = normalcol + (speccol + normalcol) * n_spec
        strlist = [specstring] + [normalcol for _ in range(n_normal)]
        alllist += [strlist]
    #     print(len(strlist))
    # print(alllist)
    # print([len(x) for x in alllist])
    if end :
        continue
    redlist = ['R' for _ in range(r)]
    yellowlist = ['Y' for _ in range(y)]
    bluelist = ['B' for _ in range(b)]
    alllist = [redlist, yellowlist, bluelist]
    alllist.sort(key=len)
    dominant = alllist[2]
    highsub = alllist[1]
    lowsub = alllist[0]
    num_merge = len(lowsub) + len(highsub) - len(dominant)
    if num_merge < 0 :
        print('Case #%d:' % case, 'IMPOSSIBLE')
        continue
    mergearr = [x+y for x, y in zip(lowsub, highsub)][:num_merge]
    lowsub = lowsub[num_merge:]
    highsub = highsub[num_merge:]
    mergefull = mergearr + lowsub + highsub
    ans = ''.join([x+y for x, y in zip(dominant, mergefull)])
    print('Case #%d:' % case, ans)
    