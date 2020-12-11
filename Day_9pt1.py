from collections import deque
from copy import deepcopy

filename = 'aoc-9.txt'

def load(infile):
    with open(infile) as f:
        reader = f.readlines()
        nums = [int(row.replace('\n', '')) for row in reader]
        
    return nums

def find_number(data):
    ftf_copy = deepcopy(data[:25])
    first_twenty_five = deque(data[i] for i in range(25))
    the_rest = deque(data[i] for i in range(25, len(data)))
    found_addends = set()
    
    i = 0
    k = 0
    index = 0
    
    while len(the_rest) != 1:
        current_addend = first_twenty_five[i]
        number = the_rest[0]

        for j in range(len(first_twenty_five)):
            second_addend = first_twenty_five[j]
            if current_addend + second_addend == number and number not in ftf_copy:
                found_addends.add(number)
    
        if i == len(first_twenty_five) - 1:
            i = 0
        else:
            i += 1
        
        if index == 625:
            first_twenty_five.popleft()
            first_twenty_five.append(the_rest[0])
            the_rest.popleft()
            index = 0
        
        index += 1

    not_found = set(data) - found_addends
    return not_found - set(ftf_copy)

info = load(filename)
print(find_number(info))


