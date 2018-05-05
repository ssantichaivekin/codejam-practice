def get_unique_elem(pos, words) :
    '''
    Get the unique elements of each position.
    The position starts from 0 to len(word) exclusive.
    '''
    chars = [ word[pos] for word in words ]
    chars = list(set(chars))
    chars.sort()
    return chars

def gen_string(gen_arr) :
    '''
    Generate string from gen_arr in dictionary order.
    '''
    l = len(gen_arr)
    seq = [ 0 for _ in range(l) ]

    # Counting part
    while True :
        out = [ gen_arr[i][seq[i]] for i in range(l) ]
        yield ''.join(out)
        seq[-1] += 1
        for i in range(l-1, -1, -1) :
            if seq[i] >= len(gen_arr[i]) :
                if i == 0 :
                    return
                else :
                    seq[i-1] += 1
                    seq[i] = 0
            else :
                break


test_cases = int(input())
for case in range(1, test_cases + 1) :
    n, l = list(map(int, input().split()))
    words = []
    for _ in range(n) :
        words += [ input() ]
    words = list(set(words))
    words.sort()
    gen_arr = []
    for i in range(l) :
        gen_arr += [get_unique_elem(i, words)]

    ans = '-'
    for gen_s, curr_s in zip(gen_string(gen_arr), words + ['']) :
        if gen_s != curr_s :
            ans = gen_s
            break

    print('Case #%d: ' % case, ans)