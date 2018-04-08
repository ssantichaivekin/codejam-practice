import sys


test_cases = int(input())
for case in range(1, test_cases+1) :
    size = int(input())
    y = 15
    x = 14
    isDug = [[False for j in range(y)] for i in range x]


    while x != 0 and y != 0 :
        # print something
        print(currentx, currenty)
        sys.stdout.flush()
        
        # read something
        y, x = list(map(int, input().split()))
        if y == -1 and x == -1 :
            sys.exit()

