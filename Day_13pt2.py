filename = 'aoc-13.txt'

def load(infile):
    with open(infile) as f:
        reader = f.readlines()
        #timestamp = int(reader[0].replace('\n',''))
        buses = [int(b) if b != '\n' and b.isnumeric() else str(b) for b in reader[1].replace('\n','').split(',')]
    return buses


def get_timestamp(buses):
    timestamp = 894_954_360_381_000
    turn = 1
    timestamp_list = []

    while True:
        for i in range(len(buses)):
            if buses[i] !='x':
                if (timestamp + i) % buses[i] == 0:
                    timestamp_list.append(timestamp)
                else:
                    timestamp_list.clear()
                    continue
                
        if len(timestamp_list) == len([b for b in buses if b != 'x']):
            return timestamp_list[0]
        else:
            timestamp_list.clear()

        timestamp += 1
        

info = load(filename)
print(get_timestamp(info))

