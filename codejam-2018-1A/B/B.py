def cal_cost(sorted_cashiers, deleted, n) :
    # calculate the cost of everything.
    # return -1 if impossible
    total_cost = 0
    for i, cashier in zip(range(len(sorted_cashiers)), sorted_cashiers) :
        if deleted[i] :
            continue
        s, p, m = cashier
        # m = max
        # s = cost per q
        # p = fixed cost
        fill = min(n, m)
        cost = fill * s + p
        total_cost += cost
        n -= fill

        if n == 0 :
            break
        
    if n > 0 :
        return -1
    return total_cost
    

test_cases = int(input())
for case in range(1, test_cases + 1) :
    print('Case #%d: ' % case, end = '')
    robots, n, c = list(map(int, input().split()))
    cashiers = [ [] for x in range(c)]
    deleted = [ False for x in range(c)]
    for i in range(c) :
        m, s, p = list(map(int, input().split()))
        # m = max, s = cost per q, p = fixed cost
        cashiers[i] = (s, p, m)
    cashiers.sort()
    cost = float('inf')
    print(cal_cost(cashiers, deleted, n))

