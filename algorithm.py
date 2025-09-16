#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
Opdracht: Mastermind
(c) 2024 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)
"""


def compare_codes(code, guess):
    """ 
    Compare a code with a guessed code and provide feedback.

    Returns: a tuple containing:
        0. The amount of pegs that are correct (both color and position)
        1. The amount of pegs with correct color, but incorrect position
    """
    pass


"""
----------------------------------------------[ HU TESTRAAMWERK ]----------------------------------------------------
"""


def test_compare():
    test_cases = [
        #      code         guess        feedback
        (((1, 1, 1, 1), (2, 2, 2, 2)), (0, 0)),
        (((1, 1, 1, 1), (1, 2, 2, 2)), (1, 0)),
        (((1, 1, 1, 1), (2, 2, 2, 1)), (1, 0)),
        (((3, 4, 4, 1), (1, 2, 2, 1)), (1, 0)),
        (((1, 1, 2, 2), (1, 1, 1, 2)), (3, 0)),
        (((1, 1, 1, 1), (1, 1, 1, 1)), (4, 0)),
        (((1, 1, 2, 2), (2, 2, 3, 3)), (0, 2)),
        (((1, 1, 2, 2), (3, 1, 1, 3)), (1, 1)),
    ]

    for test_params, test_result in test_cases:
        result = compare_codes(*test_params)
        assert result == test_result, (
            f"Fout: jouw functie compare{test_params} geeft {result} in plaats van {test_result}.\n"
        )


if __name__ == '__main__':
    try:
        print("\x1b[0;32m", end='')

        test_compare()
        print("Je functie compare() doorstaat de tests!")

        print("\x1b[0;0m", end='')
        print("Goed werk!")
    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))
    finally:
        print("\x1b[0;0m", end='')
