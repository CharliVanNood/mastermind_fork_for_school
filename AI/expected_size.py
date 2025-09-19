from collections import defaultdict

class ExpectedSize:
    def __init__(self, colors, compare):
        self.name = "ExpectedSize"
        self.colors = colors

        self.options = []
        for colorA in range(len(self.colors)):
            for colorB in range(len(self.colors)):
                for colorC in range(len(self.colors)):
                    for colorD in range(len(self.colors)):
                        self.options.append([colorA + 1, colorB + 1, colorC + 1, colorD + 1])
        self.options_next = []

        self.compare = compare

    def get_expected_size(self, guess):
        results = defaultdict(list)

        for option in self.options:
            feedback = self.compare(option, guess)
            results[str(feedback)].append(option)

        total_combinations = len(self.options)
        expected_size = 0

        for partition in results.values():
            part_size = len(partition)
            expected_size += part_size ** 2 / total_combinations

        return expected_size, results

    def set_result(self, pins):
        self.options = self.options_next[str(pins)]

    def run(self):
        best_guess = None
        best_expected = 999999

        for guess in self.options:
            expected_size, result_choices = self.get_expected_size(guess)

            if expected_size < best_expected:
                best_expected = expected_size
                best_guess = guess
                self.options_next = result_choices

        return best_guess
