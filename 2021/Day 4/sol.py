import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    raw = f.read().split("\n\n")
    numbers = tuple(map(int, raw[0].split(",")))
    boards = tuple(
        tuple(
            tuple(map(int, filter(lambda x: x != "", row.split(" "))))
            for row in board.split("\n")
        )
        for board in raw[1:]
    )


def check_board(board, numbers):
    for row in board:
        if all((n in numbers for n in row)):
            return True
    columns = tuple(zip(*board))
    for column in columns:
        if all((n in numbers for n in column)):
            return True
    return False


def score(board, numbers):
    nums = (num for row in board for num in row)
    return sum(filter(lambda x: x not in numbers, nums)) * numbers[-1]


def run():
    last = None
    won_boards = []
    for i in range(100):
        for j, board in enumerate(boards):
            if j in won_boards:
                continue
            if check_board(board, numbers[:i]):
                last = (i, j)
                won_boards.append(j)
    return score(boards[last[1]], numbers[: last[0]])


print(run())
