#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
Opdracht: Mastermind
(c) 2024 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)
"""


def compare_codes(code, guess):
    codeTried, guessTried, result = [pin for pin in code], [pin for pin in guess], [0, 0]
    for i in range(len(code)):
        if guessTried[i] == codeTried[i]:
            result[0] += 1
            codeTried[i], guessTried[i] = -1, -2
    result[1] = len([True for pin in guessTried if pin in codeTried])
    return tuple(result)


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
        (((3, 3, 4, 4), (4, 5, 3, 6)), (0, 2)),
    ]

    for test_params, test_result in test_cases:
        result = compare_codes(*test_params)
        assert result == test_result, (
            f"Fout: jouw functie compare{test_params} geeft {result} in plaats van {test_result}.\n"
        )


def run_tests():
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
