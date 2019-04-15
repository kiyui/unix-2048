#!/usr/bin/env python3
import argparse
import numpy as np
from lib import parse_board


def validate_direction(direction):
    if direction in range(0, 4):
        return direction
    raise ValueError


def slide_values(value_row):
    output_row = value_row.copy()

    # Add the same values from left to right
    i = len(output_row) - 1
    while i > 0:
        if output_row[i] == output_row[i - 1]:
            output_row[i] *= 2
            output_row[i - 1] = 0
            i -= 1
        i -= 1

    # Shift all the values over 0
    i = 0
    while i < len(output_row):
        ii = 0
        while ii < len(output_row) - 1:
            if output_row[ii + 1] == 0:
                output_row[ii + 1] = output_row[ii]
                output_row[ii] = 0
            ii += 1
        i += 1

    return output_row


def play_game(direction, board):
    # Convert board into 4x4 matrix
    shaped_board = np.reshape(list(board), (4, 4))

    # We transform the board such that the direction is
    # always from left to right when passed into the
    # `slide_values` function. Since 3 (right) is already
    # oriented from left to right, it is not transformed.
    if direction == 0:
        shaped_board = np.rot90(shaped_board, axes=(1, 0))
    elif direction == 1:
        shaped_board = np.fliplr(np.rot90(shaped_board, axes=(1, 0)))
    elif direction == 2:
        shaped_board = np.fliplr(shaped_board)

    # Create a list from the transformed rows
    slide_board = list(map(slide_values, shaped_board))

    # Convert the values back
    if direction == 0:
        slide_board = np.rot90(slide_board, axes=(0, 1))
    elif direction == 1:
        slide_board = np.fliplr(np.rot90(slide_board, axes=(1, 0)))
    elif direction == 2:
        slide_board = np.fliplr(slide_board)

    # Flatten the board into a single dimension
    return list(np.reshape(slide_board, 16))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Creates an output 2048 board based on
                       the provided direction and input board.""")
    parser.add_argument('direction',
                        type=int,
                        help="0: Up, 1: Down, 2: Left, 3: Right")
    parser.add_argument('--board',
                        type=str,
                        help="The 2048 game board as a CSV string")
    args = parser.parse_args()

    # If board is not provided from command line, ask from stdin
    board = args.board
    if board is None:
        board = input()

    played_board = play_game(
        validate_direction(args.direction),
        parse_board(board))

    print(",".join(map(str, played_board)))
