import os
#from Day_8 import find_accumulator_total
from copy import deepcopy

filename = 'test_data.txt'

#path = os.path.join('C:/Users/jbrink.ccpsweb/Desktop/', filename)



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


def correct_instructions(data):
    total = 0
    i = 0
    already_checked = []
    instructions, amounts = data[0], data[1]
    index = 0
    end = instructions[-1]
    ultimate = f'{instructions[-1]} {amounts[-1]}'
    current = None

    while current != ultimate :
        current = f'{instructions[i]} {amounts[i]}'
        
        if 'nop' in current:
            if i in already_checked:
                print(f'This is the problem: {index-1, i}')
                break
                
            else:
                already_checked.append(i)
            i += 1
            index += 1
            print(instructions[i], amounts[i])
            print(f'Index: {index}')

        
        if 'acc' in current:
            if i in already_checked:
                print('ok')
            else:
                already_checked.append(i)
            
                if '-' in amounts[i]:
                    total -= int(amounts[i][1:])
                else:
                    total += int(amounts[i][1:])
            i += 1
            index += 1
            print(instructions[i], amounts[i])

            
        if 'jmp' in current:
            if i in already_checked:
                print(f'This is the problem: {index-1, i}')
                break
                
            else:
                already_checked.append(i)
        
            if '-' in amounts[i]:
                i -= int(amounts[i][1:])
            else:
                i += int(amounts[i][1:])
            index += 1

            print(instructions[i], amounts[i])
            
        
        print(already_checked)
        if index > 10:
            break
    
    print(instructions[index-1])
    if instructions[index-1] == 'jmp':
        instructions[index-1] = instructions[index-1].replace('jmp', 'nop')
    else:
        instructions[index-1] = instructions[index-1].replace('nop', 'jmp')
    print(instructions[index-1])
    return instructions, amounts





info = load(filename)
print(correct_instructions(info))