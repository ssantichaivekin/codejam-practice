

def removedup(all_antlist) :
    x = [ (len(l), sum(l), l) for l in all_antlist ]
    x.sort()
    newlist = [ x[0][2] ]
    for i in range(1, len(x)) :
        if x[i][0] != x[i-1][0] :
            newlist += [ x[i][2] ]
    return newlist


test_cases = int(input())
for case in range(1, test_cases + 1) :
    n = int(input())
    ants = list(map(int, input().split()))
    all_antlist = [[]]

    for ant in ants :
        newlists = []
        for antlist in all_antlist :
            # Case can add :
            # Trying adding itself to the list
            # If available, then that's good.
            if sum(antlist) <= 6 * ant :
                antlist += [ant]
            # Case cannot add :
            # If can't immediately add, remove
            # the biggest ant from the list,
            # and create a new list
            else :
                new_antlist = list(antlist)
                while sum(new_antlist) > 6 * ant :
                    new_antlist.remove(max(new_antlist))
                new_antlist += [ant]
                newlists += [new_antlist]
        all_antlist += newlists
        
        all_antlist = removedup(all_antlist)
    print(all_antlist)

    print('Case #%d:' % case, len(all_antlist[-1]))