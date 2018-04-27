from math import sqrt

def merge(range1, range2) :
    # Get two ranges, merge them
    merged_range = sorted(range1 + range2)
    new_range = [merged_range[0]]
    for start, end in merged_range[1:] :
        last = new_range[-1]
        last_start, last_end = last
        # Normal case
        if start > last_end :
            new_range += [(start, end)]
        # Merge case
        else :
            new_range[-1] = (last_start, max(end, last_end))
    return new_range



test_cases = int(input())
for case in range(1, test_cases + 1) :
    n, expected_sum = list(map(int, input().split()))
    range_cookies = []
    init_sum = 0
    for _ in range(n) :
        x, y = list(map(int, input().split()))
        init_sum += 2*x+2*y
        start = 2 * min(x,y)
        end = 2 * sqrt(x**2+y**2)
        range_cookies += [(start, end)]

    # Start with no cut
    range_total = [(0,0)]
    # We will calculate the temp range (new range to be added)
    # From the new cookie and the current toral range.
    # Then we will merge the temp range back to the total range.
    for start, end in range_cookies :
        range_temp = []
        for t_start, t_end in range_total :
            n_start = t_start + start
            n_end = t_end + end
            range_temp += [(n_start, n_end)]
        range_total = merge(range_total, range_temp)

    for i in range(len(range_total)) :
        range_total[i] = (range_total[i][0]+init_sum,range_total[i][1]+init_sum)
    
    # Consider that we have already computed cookies with any number
    range_total += [(10**10, 10**10)]

    # print(range_total)
    
    is_answered = False
    for start, end in range_total :
        # print(start, expected_sum, end)
        if start <= expected_sum <= end :
            print('Case %d: %.6f' % (case, expected_sum))
            is_answered = True
            break
    
    if not is_answered :
        for i in range(len(range_total)) :
            if range_total[i][0] > expected_sum :
                print('Case %d: %.6f' % (case, range_total[i-1][1]))
                break




