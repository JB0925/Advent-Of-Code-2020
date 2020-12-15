filename = 'aoc-12.txt'

def load(infile):
    with open(infile) as f:
        return [(x[0], int(x[1:])) for x in f.readlines()]


def calculate_directions(data):
    direction = 'S W N E'.split()
    turns = 'R L'.split()
    ship_dict = {'NS': 0, 'EW': 0}
    degrees = {90: 1, 180: 2, 270: 3, 360: 4}
    waypoint = 'E N'.split()
    waypoint_dict = {'N': 1, 'S': 0, 'E': 10, 'W': 0}
    
    for path, coordinate in data:
        if path in turns:
            if path == 'R':
                val1 = waypoint_dict[waypoint[0]]
                val2 = waypoint_dict[waypoint[1]]
                waypoint_dict = waypoint_dict.fromkeys(waypoint_dict, 0)
                idx = (direction.index(waypoint[0]) + degrees.get(coordinate)) % len(direction)
                idx2 = (direction.index(waypoint[1]) + degrees.get(coordinate)) % len(direction)
                waypoint[0] = direction[idx]
                waypoint[1] = direction[idx2]
                waypoint_dict[waypoint[0]] = val1
                waypoint_dict[waypoint[1]] = val2
                
            if path == 'L':
                val1 = waypoint_dict[waypoint[0]]
                val2 = waypoint_dict[waypoint[1]]
                waypoint_dict = waypoint_dict.fromkeys(waypoint_dict, 0)
                idx = (direction.index(waypoint[0]) - degrees.get(coordinate)) % len(direction)
                idx2 = (direction.index(waypoint[1]) - degrees.get(coordinate)) % len(direction)
                waypoint[0] = direction[idx]
                waypoint[1] = direction[idx2]
                waypoint_dict[waypoint[0]] = val1
                waypoint_dict[waypoint[1]] = val2

        else:
            if path == 'F':
                name = ''.join(waypoint)
                if name == 'EN' or name == 'NE':
                    ship_dict['NS'] += (coordinate * waypoint_dict['N'])
                    ship_dict['EW'] += (coordinate * waypoint_dict['E'])
                if name == 'ES' or name == 'SE':
                    ship_dict['NS'] -= (coordinate * waypoint_dict['S'])
                    ship_dict['EW'] += (coordinate * waypoint_dict['E'])
                if name == 'SW' or name == 'WS':
                    ship_dict['NS'] -= (coordinate * waypoint_dict['S'])
                    ship_dict['EW'] -= (coordinate * waypoint_dict['W'])
                if name == 'WN' or name == 'NW':
                    ship_dict['NS'] += (coordinate * waypoint_dict['N'])
                    ship_dict['EW'] -= (coordinate * waypoint_dict['W'])
                
            else:
                if path == 'N':
                    waypoint_dict['N'] += coordinate
                    waypoint_dict['S'] -= coordinate
                if path == 'S':
                    waypoint_dict['S'] += coordinate
                    waypoint_dict['N'] -= coordinate
                if path == 'E':
                    waypoint_dict['E'] += coordinate
                    waypoint_dict['W'] -= coordinate
                if path == 'W':
                    waypoint_dict['W'] += coordinate
                    waypoint_dict['E'] -= coordinate
    
    
    north_and_south = abs(ship_dict['NS'])
    east_and_west = abs(ship_dict['EW'])
    
    return north_and_south + east_and_west
        

directions = load(filename)
print(calculate_directions(directions))