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
    for i in range(len(code)):
        if guessTried[i] in codeTried:
            result[1] += 1
            codeTried[codeTried.index(guessTried[i])], guessTried[i] = -1, -2
    return tuple(result)

"""
----------------------------------------------[ HU TESTRAAMWERK ]----------------------------------------------------
"""

def create_codes(base, length):
    codes = []
    def recursion(base, length, recur):
        for i in range(base):   
            tempinput = recur.copy()
            tempinput.append(i+1)
            if length > 1:
                recursion(base,length-1,tempinput)
            else:
                codes.append(tempinput)
    recursion(base,length,[])
    return codes

def test_compare_codes():
    test_cases = [
        ((1,1,1,1),(625,0,0,0,0,500,0,0,0,0,150,0,0,0,0,20,0,0,0,0,1,0,0,0,0)),
        ((1,1,1,2),(256,308,61,0,0,317,156,27,0,0,123,24,3,0,0,20,0,0,0,0,1,0,0,0,0)),
        ((1,1,2,2),(256,256,96,16,1,256,208,36,0,0,114,32,4,0,0,20,0,0,0,0,1,0,0,0,0)),
        ((1,1,2,3),(81,276,222,44,2,182,230,84,4,0,105,40,5,0,0,20,0,0,0,0,1,0,0,0,0)),
        ((1,2,3,4),(16,152,312,136,9,108,252,132,8,0,96,48,6,0,0,20,0,0,0,0,1,0,0,0,0)),
    ]
    codes = create_codes(6, 4)
    for comparecode, test_result in test_cases:
        resulttally = [0 for _ in range(25)] 
        for code in codes:
            result = compare_codes(code, comparecode)
            resulttally[result[0]*(len(code)+1)+result[1]] += 1
            # if result == (0,4) and comparecode == (1,1,1,2):
            #     print(f"STOPOPOP: {code}, {result}")
        assert tuple(resulttally) == test_result, (
            f"Fout: jouw functie compare met code {comparecode} geeft \n{resulttally} als resultaten in plaats van \n{test_result}.\n"
        )


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
        (((4, 2, 3, 4), (1, 1, 2, 3)), (0, 2)),
        (((1, 1, 1, 2), (3, 3, 2, 1)), (0, 2)),
        (((1, 1, 1, 2), (6, 6, 2, 1)), (0, 2)),
        (((6, 6, 2, 1), (1, 1, 1, 2)), (0, 2))
    ]

    for test_params, test_result in test_cases:
        result = tuple(compare_codes(*test_params))
        assert result == test_result, (
            f"Fout: jouw functie compare{test_params} geeft {result} in plaats van {test_result}.\n"
        )


def run_tests():
    try:
        print("\x1b[0;32m", end='')

        test_compare()
        # test_compare_codes()
        print("Je functie compare() doorstaat de tests!")

        print("\x1b[0;0m", end='')
        print("Goed werk!")
    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))
    finally:
        print("\x1b[0;0m", end='')
