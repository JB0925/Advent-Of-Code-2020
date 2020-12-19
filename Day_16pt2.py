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
    return loose_tickets


def figure_out_fields(data, tickets):
    category_values = data[0]
    corrected_categories = {}
    final_categories = [None for i in range(20)]
    my_ticket = data[2]
    j = 0
    k = 0
    ticket_data = []

    while j != 20:
        temp = []
        for ticket in tickets:
            value = tickets.get(ticket)
            temp.append(value[j])
        temp.append(my_ticket[j])
        
        ticket_data.append(temp)
        j += 1


    for idx, ticket in enumerate(ticket_data):
        temp = []
        for category in category_values:
            c = category_values.get(category)
            t = ticket
            in_common = set(t) < set(c)
        
            if in_common:
                temp.append(category)
                 
                if category not in corrected_categories:
                    corrected_categories[category] = [idx]
                else:
                   corrected_categories[category].append(idx)

        
    while None in final_categories:
        for category in corrected_categories:
            if len(corrected_categories[category]) == k:
               
                for item in corrected_categories[category]:
                    if final_categories[item] is None:
                        if category not in final_categories:
                            final_categories[item] = category
        k += 1
        
    
    return final_categories


def calculate_my_ticket_values(data, categories):
    my_ticket = data[2]
    total = 1

    for i in range(len(my_ticket)):
        if 'departure' in categories[i]:
            total *= my_ticket[i]
    
    return total
    

info = load(filename)
valid_tickets = find_invalid_tickets(info)
sorted_data = figure_out_fields(info, valid_tickets)
my_ticket = calculate_my_ticket_values(info, sorted_data)
print(my_ticket)

