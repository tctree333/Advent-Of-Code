import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

coords = tuple(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), data[:999]))

folds = tuple(
    (
        (d.split(" ")[2].split("=")[0], int(d.split(" ")[2].split("=")[1]))
        for d in data[1000:]
    )
)

count = len(coords)
for point in coords:
    x, y = point
    if x > folds[0][1]:
        new_point = (2 * (folds[0][1]) - x, y)
        if new_point in coords:
            count -= 1

print(count)
