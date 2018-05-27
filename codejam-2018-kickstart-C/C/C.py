p = 1000000007

def wakeup(const, k, order, p) :
    # print(const, k, order)
    val = 0
    for i in range(1, k+1) :
        # k is the order-power
        mul = order ** i
        val += mul
    ans = (const * val) % p
    # print('>', const, val, ans)
    return ans



def power(A, k, p) :
    # k is the number of wake up calls
    sumval = 0
    for i in range(1, len(A)+1) :
        sumval += wakeup(A[i-1], k, i, p)
        sumval %= p
    return sumval

test_cases = int(input())
for case in range(1, test_cases+1) :
    n, k, x1, y1, c, d, e1, e2, f = list(map(int, input().split()))
    X = [0, x1]
    Y = [0, y1]
    sumval = 0
    for i in range(2, n+1) :
        xi = (c*X[i-1] + d*Y[i-1] + e1) % f
        yi = (d*X[i-1] + c*Y[i-1] + e2) % f
        X += [xi]
        Y += [yi]
    A = [(x+y)%f for x, y in zip(X,Y)]
    A = transform(A)
    for w_size in range(1, n+1) :
        # choose the size of the window
        for start in range(1, n+2-w_size) :
            # choose the start position
            sumval += power(A[start:start+w_size], k, p)
            sumval %= p
    print('Case #%d:' % case, sumval)

            


