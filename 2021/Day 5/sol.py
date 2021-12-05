import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

grid = {}
for line in data:
    coord1, coord2 = line.split(" -> ")
    x1, y1 = map(int, coord1.split(","))
    x2, y2 = map(int, coord2.split(","))
    if x1 == x2:
        minY = min(y1, y2)
        for i in range(abs(y1 - y2) + 1):
            grid.setdefault((x1, minY + i), 0)
            grid[(x1, minY + i)] += 1
    elif y1 == y2:
        minX = min(x1, x2)
        for i in range(abs(x1 - x2) + 1):
            grid.setdefault((minX + i, y1), 0)
            grid[(minX + i, y1)] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        slope = int(abs((y1 - y2) / (x1 - x2)) / ((y1 - y2) / (x1 - x2)))
        minX = min(x1, x2)
        minY = min(y1, y2)
        maxY = max(y1, y2)
        for i in range(abs(x1 - x2) + 1):
            if slope == 1:
                grid.setdefault((minX + i, minY + i), 0)
                grid[(minX + i, minY + i)] += 1
            elif slope == -1:
                grid.setdefault((minX + i, maxY - i), 0)
                grid[(minX + i, maxY - i)] += 1

print(len(tuple(filter(lambda x: x > 1, grid.values()))))
