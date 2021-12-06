import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = list(map(int, f.read().split(",")))

ages = {i: 0 for i in range(0, 9)}
for age in data:
    ages[age] += 1

for day in range(256):
    ages = {k - 1: v for k, v in ages.items()}
    ages[8] = ages[-1]
    ages[6] += ages.pop(-1)


print(sum(ages.values()))
