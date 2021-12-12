import copy
class Board:

    def __init__(self, data):
        self.data = data
        self.row_marks = { k: set() for k in range(len(data)) }
        self.col_marks = { k: set() for k in range(len(data)) }
        self.marks = []

    def is_winning(self):
        for row, cols in self.row_marks.items():
            all_indices = list(range(len(self.data)))
            for col in cols:
                all_indices.remove(col)
            if len(all_indices) < 1:
                return row, cols

        for col, rows in self.col_marks.items():
            all_indices = list(range(len(self.data)))
            for row in rows:
                all_indices.remove(row)
            if len(all_indices) < 1:
                return col, rows

        return None

    def find(self, number):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == number:
                    return i, j
        return None

    def mark(self, number):
        result = self.find(number)
        if result:
            i, j = result
            self.row_marks[i].add(j)
            self.col_marks[j].add(i)
            self.marks.append((i, j))

    def score(self, current_number):
        total_sum = sum([sum(row) for row in self.data])
        marked_sum = 0
        for mark in self.marks:
            marked_sum += self.data[mark[0]][mark[1]]

        unmarked_sum = total_sum - marked_sum

        return unmarked_sum * current_number

    def __repr__(self):
        return repr(self.data)


def read_bingo_input(path):
    text = ""
    with open(path) as f:
        text = f.read()

    numbers, *boards = text.split("\n\n")
    numbers = [int(x) for x in numbers.split(",")]
    split_boards = []
    for board in boards:
        split_boards.append(Board([[int(el) for el in row.strip().split(" ") if el != ""] for row in board.split("\n")]))
    return numbers, split_boards

numbers, boards = read_bingo_input("day4/input.txt")

def play_bingo(numbers, boards):
    for n in numbers:
        for board in boards:
            board.mark(n)
            res = board.is_winning()
            if res is not None:
                return board.score(n)

print("Part 1: ", play_bingo(numbers, boards))

numbers, boards = read_bingo_input("day4/input.txt")

def play_bingo_2(numbers, boards):
    last_score = -1
    boards_not_won = list(range(len(boards)))
    while len(boards_not_won) > 0:
        for n in numbers:
            for i in copy.copy(boards_not_won):
                board = boards[i]
                board.mark(n)
                res = board.is_winning()
                if res is not None:
                    boards_not_won.remove(i)
                    last_score = board.score(n)
            if len(boards_not_won) < 1:
                break
    return last_score

print("Part 2: ", play_bingo_2(numbers, boards))






