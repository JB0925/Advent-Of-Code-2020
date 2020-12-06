import os
from collections import Counter
filename = os.path.join('C:/Users/superuser/Desktop', 'aoc-2.txt')


num_passwords = 0
passwords = []
good_password = False

with open(filename) as f:
    reader = f.readlines()
    for row in reader:
        count = Counter()
        row = row.split()
        num1 = int(row[0].split('-')[0])
        num2 = int(row[0].split('-')[1])
        total = list(range(num1, num2 + 1))
        letter = row[1].replace(':', '')
        count.update(row[2])

        if count.get(letter) in total:
            num_passwords += 1

print(num_passwords)


with open(filename) as f:
    reader = f.readlines()
    for row in reader:
        row = row.split()
        num1 = int(row[0].split('-')[0])
        num2 = int(row[0].split('-')[1])
        letter = row[1].replace(':', '')
        password = row[2]
        if password[num1-1] == letter and password[num2-1] != letter:
            passwords.append(password)
        if password[num1-1] != letter and password[num2-1] == letter:
            passwords.append(password)
print(len(passwords))




    