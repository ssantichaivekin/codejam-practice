import sys

if __name__ == '__main__' :
    test_cases = int(input())
    for case in range(1, test_cases+1) :
        size = int(input())


        while x != 0 and y != 0 :
            # print something
            print(currentx, currenty)
            sys.stdout.flush()
            
            # read something
            y, x = list(map(int, input().split()))
            if y == -1 and x == -1 :
                sys.exit()

