import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = tuple(map(int, f.read().split(",")))

print(len(data))
totals = [0] * 1788
for x in range(1788):
    for i in data:
        totals[x] += sum(range(1, abs(i - x) + 1))

print(min(totals))
