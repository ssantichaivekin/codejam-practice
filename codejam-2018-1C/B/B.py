import sys

test_cases = int(input())
for case in range(1, test_cases + 1) :
    n = int(input())
    commonness = {}
    # Initialize available flavors to 0.
    for flav in range(n) :
        commonness[flav] = 0
    # Input loop :
    for _ in range(n) :
        prefs = list(map(int, input().split()))
        if prefs[0] == 0 :
            print(-1)
            sys.stdout.flush()
            continue
        if prefs[0] == -1 :
            sys.exit()

        # Loop through all the flavors the customer wants
        # Give the customer the rarest flavor
        # Add all other flavors to the commonness of flavors
        prefs = prefs[1:]
        min_flav = -1
        min_val = 10**10
        for flav in prefs :
            if flav in commonness :
                if commonness[flav] < min_val :
                    min_flav = flav
                    min_val = commonness[flav]
        
        if min_flav != -1 :
            # Has a flavor one can offer :
            del commonness[min_flav]
            print(min_flav)
            sys.stdout.flush()
            # Add all other flavors to the commonness of flavors
            prefs.remove(min_flav)
            for flav in prefs :
                if flav in commonness :
                    commonness[flav] += 1
        else :
            # Cannot offer anything
            print(-1)
            sys.stdout.flush()