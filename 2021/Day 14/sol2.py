import os.path
import math

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

pairs = {}
for i in range(len(data[0]) + 1):
    pair = data[0][i : i + 2]
    pairs[pair] = pairs.get(pair, 0) + 1
rules = {k: v for k, v in (x.split(" -> ") for x in data[2:])}
for step in range(40):
    updated_pairs = {}
    for pair, count in pairs.items():
        if pair in rules:
            pairs[pair] -= count
            insert = rules[pair]
            updated_pairs[pair[0] + insert] = (
                updated_pairs.get(pair[0] + insert, 0) + count
            )
            updated_pairs[insert + pair[1]] = (
                updated_pairs.get(insert + pair[1], 0) + count
            )
    for pair, count in updated_pairs.items():
        pairs[pair] = pairs.get(pair, 0) + count

counts = {}
for pair, amt in pairs.items():
    for char in pair:
        counts[char] = counts.get(char, 0) + amt
counts = {k: math.floor(v / 2) for k, v in counts.items()}

sort_counts = tuple(sorted(counts.values(), reverse=True))
print(sort_counts[0] - sort_counts[-1])
