from queue import PriorityQueue

def get_dec(num) :
    return num - int(num)

def num_to_pass(init, person_val) :
    # print('>', init, person_val)
    if get_dec(person_val) == 0 :
        return 1
    # print(get_dec(init), get_dec(person_val))
    # print('>', int((0.5 - get_dec(init))/get_dec(person_val) + 1))
    # print((0.5 - get_dec(init))/get_dec(person_val))
    if get_dec(person_val) >= 0.5 :
        if init > 0 :
            return 0
        else :
            return 1
    if get_dec(init) >= 0.5 :
        return 0
    return int((0.5 - get_dec(init+0.0000001))/get_dec(person_val) + 1)

def get_tup(init, person_val) :
    return (num_to_pass(init, person_val), init)

def build_queue(lang_list, person_val) :
    q = PriorityQueue()
    for n_people in lang_list :
        q.put(get_tup(n_people * person_val, person_val))
    for _ in range(10) :
        q.put(get_tup(0, person_val))
    return q

test_cases = int(input())
for case in range(1, test_cases + 1) :
    people, num_lang = list(map(int, input().split()))
    lang_list = list(map(int, input().split()))
    person_val = 100 / people
    people -= sum(lang_list)
    # print(case)
    # print(lang_list, person_val)
    q = build_queue(lang_list, person_val)
    # while not q.empty() :
    #     print(q.get())
    l = []
    # while not q.empty() :
    #     print(q.get())
    while not q.empty() :
        if people == 0 :
            break
        num, init = q.get()
        # print(num, init, people)
        if num == 0 :
            l += [ int(init+0.5) ]
            # print(int(init+0.5))
            q.put(get_tup(0, person_val))
            continue
        for _ in range(num) :
            # print(init, person_val)
            init += person_val
            people -= 1
            if people == 0 :
                break
        # print(people)
        q.put(get_tup(init, person_val))
    # while not q.empty() :
    #     print(q.get())
    # print(l)
    while not q.empty() :
        l += [int((q.get()[1])+0.5)]
    print('Case #%d: %d' % (case, sum(l)))




