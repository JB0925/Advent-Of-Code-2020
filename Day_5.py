filename = 'aoc-5.txt'

def get_row(item):
    rows = list(range(0, 128))
    mid = len(rows) // 2

    while len(rows) > 1:
        for x in item[0:7]:
            if x == 'F':
                rows = rows[:mid]
            else:
                rows = rows[mid:]
                
            mid = len(rows) // 2
    
    return rows[0]
                

def get_column(item):
    rows = list(range(0,8))
    mid = len(rows) // 2

    while len(rows) > 1:
        for x in item[7:]:
            if x == 'L':
                rows = rows[:mid]
            else:
                rows = rows[mid:]
                    
            mid = len(rows) // 2

    return rows[0]


def get_highest_seat_number(infile):
    seat_numbers = []

    with open(infile) as f:
        reader = f.readlines()
        for row in reader:
            row_num = get_row(row)
            col_num = get_column(row)
            seat_num = row_num * 8 + col_num
            seat_numbers.append(seat_num)

    return max(seat_numbers)


print(get_highest_seat_number(filename))

    


