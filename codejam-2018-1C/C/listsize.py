def listsize() :
    antlist = [1]
    while True :
        newant = (sum(antlist)+5)//6
        if newant > 10**9 :
            break
        antlist += [newant]
    return antlist

if __name__ == '__main__' :
    print(len(listsize()), listsize())