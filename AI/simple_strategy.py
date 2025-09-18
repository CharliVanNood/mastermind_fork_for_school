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
        results = {}
        for color in self.options:
            result = self.compare(color, color_list)
            if not str(result) in results: results[str(result)] = [color]
            else: results[str(result)].append(color)

        max_steps = 0
        for combination in results:
            if len(results[combination]) > max_steps:
                max_steps = len(results[combination])

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
        
        min_option = 9999
        chosen = False
        for option in possible_options:
            if option[0] < min_option:
                min_option = option[0]
                chosen = option[1]
        
        print(min_option)
        return chosen
