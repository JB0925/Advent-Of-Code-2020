import os

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


def find_accumulator_total(data):
    total = 0
    already_checked = []
    checked_twice = False
    i = 0
    index = 0
    checklist = []
    instructions, amounts = data[0], data[1]

    while index != 632:
        if instructions[i] == 'nop':
            if i in already_checked:
                checked_twice = True
            else:
                already_checked.append(i)
            i += 1
            
            

        if instructions[i] == 'acc':
            if i in already_checked:
                checked_twice = True
                break
            else:
                already_checked.append(i)
            
                if '-' in amounts[i]:
                    total -= int(amounts[i][1:])
                else:
                    total += int(amounts[i][1:])
            i += 1
        
            

        if instructions[i] == 'jmp':
            if i in already_checked:
                checked_twice = True
            else:
                already_checked.append(i)
        
            if '-' in amounts[i]:
                i -= int(amounts[i][1:])
            else:
                i += int(amounts[i][1:])

        index += 1
            
            
    print(index)
    return total

info = load(path)
amount = find_accumulator_total(info)
print(amount)




