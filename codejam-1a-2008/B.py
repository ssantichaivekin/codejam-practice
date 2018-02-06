def valid_pref(person_pref, malted_list) :
    for flavor in person_pref :
        if type(flavor) is int :
            if person_pref[flavor] == malted_list[flavor] :
                return True
    return False

test_cases = int(input())
for case in range(1, test_cases + 1) :
    n_flavors = int(input())
    n_people = int(input())
    people = []
    for person in range(n_people) :
        input_pref = list(map(int, input().split()))
        input_pref = input_pref[1:]
        prefs = {}
        for i in range(len(input_pref) // 2) :
            flav = input_pref[2*i]
            malted = input_pref[2*i+1]
            prefs[flav] = malted
            if malted :
                prefs['malted_flav'] = flav
        people += [prefs]


    malted_list = [0 for i in range(n_flavors + 1)]
    need_malted = []
    impossible = False
    # print(people)
    while True :
        # check whether the malted list is valid
        # meaning that it should satisfy all people
        changed_malted = False

        for person_pref in people :
            # check whether it is valid
            # if it is valid, just ignore the person.
            # print('~', person_pref)
            # print(malted_list)
            # print(valid_pref(person_pref, malted_list))
            if not valid_pref(person_pref, malted_list) :
                # if not valid, check whether we can change
                # one of the flav to malted
                # check malted
                if 'malted_flav' in person_pref :
                    if malted_list[person_pref['malted_flav']] :
                        # if the malted flavor is already malted
                        # but the flavors are still invalid
                        impossible = True
                        break
                    else :
                        # if the malted flavor has not yet been
                        # changed
                        changed_malted = True
                        malted_list[person_pref['malted_flav']] = 1
                        break
                # if we can't then we are doomed
                else :
                    impossible = True
                    break
        
        if impossible :
            break
        if not changed_malted :
            break
    print("Case #%d:" % case, end = ' ')
    if impossible :
        print("IMPOSSIBLE")
    else :
        print(*malted_list[1:])
    
