forest = []
tree = '#'
tree_count = 0
x, y = 0, 0

with open('aoc-3.txt') as f:
    reader = f.readlines()
    for row in reader:
        forest.append(row)

player = forest

while x < len(forest) or y < len(forest[0]):
    if player[x][y] == tree:
        tree_count += 1
    x += 2
    y += 1

    if x >= len(forest):
        break
    if y >= len(forest[0]) -1:
        y -= len(forest[0]) -1



print(tree_count)


print(159 * 86 * 97 * 88 * 55)