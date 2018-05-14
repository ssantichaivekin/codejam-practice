from itertools import zip_longest

test_cases = int(input())
for case in range(1, test_cases+1) :
    n, r, o, y, g, b, v = list(map(int, input().split()))
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
    