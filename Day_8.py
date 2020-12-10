import os

filename = 'aoc-8.txt'

def load(infile):
    instructions, amounts = [], []
    with open(infile) as f:
        reader = f.readlines()
        for row in reader:
            row = row.replace('\n', '')
            instruction, amount = row.split()
            instructions.append(instruction)
            amounts.append(amount)
    return instructions, amounts


def find_accumulator_total(data):
    total = 0
    already_checked = []
    checked_twice = False
    i = 0
    index = 0
    checklist = []
    instructions, amounts = data[0], data[1]

    while i != len(instructions) - 1:
        current = f'{instructions[i]} {amounts[i]}'

        if 'nop' in current:
            if i in already_checked:
                checked_twice = True
            else:
                already_checked.append(i)
            i += 1
            
            

        if 'acc' in current:
            if i in already_checked:
                checked_twice = True
                if '-' in amounts[i]:
                    total -= int(amounts[i][1:])
                else:
                    total += int(amounts[i][1:])
                break
            else:
                already_checked.append(i)
            
                if '-' in amounts[i]:
                    total -= int(amounts[i][1:])
                else:
                    total += int(amounts[i][1:])
            i += 1
        
            

        if 'jmp' in current:
            if i in already_checked:
                checked_twice = True
            else:
                already_checked.append(i)
        
            if '-' in amounts[i]:
                i -= int(amounts[i][1:])
            else:
                i += int(amounts[i][1:])

    return total

# info = load(filename)
# amount = find_accumulator_total(info)
# print(amount)




