from add_random import add_random


def test_add_random():
    board = [0, 2, 0, 2,
             0, 0, 2, 4,
             0, 0, 2, 16,
             4, 4, 32, 2]

    random_added = add_random(board)

    i = 0
    differences = []
    while i < len(board):
        if board[i] != random_added[i]:
            differences.append(random_added[i])
        i += 1

    assert differences == [2]
