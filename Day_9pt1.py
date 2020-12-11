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
    return list(not_found - set(ftf_copy))[0]


def part_two(num, data):
    data.remove(num)
    total = 0
    addends = []

    for i in range(len(data)):
        initial_number = data[i]
        addends.append(initial_number)
        for j in range(i+1, len(data)):
            other_num = data[j]
            addends.append(other_num)
            total = sum(addends)
        
            if total > num:
                addends.clear()
                continue
            else:
                if total == num:
                    return min(addends) + max(addends)
        
        addends.clear()
        


    


info = load(filename)
number = find_number(info)
addends = part_two(number, info)
print(addends)


