from queue import Queue

def trace(start, end, visited_from) :
    cycle_list = []
    curr = start
    while True :
        cycle_list += [curr]
        if curr == end :
            break
        curr = visited_from[curr]
    return cycle_list

def paint_cycle(edges) :
    visited_from = [False for _ in range(len(edges))]
    stack = []
    stack.append((1, -1))
    while stack :
        curr, last = stack.pop()
        if visited_from[curr] :
            # case there is a cycle
            # trace back from last to curr
            return trace(last, curr, visited_from)
        visited_from[curr] = last
        for child in edges[curr] :
            # iterate into other children that is not last
            if child != last :
                stack.append((child, curr))

def find_dist(starts, edges) :
    dists = [ -1 for _ in range(len(edges))]
    q = Queue()
    # print(starts)
    for start in starts :
        q.put((start, 0))
    while not q.empty() :
        node, dist = q.get()
        if dists[node] == -1 :
            # print(node,dist)
            dists[node] = dist
            for child in edges[node] :
                q.put((child, dist+1))
    return dists



test_cases = int(input())
for case in range(1, test_cases + 1) :
    n = int(input())
    # Note that edges[0] is always empty
    # edges is indexed from 1..n
    edges = [ [] for _ in range(n + 1)]
    for _ in range(n) :
        x, y = list(map(int, input().split()))
        edges[x] += [y]
        edges[y] += [x]
    cycle_list = paint_cycle(edges)
    ans = find_dist(cycle_list, edges)
    ans = ans[1:]
    print('Case #%d:' % case, *ans)
    

    





    
