from collections import defaultdict

filename = 'aoc-4.txt'
passport_info = []
keys, values = [], []


fields = 'eyr pid hcl byr iyr ecl hgt cid'.split()
fields.sort()
fields2 = fields[:]
fields2.remove('cid')
count = 0

with open(filename) as f:
    reader = f.readlines()
    for row in reader:
        row = row.split()
        print(row)
        if row != []:
            for item in row:
                keys.append(item.split(':')[0])
                values.append(item[1])
        else:
            if sorted(keys) == fields or sorted(keys) == fields2:
                print(sorted(keys))
                passport_info.append(dict(zip(keys, values)))
                count += 1
            keys, values = [], []
                    

print(count)