'''
I will write a very well-seructured b-search based program.
'''

def bsearch_answer(condfunc, start, end) :
    '''
    Find the first integer in the range [start, end) that
    satisfies the condition function condfunc(x).
    Note that confunc(x) is a boolean function.
    Return that integer.
    We assume that there is at least one mumber in the range that
    satisfies the function, and that if x satisfies, then y > x also
    satisfies the function.
    '''
    if end - start == 1 :
        # The range is of length 1. Therefore, by our assumption
        # the number satisfies the function.
        return start
    mid = (start+end-1)//2
    if condfunc(mid) :
        # The mid satisfies the condition. Test mid and things before.
        return bsearch_answer(condfunc, start, mid+1)
    else :
        # The mid DOES NOT satisfies the condition.
        # Test the things strictly after the mid.
        return bsearch_answer(condfunc, mid+1, end)
    
def cancarrybits(n_bits, n_robots, cashiers, time) :
    # Fill each counter such that it does not exceed the
    # calculation of time. Note that if we have limited robots,
    # Then we will have to prioritize only the first ones
    # that we can carry.
    required_bits = n_bits
    bits_list = []
    for maxitem, cost_per_item, added_cost in cashiers :
        bits = (time - added_cost)//cost_per_item
        bits = min(maxitem, bits)
        bits_list += [bits]
    bits_list.sort(reverse=True)
    # print(time, ':', bits_list, bits_list[:n_robots])
    ans = sum(bits_list[:n_robots]) >= required_bits
    return ans


test_cases = int(input())
for case in range(1, test_cases+1) :
    n_robots, n_bits, n_cashiers = list(map(int, input().split()))
    cashiers = []
    for _ in range(n_cashiers) :
        maxitem, cost_per_item, added_cost = list(map(int, input().split()))
        cashiers += [(maxitem, cost_per_item, added_cost)]
    
    condfunc = lambda t: cancarrybits(n_bits, n_robots, cashiers, t)
    ans = bsearch_answer(condfunc, 0, 10**10)
    print('Case #%d: %d' % (case, ans))

