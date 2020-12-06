import re

filename = 'aoc-4.txt'
passport_info = []
keys, values = [], []


fields = 'eyr pid hcl byr iyr ecl hgt cid'.split()
fields.sort()
fields2 = fields[:]
fields2.remove('cid')
count = 0
total = 0

with open(filename) as f:
    reader = f.readlines()
    for row in reader:
        row = row.split()
        if row != []:
            for item in row:
                keys.append(item.split(':')[0])
                values.append(item.split(':')[1])
        else:
            if sorted(keys) == fields or sorted(keys) == fields2:
                passport_info.append(dict(zip(keys, values)))
                count += 1
            keys, values = [], []
                    

#print(count)

#$print(passport_info[0])

birth_year = list(range(1920, 2003))
issue_yr = list(range(2010, 2021))
exp_year = list(range(2020, 2031))
cm_height = list(range(150, 194))
in_height = list(range(59, 77))
hair_color = r'#[a-z0-9]{6}'
eyes = '|'.join('amb blu brn gry grn hzl oth'.split())
eyes = rf'({eyes})'
pass_id = r'[0-9]{9}'

for p in passport_info:
    birthday = int(p['byr']) in birth_year
    issue = int(p['iyr']) in issue_yr
    expired = int(p['eyr']) in exp_year
    hair = p['hcl'] in re.findall(hair_color, p['hcl'])
    eye_color = p['ecl'] in re.findall(eyes, p['ecl'])
    pid = p['pid'] in re.findall(pass_id, p['pid'])
    if 'in' in p['hgt']:
        hgt = p['hgt'].split('in')[0]
        height = int(hgt) in in_height
    
    elif 'cm' in p['hgt']:
        hgt = p['hgt'].split('cm')[0]
        height = int(hgt) in cm_height
    
    else:
        height = False
    
    valid_passport = [birthday, issue, expired, hair, eye_color, pid, height]
    if all(valid_passport):
        total += 1

print(total)

