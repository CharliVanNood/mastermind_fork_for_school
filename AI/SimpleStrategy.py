class SimpleStrategy:
    def __init__(self, colors, compare):
        self.possible_colors = colors
        self.guessed_places = [0, 0, 0, 0]

        self.compare = compare

        print(self.get_possibilities([1, 1, 1, 1]))

    def get_possibilities(self, color_list):
        result = 0
        amount_of_colors_untried = 0

        for color in color_list:
            pass

        return result

    def run(self):
        possible_options = []
        for colorA in range(len(self.possible_colors)):
            for colorB in range(len(self.possible_colors)):
                for colorC in range(len(self.possible_colors)):
                    for colorD in range(len(self.possible_colors)):
                        color_list = [colorA + 1, colorB + 1, colorC + 1, colorD + 1]
                        possible_options.append([self.get_possibilities(color_list), color_list])
        print(possible_options)
        