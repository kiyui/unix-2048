from game import slide_values, play_game


def test_slide_values():
    assert slide_values([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert slide_values([0, 0, 0, 2]) == [0, 0, 0, 2]
    assert slide_values([0, 0, 2, 0]) == [0, 0, 0, 2]
    assert slide_values([0, 0, 2, 2]) == [0, 0, 0, 4]
    assert slide_values([0, 0, 2, 4]) == [0, 0, 2, 4]
    assert slide_values([0, 2, 0, 0]) == [0, 0, 0, 2]
    assert slide_values([0, 2, 0, 2]) == [0, 0, 0, 4]
    assert slide_values([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert slide_values([0, 2, 2, 0]) == [0, 0, 0, 4]
    assert slide_values([0, 2, 2, 2]) == [0, 0, 2, 4]
    assert slide_values([0, 2, 2, 4]) == [0, 0, 4, 4]
    assert slide_values([0, 2, 4, 0]) == [0, 0, 2, 4]
    assert slide_values([0, 2, 4, 2]) == [0, 2, 4, 2]
    assert slide_values([0, 2, 4, 4]) == [0, 0, 2, 8]
    assert slide_values([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert slide_values([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert slide_values([2, 0, 0, 4]) == [0, 0, 2, 4]
    assert slide_values([2, 0, 2, 0]) == [0, 0, 0, 4]
    assert slide_values([2, 0, 2, 2]) == [0, 0, 2, 4]
    assert slide_values([2, 0, 2, 4]) == [0, 0, 4, 4]
    assert slide_values([2, 0, 4, 0]) == [0, 0, 2, 4]
    assert slide_values([2, 0, 4, 2]) == [0, 2, 4, 2]
    assert slide_values([2, 0, 4, 4]) == [0, 0, 2, 8]
    assert slide_values([2, 2, 0, 0]) == [0, 0, 0, 4]
    assert slide_values([2, 2, 0, 2]) == [0, 0, 2, 4]
    assert slide_values([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert slide_values([2, 2, 2, 0]) == [0, 0, 2, 4]
    assert slide_values([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert slide_values([2, 2, 2, 4]) == [0, 2, 4, 4]
    assert slide_values([2, 2, 4, 0]) == [0, 0, 4, 4]
    assert slide_values([2, 2, 4, 2]) == [0, 4, 4, 2]
    assert slide_values([2, 2, 4, 4]) == [0, 0, 4, 8]
    assert slide_values([2, 4, 0, 0]) == [0, 0, 2, 4]
    assert slide_values([2, 4, 0, 2]) == [0, 2, 4, 2]
    assert slide_values([2, 4, 0, 4]) == [0, 0, 2, 8]
    assert slide_values([2, 4, 2, 0]) == [0, 2, 4, 2]
    assert slide_values([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert slide_values([2, 4, 2, 4]) == [2, 4, 2, 4]
    assert slide_values([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert slide_values([2, 4, 4, 2]) == [0, 2, 8, 2]
    assert slide_values([2, 4, 4, 4]) == [0, 2, 4, 8]


def test_play_game():
    board_a = [0, 2, 0, 2,
               0, 0, 2, 4,
               0, 0, 0, 16,
               0, 4, 16, 2]

    assert play_game(0, board_a) == [0, 2, 2, 2,
                                     0, 4, 16, 4,
                                     0, 0, 0, 16,
                                     0, 0, 0, 2]

    assert play_game(1, board_a) == [0, 0, 0, 2,
                                     0, 0, 0, 4,
                                     0, 2, 2, 16,
                                     0, 4, 16, 2]

    assert play_game(2, board_a) == [4, 0, 0, 0,
                                     2, 4, 0, 0,
                                     16, 0, 0, 0,
                                     4, 16, 2, 0]

    assert play_game(3, board_a) == [0, 0, 0, 4,
                                     0, 0, 2, 4,
                                     0, 0, 0, 16,
                                     0, 4, 16, 2]

    board_b = [2, 0, 0, 2,
               4, 0, 0, 0,
               2, 4, 16, 0,
               2, 8, 16, 2]

    assert play_game(0, board_b) == [2, 4, 32, 4,
                                     4, 8, 0, 0,
                                     4, 0, 0, 0,
                                     0, 0, 0, 0]

    assert play_game(1, board_b) == [0, 0, 0, 0,
                                     2, 0, 0, 0,
                                     4, 4, 0, 0,
                                     4, 8, 32, 4]

    assert play_game(2, board_b) == [4, 0, 0, 0,
                                     4, 0, 0, 0,
                                     2, 4, 16, 0,
                                     2, 8, 16, 2]

    assert play_game(3, board_b) == [0, 0, 0, 4,
                                     0, 0, 0, 4,
                                     0, 2, 4, 16,
                                     2, 8, 16, 2]
