import random

class Ball():
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.atBottom = False

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
        self.grid = []
        self.fill_grid()

    def fill_grid(self):
        initial_row = [False]*self.bottom_container_count
        initial_row[self.middle_x] = 0
        self.grid.append(initial_row)

        distance_from_middle = 1
        for i in range(1, self.y_levels):
            next_row = initial_row.copy()
            next_row[self.middle_x + distance_from_middle] = 0
            next_row[self.middle_x - distance_from_middle] = 0
            self.grid.append(next_row)
            initial_row = next_row
            distance_from_middle += 1

    def check_valid_move(self, possible_x, possible_y):
        valid_move = True

        if possible_y > self.y_levels:
            valid_move = False
        else:
            x_values_grid = self.grid[possible_y]
            if x_values_grid[possible_x] is False:
                valid_move = False

        return valid_move

    def start_ball(self):
        self.grid[0][self.middle_x] += 1

    def move_levels(self, old_x, old_y, new_x, new_y):
        self.grid[old_y][old_x] -= 1
        self.grid[new_y][new_x] += 1

    def get_base_level(self):
        return self.grid[self.y_levels]


gridObj = Grid(7)
print(gridObj.grid)


