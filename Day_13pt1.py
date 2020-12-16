filename = 'aoc-13.txt'

def load(infile):
    with open(infile) as f:
        reader = f.readlines()
        timestamp = int(reader[0].replace('\n',''))
        buses = [int(b) for b in reader[1].split(',') if b != 'x' and b != ',' and b != '\n']
    return timestamp, buses
        

def find_closest_bus(data):
    timestamp = data[0]
    buses = data[1]
    difference = timestamp
    bus_number = 0
    total_time = 0
    times = []

    for bus in buses:
        while total_time < timestamp:
            total_time += bus
        times.append((bus, total_time))
        total_time = 0
    
    for bus, time, in times:
        difference = min(difference, time - timestamp)
        if time - timestamp == difference:
            bus_number = bus
    
    return bus_number * difference


info = load(filename)
closest_time = find_closest_bus(info)
print(closest_time)