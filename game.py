from algorithm import compare_codes
import time
import random

class Game:
    def __init__(self, amount_of_turns=8, colors=[1, 2, 3, 4, 5, 6], chosen_code=False):
        self.turns = amount_of_turns

        if chosen_code:
            self.chosen_code = chosen_code
        else:
            self.chosen_code = [random.choice(colors) for _ in range(4)]
        print("chosen code", self.chosen_code)

    def run(self, algorithm=False):
        if algorithm:
            print(f"running game with {algorithm.name}")

        start_time = time.time()

        for i in range(self.turns):
            if algorithm:
                chosen = algorithm.run()
                similarity = compare_codes(chosen, self.chosen_code)
                print(chosen, "->", similarity)
                if chosen == self.chosen_code: break
                algorithm.set_result(similarity)

        print(f"Finished SimpleStrategy in {time.time() - start_time} seconds")
