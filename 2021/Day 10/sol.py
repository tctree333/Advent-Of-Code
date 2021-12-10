import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

score = 0
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
for seq in data:
    closing = {"}": "{", "]": "[", ")": "(", ">": "<"}
    current = []
    for char in seq:
        if char in closing.values():
            current.append(char)
        else:
            if closing[char] != current.pop():
                score += scores[char]
                break

print(score)
