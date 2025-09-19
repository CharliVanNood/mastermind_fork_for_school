from algorithm import run_tests, compare_codes
from AI.simple_strategy import SimpleStrategy
import time

run_tests()

chosen_code = [1, 2, 3, 4]
colors = [1, 2, 3, 4, 5, 6]

start_time = time.time()
simple_strategy = SimpleStrategy([1, 2, 3, 4, 5, 6], compare_codes)
chosen = simple_strategy.run()
print(chosen)
similarity = compare_codes(chosen, chosen_code)
simple_strategy.set_result(similarity)
chosen = simple_strategy.run()
print(chosen)
similarity = compare_codes(chosen, chosen_code)
simple_strategy.set_result(similarity)
chosen = simple_strategy.run()
print(chosen)
similarity = compare_codes(chosen, chosen_code)
simple_strategy.set_result(similarity)
chosen = simple_strategy.run()
print(chosen)
print(f"Finished SimpleStrategy in {time.time() - start_time} seconds")
