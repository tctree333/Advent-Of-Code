import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

coords = set(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), data[:999]))

folds = tuple(
    (
        (d.split(" ")[2].split("=")[0], int(d.split(" ")[2].split("=")[1]))
        for d in data[1000:]
    )
)
grid = [
    [" " for _ in range(max(coords, key=lambda x: x[0])[0] + 1)]
    for _ in range(max(coords, key=lambda x: x[1])[1] + 1)
]

for x, y in coords:
    grid[y][x] = "#"

for axis, value in folds:
    remove = set()
    add = set()
    for point in coords:
        x, y = point
        if axis == "x":
            if x > value:
                grid[y][x] = " "
                grid[y][(2 * value) - x] = "#"
                add.add(((2 * value) - x, y))
                remove.add(point)
        if axis == "y":
            if y > value:
                grid[y][x] = " "
                grid[(2 * value) - y][x] = "#"
                add.add((x, (2 * value) - y))
                remove.add(point)
    coords.difference_update(remove)
    coords.update(add)

print("\n".join(["".join(row).strip() for row in grid]).strip())
