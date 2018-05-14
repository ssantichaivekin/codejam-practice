test_cases = int(input())
for case in range(1, test_cases+1) :
    dist, n = list(map(int, input().split()))
    maxh = 0
    for _ in range(n) :
        start, speed = list(map(int, input().split()))
        hour = (dist-start)/speed
        if hour > maxh :
            maxh = hour
    myspeed = dist / maxh
    print('Case #%d:' % case, '%.6f' % myspeed)
