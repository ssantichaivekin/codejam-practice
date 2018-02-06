test_cases = int(input())
for test in range(1, test_cases + 1) :
    size = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    x.sort()
    y.sort(reverse=True)
    print("Case #%d:" % (test), sum([x[i] * y[i] for i in range(size)]))