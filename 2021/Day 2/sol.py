import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0
for line in data:
    direction, distance = line.split(" ")
    if direction == "forward":
        horizontal += int(distance)
        depth += aim * int(distance)
    elif direction == "up":
        aim -= int(distance)
    elif direction == "down":
        aim += int(distance)

print(horizontal * depth)
