#!/usr/bin/env python3
import argparse
import numpy as np
from lib import parse_board
from prettytable import PrettyTable, ALL


def show_board(board):
    shaped_board = np.reshape(list(board), (4, 4))

    # Create table
    table = PrettyTable()
    table.header = False
    table.hrules = ALL

    for row in shaped_board:
        table.add_row(row)

    # Display
    print(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display a 2048 board string")
    parser.add_argument('--board',
                        type=str,
                        help="The 2048 game board as a CSV string")
    args = parser.parse_args()

    # If board is not provided from command line, ask from stdin
    board = args.board
    if board is None:
        board = input()

    show_board(parse_board(board))
