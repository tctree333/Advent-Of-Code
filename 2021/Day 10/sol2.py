import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

score_table = {")": 1, "]": 2, "}": 3, ">": 4}
opening = {"}": "{", "]": "[", ")": "(", ">": "<"}
closing = {"{": "}", "[": "]", "(": ")", "<": ">"}

corrupted = []
for i, seq in enumerate(data):
    current = []
    for char in seq:
        if char in opening.values():
            current.append(char)
        else:
            if opening[char] != current.pop():
                corrupted.append(i)
                break
data = [seq for i, seq in enumerate(data) if i not in corrupted]

scores = []
for seq in data:
    current = []
    for char in seq:
        if char in opening.values():
            current.append(char)
        else:
            current.pop()
    score = 0
    for char in (closing[char] for char in reversed(current)):
        score *= 5
        score += score_table[char]
    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
