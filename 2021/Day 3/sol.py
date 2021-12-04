import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

bits = [0] * len(data[0])
for line in data:
    for i, char in enumerate(line):
        if char == "1":
            bits[i] += 1

gamma = ""
epsilon = ""
for num in bits:
    if num > len(data) / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
