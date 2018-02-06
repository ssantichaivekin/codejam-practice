#!usr/env/bin bash

# write a function that recieves
# a long decimal and get only the
# first 3 digits before the decimal
# point

trim_dec() {
    echo ''
}

# write a function that uses bc to
# find the answer of a^n

find_ans() {
    echo $( bc <<< "scale=1000; (3+sqrt(5))^${1}" )
}

# in main, create an array of size 100, keeping
# the answer for each n
# create another array to check for repeating n
#