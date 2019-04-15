#!/usr/bin/env python3
def parse_board(board_string):
    board = board_string.split(',')
    if len(board) == 16:
        return map(lambda value: int(value), board)
    raise ValueError
