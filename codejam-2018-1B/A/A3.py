def div_round_up(x, y) :
    # print(x, y)
    '''
    Return x/y rounded up.
    '''
    return (x+y-1)//y

def div_round(x, y) :
    '''
    Return x/y rounded to the nearest 0.0
    '''
    return (x+y//2)//y

def calculate_percent(n, x) :
    '''
    Return the rounded percent.
    '''
    return div_round(100*x, n)

def is_rounding_up(n, x) :
    '''
    Given
    n: total number of people in polls,
    x: people in this specific language
    Find whether the language is already rounding up.
    '''
    return 2*(100*x%n) >= n

def min_to_round(n, x) :
    '''
    Given
    n: total number of people in polls,
    x: people in this specific language
    Assuming that dec(x) < 0.5 and the language is not
    rounding up, find the minimum people the langauge
    requires for it to be rounding up.
    '''
    # print(n, x)
    return div_round_up(n-2*(100*x%n), 2*(100%n))

def find_to_round(n, x) :
    '''
    Return how many people we should add to this existing language.
    '''
    if 100 % n == 0 :
        # This means it won't matter.
        # Doing this anyway is fine.
        # Basically, just do it.
        return 10**6
    if is_rounding_up(n, 1) :
        # Better to have 1 1 1 1 1 as the language
        return 0
    if is_rounding_up(n, x) :
        # The language is already rounding up.
        # Don't do anything.
        return 0
    # Return the number of elements required to round.
    return min_to_round(n, x)

test_cases = int(input())
for case in range(1, test_cases + 1) :
    n, l = list(map(int, input().split()))
    lang = list(map(int, input().split()))
    n_left = n - sum(lang)
    lang = [ (find_to_round(n, x), x) for x in lang ]
    lang.sort()
    sum_percent = 0
    # Loop through the languages in the poll :
    for todo, num in lang :
        willdo = min(todo, n_left)
        n_left -= willdo
        num += willdo
        percent = calculate_percent(n, num)
        # print('>>', percent)
        sum_percent += percent

    # find the number per language we will use
    # Note that we don't have to care for the case
    # where n % 100 == 0 since we will have at least
    # one element in the language.
    if n_left > 0 :
        num_per_lang = min_to_round(n, 0)
        # filled_lang is the number of filled langugaes
        filled_lang = n_left // num_per_lang
        n_left -= filled_lang * num_per_lang
        sum_percent += calculate_percent(n, num_per_lang) * filled_lang
        sum_percent += calculate_percent(n, n_left)
        n_left = 0
    
       
    print('Case #%d:' % case, sum_percent)

    


