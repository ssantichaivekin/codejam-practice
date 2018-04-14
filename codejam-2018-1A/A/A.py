def row_count_cookies(pan, i) :
    # count cookies in row i
    return sum(pan[i])    

def col_count_cookies(pan, j) :
    # count cookies in col j
    R = len(pan)
    cookies = 0
    for i in range(R) :
        cookies += pan[i][j]
    return cookies

def row_arrange_cookies(pan, cookies_per_row) :
    R = len(pan)
    C = len(pan[0])
    cut = [0]
    cookies_now = 0
    for i in range(R) :
        # go row by row :
        count = row_count_cookies(pan, i)
        cookies_now += count
        if cookies_now == cookies_per_row :
            cookies_now = 0
            cut += [i+1]
        if cookies_now > cookies_per_row :
            return False
    return cut


def col_arrange_cookies(pan, cookies_per_col) :
    R = len(pan)
    C = len(pan[0])
    cut = [0]
    cookies_now = 0
    for j in range(C) :
        # go by col :
        count = col_count_cookies(pan, j)
        cookies_now += count
        # print(count, end = '/')
        # print(cookies_now, end = '//')
        if cookies_now == cookies_per_col :
            cookies_now = 0
            cut += [j+1]
        if cookies_now > cookies_per_col :
            # this is just an assumption
            # we might have to rewrite
            # the col arrange to return the num cut
            return False
    return cut

def count_cookies(pan, j1, j2) :
    count = 0
    for i in range(len(pan)) :
        count += sum(pan[i][j1:j2])
    return count

test_cases = int(input())
for case in range(1, test_cases + 1) :
    print('Case #%d: ' % (case), end='')
    R, C, h, v = list(map(int, input().split()))
    pan = [ [] for i in range(R) ]
    for i in range(R) :
        pan[i] = list(input())

    total_cookies = 0
    for i in range(R) :
        for j in range(C) :
            if pan[i][j] == '@' :
                pan[i][j] = 1
                total_cookies += 1
            else :
                pan[i][j] = 0
    
    if total_cookies % (h+1) != 0 :
        print('IMPOSSIBLE')
        continue
    if total_cookies % (v+1) != 0 :
        print('IMPOSSIBLE')
        continue

    cookies_per_row = total_cookies / (h+1)
    cookies_per_col = total_cookies / (v+1)
    cookies_per_block = total_cookies / (h+1) / (v+1)
    cut_row = row_arrange_cookies(pan, cookies_per_row)
    cut_col = col_arrange_cookies(pan, cookies_per_col)
    #print(cut_row, cut_col)
    if not (cut_row and cut_col) :
        print('IMPOSSIBLE')
        continue
    
    valid = True
    for i in range(len(cut_row)-1) :
        for j in range(len(cut_col)-1) :
            #print((cut_row[i],cut_row[i+1]), (cut_col[j],cut_col[j+1]))
            pan2 = pan[cut_row[i]:cut_row[i+1]]
            #print(pan2, cut_col[j], cut_col[j+1])
            count = count_cookies(pan2, cut_col[j], cut_col[j+1])
            #print(count)
            if count != cookies_per_block :
                valid = False
                break
    
    if valid :
        print('POSSIBLE')
    else :
        print('IMPOSSIBLE')



    