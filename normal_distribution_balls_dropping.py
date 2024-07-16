import random


class Ball():
    def __init__(self):
        self.position_x = 0
        self.position_y = 0

    def possible_move(self):
        randNum = random.randint(-1, 1)
        possible_x = self.position_x
        if randNum < 0:
            possible_x = self.position_x - 1
        elif randNum > 0:
            possible_x = self.position_x + 1

        return possible_x

    def moved(self, new_x):
        self.position_y -= 1
        self.position_x = new_x


class Grid:
    def __init__(self, bottom_container_count):
        self.bottom_container_count = bottom_container_count
        self.y_levels = bottom_container_count // 2 + 1
        self.middle_x = bottom_container_count // 2
        self.grid = [[None]*bottom_container_count for _ in range(0, self.y_levels)]

    def check_valid_move(self, possible_x, possible_y):
        valid_move = True

        if possible_y > self.y_levels:
            valid_move = False
        else:
            x_values_grid = self.grid[possible_y]
            if not x_values_grid[possible_x]:
                valid_move = False

        return valid_move


grid = Grid(7)
