from collections import defaultdict

def last_number_spoken():
    numbers = defaultdict(list)
    numbers[0].append(1)
    numbers[6].append(2)
    numbers[1].append(3)
    numbers[7].append(4)
    numbers[2].append(5)
    numbers[19].append(6)
    numbers[20].append(7)
    current_number = 0

    for i in range(8,30_000_000):
        numbers[current_number].append(i)

        if current_number in numbers:
            if len(numbers.get(current_number)) == 1:
                current_number = i - numbers.get(current_number)[0]
            else:
                turn = numbers.get(current_number)
                turn.sort()
                current_number = turn[-1] - turn[-2]
        else:
            current_number = 0
    
    return current_number


print(last_number_spoken())


def faster_last_number_spoken():
    numbers = {0:1, 6:2, 1:3, 7:4, 2:5, 19:6, 20:7}
    current_number = 0
    previous_number = None
    

    for i in range(8,30_000_000):
        previous_number = numbers.get(current_number, None)
        numbers[current_number] = i
        
        if current_number in numbers and previous_number is not None:
            current_number = i - previous_number
        else:
            current_number = 0
    
        
    return current_number


print(faster_last_number_spoken())
