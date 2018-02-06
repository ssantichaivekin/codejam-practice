import math

def nCr(n, r) :
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def generate_trees(n, A, B, C, D, x0, y0, m) :
    trees = []
    x = x0
    y = y0
    trees += [(x, y)]
    for i in range(1, n) :
        x = (A * x + B) % m
        y = (C * y + D) % m
        trees += [(x, y)]
    return trees

def compute_ans(trees) :
    ans = 0
    arr = {}
    for i in range(3) :
        for j in range(3) :
            arr['%d|%d' % (i, j)] = 0
    
    for x, y in trees :
        arr['%d|%d' % (x % 3, y % 3)] += 1
    
    # for key in arr :
        # print(key, arr[key])
    
    for key0 in arr :
        for key1 in arr :
            for key2 in arr :
                num0 = arr[key0]
                num1 = arr[key1]
                num2 = arr[key2]
                x0, y0 = list(map(int, key0.split('|')))
                x1, y1 = list(map(int, key1.split('|')))
                x2, y2 = list(map(int, key2.split('|')))
                
                if (x0 + x1 + x2) % 3 == 0 and (y0 + y1 + y2) % 3 == 0 :
                    if key0 >= key1 >= key2 :
                        if key0 == key1 == key2 :
                            if num0 >= 3 :
                                ans += nCr(num0, 3)
                                # print((x0, y0), '|', (x1, y1), '|', (x2, y2))
                                # print(num0, '1->', nCr(num0, 3))
                        if key0 == key1 > key2 :
                            if num0 >= 2 :
                                ans += nCr(num0, 2) * num2
                                # print((x0, y0), '|', (x1, y1), '|', (x2, y2))
                                # print(num0, num2, '2->', nCr(num0, 2) * num2)
                        if key0 > key1 == key2 :
                            if num1 >= 2 :
                                ans += nCr(num2, 2) * num0
                                # print((x0, y0), '|', (x1, y1), '|', (x2, y2))
                                # print(num0, num2, '3->', nCr(num2, 2) * num0)
                        if key0 > key1 > key2 :
                            poss = num0 * num1 * num2
                            ans += poss
                                # if poss != 0 :
                                    # print((x0, y0), '|', (x1, y1), '|', (x2, y2))
                                    # print('*' * poss)
                
    
    return ans

def brute_force(trees) :
    n = len(trees)
    ans = 0
    for i in range(n) :
        for j in range(i+1, n) :
            for k in range(j+1, n) :
                x0, y0 = trees[i]
                x1, y1 = trees[j]
                x2, y2 = trees[k]
                trees[i] = x0 %3, y0 %3
                trees[j] = x1 %3, y1 %3
                trees[k] = x2 %3, y2 %3
                if (x0 + x1 + x2) % 3 == 0 and (y0 + y1 + y2) % 3 == 0 :
                    ans += 1
                    # print(trees[i], '|', trees[j], '|', trees[k])
                    # print('*')
    return ans

test_cases = int(input())
for case in range(1, test_cases + 1) :
    n, A, B, C, D, x0, y0, m = list(map(int, input().split()))
    ans = compute_ans(generate_trees(n, A, B, C, D, x0, y0, m))
    # ans = brute_force(generate_trees(n, A, B, C, D, x0, y0, m))
    print('Case #%d:' % (case), ans)


    


                    