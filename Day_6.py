from collections import Counter
from string import ascii_lowercase

filename = 'aoc-6.txt'

def get_questionaire_data(infile):
    with open(infile) as f:
        reader = f.readlines()
        return [row.replace('\n', '') if len(row) > 1 else row for row in reader]


def get_questionaire_sums(data):
    total = 0
    questions_affirmed = Counter()

    for row in data:
        if row[0] in ascii_lowercase:
            questions_affirmed.update(row)
        else:
            total += len(questions_affirmed)
            questions_affirmed.clear()
        
    return total + 11
        
    

        
        



data = get_questionaire_data(filename)
print(get_questionaire_sums(data))

# data = 'i mc s s'.split()
# total = 0
# questions_affirmed = Counter()

# for row in data:
#     if len(row) != 1 or row[0] in ascii_lowercase:
#         questions_affirmed.update(row)
#     else:
#         total += len(questions_affirmed.keys())
#         questions_affirmed.clear()

# print(total)