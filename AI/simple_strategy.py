from collections import defaultdict

class SimpleStrategy:
    def __init__(self, colors, compare):
        self.colors = colors
        self.guessed_places = [0, 0, 0, 0]

        self.options = []
        for colorA in range(len(self.colors)):
            for colorB in range(len(self.colors)):
                for colorC in range(len(self.colors)):
                    for colorD in range(len(self.colors)):
                        self.options.append([colorA + 1, colorB + 1, colorC + 1, colorD + 1])
        self.options_next = []

        self.compare = compare

    def get_possibilities(self, color_list):
        results = defaultdict(list)
        for color in self.options:
            result = self.compare(color, color_list)
            results[str(result)].append(color)

        max_steps = 0
        for combination in results:
            results_length = len(results[combination])
            if results_length > max_steps:
                max_steps = results_length

        return (max_steps, results)

    def set_result(self, pins):
        self.options = self.options_next[str(pins)]

    def run(self):
        possible_options = []
        lowest = 9999
        for color in self.options:
            possibilities, result_choises = self.get_possibilities(color)
            if possibilities < lowest:
                possible_options.append([possibilities, color])
                self.options_next = result_choises
                lowest = possibilities
        
        chosen = False
        for option in possible_options:
            if option[0] == lowest:
                chosen = option[1]
                break
        
        return chosen
