from math import *

def gen_prime(maxprime) :
    primearr = []
    for i in range(2, maxprime) :
        isprime = True
        for p in primearr :
            if i % p == 0 :
                isprime = False
                break
        if isprime :
            primearr += [i]
    return primearr

def share_prime(x, y, p, primearr) :
    if x > y :
        x, y = y, x
    
    for i in primearr :
        if i >= p and x % i == 0 and y % i == 0 :
            return True
    
    return False

def calculate_group(start, end, p) :
    group = {}
    primearr = gen_prime(end+10)
    for x in range(start, end + 1) :
        group[x] = x
    
    for i in range(start, end + 1) :
        # mingroup = group[i]
        # grouplist = [i]
        for j in range(i + 1, end + 1) :
            if share_prime(i, j, p, primearr) :
                #if group[j] < mingroup :
                #    mingroup = group[j]
                min_group = min(group[i], group[j])
                group[i] = min_group
                group[j] = min_group
                # print('Group %d %d <= %d' % (i, j, min_group))
        #        grouplist += [j]
        # for i in grouplist :
        #    group[i] = mingroup
    
    groups = group.values()
    #for key in sorted(group.keys()) :
    #    print('%d|%d' % (key, group[key]))
    unique_groups = set(groups)
    #print(sorted(unique_groups))
    ans = len(unique_groups)
    return unique_groups

# test_cases = int(input())
# for case in range(1, test_cases + 1) :
#     a, b, p = list(map(int, input().split()))
#     ans = calculate_group(a, b, p)
#     print('Case #%d:' % (case), ans)
    
    
