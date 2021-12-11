import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = list(map(lambda x: list(map(int, x)), f.read().splitlines()))

steps = 0
while True:
    steps += 1
    data = list(map(lambda x: list(map(lambda y: y + 1, x)), data))
    updated = True
    while updated:
        updated = False
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                if item > 9:
                    updated = True
                    data[i][j] = float("-inf")
                    if i - 1 >= 0:
                        data[i - 1][j] += 1
                    if i + 1 < len(data):
                        data[i + 1][j] += 1
                    if j - 1 >= 0:
                        data[i][j - 1] += 1
                    if j + 1 < len(row):
                        data[i][j + 1] += 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        data[i - 1][j - 1] += 1
                    if i - 1 >= 0 and j + 1 < len(row):
                        data[i - 1][j + 1] += 1
                    if i + 1 < len(data) and j - 1 >= 0:
                        data[i + 1][j - 1] += 1
                    if i + 1 < len(data) and j + 1 < len(row):
                        data[i + 1][j + 1] += 1

    flashes = 0
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item > 9 or item == float("-inf"):
                flashes += 1
                data[i][j] = 0
    print(flashes)
    if flashes == 100:
        break

print(steps)
