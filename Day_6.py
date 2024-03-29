from collections import Counter
from string import ascii_lowercase

filename = 'aoc-6.txt'

def get_questionaire_data(infile):
    with open(infile) as f:
        reader = f.readlines()
        return [row.replace('\n', '') if len(row) > 1 else row for row in reader]


def get_questionaire_sums(data):
    anyone_answered_yes = 0
    all_answered_yes = 0
    group_list = []
    questions_affirmed = Counter()

    for row in data:
        if row[0] in ascii_lowercase:
            group_list.append(row)
            questions_affirmed.update(row)
        else:
            for letter in questions_affirmed:
                if questions_affirmed.get(letter) == len(group_list):
                    all_answered_yes += 1

            anyone_answered_yes += len(questions_affirmed)
            questions_affirmed.clear()
            group_list.clear()
        
    return f'Part 1: {anyone_answered_yes + 11}, Part 2: {all_answered_yes}'
        

data = get_questionaire_data(filename)
print(get_questionaire_sums(data))

