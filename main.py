from algorithm import run_tests, compare_codes
from AI.simple_strategy import SimpleStrategy
from AI.expected_size import ExpectedSize
from game import Game

run_tests()

chosen_code = [1, 4, 3, 2] # Set to False for random
colors = [1, 2, 3, 4, 5, 6]

game = Game(8, colors, chosen_code)
game.run(SimpleStrategy(colors, compare_codes))
game.run(ExpectedSize(colors, compare_codes))
