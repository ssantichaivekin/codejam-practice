import sys

def gen_square(y, x) :
    for i in range(1, y+1) :
        for j in range(1, x+1) :
            yield (i, j)

def dig_here(maxy, maxx, holei, holej) :
    holei += 1
    holej += 1
    if holei >= maxy :
        holei -= 1
    if holej >= maxx :
        holej -= 1
    return holei, holej

test_cases = int(input())
for case in range(1, test_cases+1) :
    size = int(input())
    # dig from i = 1 -> 15 inclusive
    maxy = 15
    # dig from j = 1 -> 14 inclusive
    maxx = 14

    isDug = [[False for j in range(maxy+4)] for i in range(maxx+4)]

    for posi, posj in gen_square(maxy, maxx) :
        quit = False
        while(not isDug[posi][posj]) :
            
            # print something
            digi, digj = dig_here(maxy, maxx, posi, posj)
            sys.stderr.write(' '.join([str(digi), str(digj)])+'\n')
            print(digi, digj)
            sys.stdout.flush()
            
            # read something
            y, x = list(map(int, input().split()))
            if y == 0 and x == 0 :
                quit = True
                break
            if y == -1 and x == -1 :
                sys.exit()
            isDug[y][x] = True
        
        if(quit) :
            break

