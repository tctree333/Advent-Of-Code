import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

windows = [
    int(x) + int(data[i + 1]) + int(data[i + 2])
    for i, x in enumerate(data)
    if i < len(data) - 2
]

prev = None
count = 0
for depth in windows:
    if prev is not None and int(depth) > prev:
        count += 1
    prev = int(depth)

print(count)
