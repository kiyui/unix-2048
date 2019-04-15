#!/usr/bin/env python3
import argparse
from random import randint
from lib import parse_board


def add_random(board):
    game_board = list(board).copy()

    random_added = False
    while not random_added:
        add_at = randint(0, len(game_board) - 1)

        # Replace the value if it is a 2
        if game_board[add_at] == 0:
            game_board[add_at] = 2
            random_added = True

    return game_board


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Randomly populates an empty tile
                       in a 2048 board string with a 2.""")
    parser.add_argument('--board',
                        type=str,
                        help="The 2048 game board as a CSV string")
    args = parser.parse_args()

    # If board is not provided from command line, ask from stdin
    board = args.board
    if board is None:
        board = input()

    played_board = add_random(parse_board(board))

    print(",".join(map(str, played_board)))
