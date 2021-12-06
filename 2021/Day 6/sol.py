import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    ages = list(map(int, f.read().split(",")))

for day in range(80):
    for i in range(len(ages)):
        if ages[i] == 0:
            ages[i] = 6
            ages.append(8)
        else:
            ages[i] -= 1

print(len(ages))
