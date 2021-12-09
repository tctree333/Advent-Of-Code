import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = tuple(map(lambda x: tuple(map(int, x)), f.read().splitlines()))

risk = 0
for i, row in enumerate(data):
    for j, col in enumerate(row):
        top = data[i - 1][j] if i > 0 else float("inf")
        bottom = data[i + 1][j] if i < len(data) - 1 else float("inf")
        left = data[i][j - 1] if j > 0 else float("inf")
        right = data[i][j + 1] if j < len(row) - 1 else float("inf")

        if col < min(top, bottom, left, right):
            risk += 1 + col

print(risk)
