import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = tuple(map(lambda x: tuple(map(int, x)), f.read().splitlines()))


basins = []
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == 9:
            continue
        top = data[i - 1][j] if i > 0 else float("inf")
        bottom = data[i + 1][j] if i < len(data) - 1 else float("inf")
        left = data[i][j - 1] if j > 0 else float("inf")
        right = data[i][j + 1] if j < len(row) - 1 else float("inf")

        if col < min(top, bottom, left, right):
            visited = set()
            queue = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            while queue:
                x, y = queue.pop()
                if x < 0 or y < 0 or x >= len(data) or y >= len(row):
                    continue

                if data[x][y] == 9 or (x, y) in visited:
                    continue
                visited.add((x, y))

                queue.insert(0, (x - 1, y))
                queue.insert(0, (x + 1, y))
                queue.insert(0, (x, y - 1))
                queue.insert(0, (x, y + 1))

            basins.append(len(visited))


basins.sort(reverse=True)
print(basins)
print(basins[0] * basins[1] * basins[2])
