import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

template = data[0]
rules = {k: v for k, v in (x.split(" -> ") for x in data[2:])}

for step in range(10):
    new_template = [template[0]]
    for i in range(len(template) - 1):
        pair = template[i : i + 2]
        if pair in rules:
            new_template.append(rules[pair])
            new_template.append(pair[1])
        else:
            new_template.append(pair[1])
    template = "".join(new_template)

counts = {}
for char in template:
    counts[char] = counts.get(char, 0) + 1
sort_counts = tuple(sorted(counts.values(), reverse=True))
print(sort_counts[0] - sort_counts[-1])
