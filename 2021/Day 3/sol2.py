import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()


def get_ones(numbers, index):
    ones = 0
    for line in numbers:
        if line[index] == "1":
            ones += 1
    return ones


oxygen = tuple(_ for _ in data)
for i in range(len(oxygen[0])):
    ones = get_ones(oxygen, i)
    if ones >= (len(oxygen) / 2):
        oxygen = tuple(filter(lambda x: x[i] == "1", oxygen))
    else:
        oxygen = tuple(filter(lambda x: x[i] == "0", oxygen))
    if len(oxygen) == 1:
        break

co2 = tuple(_ for _ in data)
for i in range(len(co2[0])):
    ones = get_ones(co2, i)
    if ones >= (len(co2) / 2):
        co2 = tuple(filter(lambda x: x[i] == "0", co2))
    else:
        co2 = tuple(filter(lambda x: x[i] == "1", co2))
    if len(co2) == 1:
        break


print(oxygen)
print(co2)
print(int(oxygen[0], 2) * int(co2[0], 2))
