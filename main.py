from algorithm import run_tests, compare_codes
from AI.simple_strategy import SimpleStrategy
from AI.expected_size import ExpectedSize
from AI.machine_learning import MachineLearning
from game import Game
import numpy as np

run_tests()

machine_learning = MachineLearning()
model = machine_learning.build_mastermind_model(colors=6, pins=4, turns=8)

X = np.random.randint(0, 7, size=(1000, 8 * (4 + 2)))
y = [np.random.randint(0, 6, size=(1000,)) for _ in range(4)]

model.fit(X, y, epochs=10, batch_size=32)

chosen_code = [1, 4, 3, 2] # Set to False for random
colors = [1, 2, 3, 4, 5, 6]

game = Game(8, colors, chosen_code)
game.run(SimpleStrategy(colors, compare_codes))
game.run(ExpectedSize(colors, compare_codes))
