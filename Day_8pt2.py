import os
from Day_8 import find_accumulator_total
from copy import deepcopy

filename = 'aoc-8.txt'

path = os.path.join('C:/Users/jbrink.ccpsweb/Desktop/', filename)


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


def fix_instructions(data):
    already_checked = []
    checked_twice = False
    i = 0
    instructions, amounts = data[0], data[1]
    checklist = []
    index = 0
    stopping_point = None

    while not checked_twice:
        if instructions[i] == 'nop':
            if instructions[i] + ' ' + amounts[i] in checklist:
                print(instructions[i])
                checked_twice = True
                break
            else:
                checklist.append(instructions[i] + ' ' + amounts[i])
            i += 1

        if instructions[i] == 'acc':
            checklist.append(instructions[i] + ' ' + amounts[i])
            i += 1

        if instructions[i] == 'jmp':
            if instructions[i] + ' ' + amounts[i] in checklist:
                print(instructions[i])
                checked_twice = True
                break
            else:
                if '-' in amounts[i]:
                    i -= int(amounts[i][1:])
                else:
                    i += int(amounts[i][1:])

    instructions[len(checklist)] = 'jmp'
    return instructions, amounts
    
##    while not checked_twice:
##        if instructions[i] == 'nop':
##            if i in already_checked:
##                checked_twice = True
##                index += 1
##                break
##            else:
##                already_checked.append(i)
##                i += 1
##                index += 1
##            
##
##        if instructions[i] == 'acc':
##            if i in already_checked:
##                checked_twice = True
##                index += 1
##                break
##            else:
##                already_checked.append(i)
##                i += 1
##                index += 1
##            
##
##        if instructions[i] == 'jmp':
##            if i in already_checked:
##                checked_twice = True
##                index += 1
##                break
##            else:
##                already_checked.append(i)
##                if '-' in amounts[i]:
##                    i -= int(amounts[i][1:])
##                else:
##                    i += int(amounts[i][1:])
##
##                index += 1

    
##    instructions[10] = 'nop'
##    
##    return instructions, amounts

        




info = load(path)
amount = fix_instructions(info)
#final = find_accumulator_total(amount)
print(find_accumulator_total(amount))

