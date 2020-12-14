filename = 'aoc-12.txt'

def load(infile):
    with open(infile) as f:
        return [(x[0], int(x[1:])) for x in f.readlines()]


def calculate_directions(data):
    direction = 'S W N E'.split()
    turns = 'R L'.split()
    directions_dict = {'NS': 0, 'EW': 0}
    degrees = {90: 1, 180: 2, 270: 3, 360: 4}
    currently_facing = 'E'
    
    for path, coordinate in data:
        if path in turns:
            if path == 'R':
                idx = (direction.index(currently_facing) + degrees.get(coordinate)) % len(direction)
                currently_facing = direction[idx]
            if path == 'L':
                idx = (direction.index(currently_facing) - degrees.get(coordinate)) % len(direction)
                currently_facing = direction[idx]
        else:
            if path == 'F':
                if currently_facing == 'N':
                    directions_dict['NS'] += coordinate
                if currently_facing == 'S':
                    directions_dict['NS'] -= coordinate
                if currently_facing == 'E':
                    directions_dict['EW'] += coordinate
                if currently_facing == 'W':
                    directions_dict['EW'] -= coordinate
    
            else:
                if path == 'N':
                    directions_dict['NS'] += coordinate
                if path == 'S':
                    directions_dict['NS'] -= coordinate
                if path == 'E':
                    directions_dict['EW'] += coordinate
                if path == 'W':
                    directions_dict['EW'] -= coordinate
    
    
    north_and_south = abs(directions_dict['NS'])
    east_and_west = abs(directions_dict['EW'])

    return north_and_south + east_and_west
        
    










directions = load(filename)
print(calculate_directions(directions))

with open('aoc-12.txt') as file:
    n = 0
    e = 0
    facing = 'E'
    directions =['N', 'E', 'S', 'W']
    for move in file:
        direction = move[0]
        coord = int(move[1:])
        if direction == 'R':
            to_move = coord // 90
            idx = (directions.index(facing) + to_move) % len(directions)
            facing = directions[idx]
        if direction == 'L':
            to_move = coord // 90
            idx = (directions.index(facing) - to_move) % len(directions)
            facing = directions[idx]
        if direction == 'F':
            direction = facing
        if direction == 'N':
            n += coord
        if direction == 'S':
            n -= coord
        if direction == 'E':
            e += coord
        if direction == 'W':
            e -= coord
    print(abs(n) + abs(e))