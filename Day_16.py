import re

filename = 'aoc-16.txt'

def load(infile):
    information = {}
    all_info = []
    all_other_tickets = {}

    with open(infile) as f:
        reader = f.readlines()
        my_ticket = [int(n) for n in reader[22].replace('\n','').split(',')]
        for row in reader[0:20]:
            category, data = row.replace('\n','').split(':')
            data = re.findall('[\d]+', data)
            i,j,k,l = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            information[category] = list(range(i, j+1))
            information.get(category).extend(list(range(k, l+1)))
            all_info.extend(list(range(i, j+1)))
            all_info.extend(list(range(k, l+1)))

        for idx, row in enumerate(reader[25:]):
            temp = [int(n) for n in row.replace('\n','').split(',')]
            all_other_tickets[idx] = temp
    
    return information, all_other_tickets, my_ticket, set(all_info)


def find_invalid_tickets(data):
    invalid_tickets = set()
    loose_tickets = data[1]
    all_info = data[3]
    total = 0
    
    for ticket in loose_tickets:
        values = loose_tickets.get(ticket)
        not_in_common = set(values) - all_info
        
        if len(not_in_common) >= 1:
            total += sum(list(not_in_common))
            invalid_tickets.add(ticket)
        
    loose_tickets = {k:v for k, v in loose_tickets.items() if k not in invalid_tickets}
    return loose_tickets, total


info = load(filename)
print(find_invalid_tickets(info))


