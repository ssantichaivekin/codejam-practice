def finddamage(seq) :
    power = 1
    damage = 0
    for x in seq :
        if x == 'S' :
            damage += power
        else :
            power *= 2
    return damage

def swapclosest(seq) :
    # return True upon sucessful swap
    # return False upon cannot swap
    index_swap = -1
    for i in range(len(seq)-1) :
        # print(seq[i:i+2])
        if seq[i:i+2] == ['C', 'S'] :
            index_swap = i

    if index_swap == -1 :
        return False
    else :
        seq[index_swap], seq[index_swap+1] = seq[index_swap+1], seq[index_swap]
        return True

test_cases = int(input())
for case in range(1, test_cases+1) :
    s = input().split()
    shield = int(s[0])
    seq = list(s[1])
    count = 0
    isvalid = True
    while finddamage(seq) > shield :
        result = swapclosest(seq)
        if result :
            count += 1
        else :
            isvalid = False
            break
    
    if isvalid :
        print('Case #%d:' % (case), count)
    else :
        print('Case #%d:' % (case), 'IMPOSSIBLE')
