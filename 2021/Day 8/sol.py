import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

output_digits = tuple(map(lambda x: x.split(" | ")[1].split(" "), data))

count = 0
for seq in output_digits:
    for d in seq:
        if len(d) in (2, 4, 3, 7):
            count += 1

print(count)
