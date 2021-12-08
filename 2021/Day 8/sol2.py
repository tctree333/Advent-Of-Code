import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = map(
        lambda x: tuple(map(lambda x: x.split(" "), x.split(" | "))),
        f.read().splitlines(),
    )

output = []
for input_digits, output_digits in data:
    digits = {}
    mapping = {}
    for d in input_digits:
        uniq_seg = {2: 1, 4: 4, 3: 7, 7: 8}
        if len(d) in uniq_seg:
            # 1, 4, 7, 8
            digits[uniq_seg[len(d)]] = d
            if 1 in digits and 7 in digits:
                mapping["a"] = set(digits[7]).difference(digits[1]).pop()

    for d in input_digits:
        if len(d) == 6:
            # 0, 6, 9
            diff = set(digits[8]).difference(d).pop()
            if diff not in digits[4]:
                mapping["e"] = diff
                digits[9] = d
            elif diff not in digits[1]:
                mapping["d"] = diff
                digits[0] = d
            else:
                mapping["c"] = diff
                digits[6] = d

    for d in input_digits:
        if len(d) == 5:
            # 2, 3, 5
            if mapping["e"] in d and mapping["c"] in d:
                missing = set(digits[8]).difference(d)
                digits[2] = d
            elif mapping["c"] in d:
                digits[3] = d
            else:
                digits[5] = d

    number = ""
    for o in output_digits:
        for d in digits:
            if set(o) == set(digits[d]):
                number += str(d)
                break
    output.append(int(number))


print(sum(output))
