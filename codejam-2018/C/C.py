import sys

if __name__ == '__main__' :
    test_cases = int(input())
    for case in range(1, test_cases+1) :
        size = int(input())
        y = -2
        x = -2
        minx = 2
        miny = 2
        maxx = 7
        maxy = 6
        currentx = 2
        currenty = 2
        tcurr = 0
        tmax = 50

        while x != 0 and y != 0 :
            # print something
            print(currentx, currenty)
            sys.stdout.flush()
            tcurr += 1
            if tcurr == tmax :
                tcurr = 0
                currenty += 1
            if currenty == maxy :
                currenty = 2
                currentx += 1
            

            # read something
            y, x = list(map(int, input().split()))
            if y == -1 and x == -1 :
                sys.exit()

