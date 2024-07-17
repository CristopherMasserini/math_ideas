import random


class Ball:
    def __init__(self):
        self.position_x = None
        self.position_y = None
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


class BallSystem:
    def __init__(self, bottom_container_count, balls_count):
        self.gridObj = Grid(bottom_container_count)
        self.balls = [Ball() for _ in range(0, balls_count)]



    def initiate_balls(self):
        for ball in self.balls:
            self.gridObj.start_ball()
            ball.position_y = 0
            ball.position_x = self.gridObj.middle_x

    def check_ball_at_bottom(self, ball, grid):
        ballAtBottom = False
        if ball.atBottom:
            ballAtBottom = True
        elif ball.position_y == grid.y_levels:
            ball.atBottom = True
            ballAtBottom = True

        return ballAtBottom

    def run_ball(self, ball):
        while not ball.atBottom:
            can_move = False
            new_x = None
            new_y = None
            while not can_move:
                new_x = ball.possible_move()
                new_y = ball.position_y - 1
                can_move = self.gridObj.check_valid_move(new_x, new_y)

            self.gridObj.move_levels(ball.position_x, ball.position_y, new_x, new_y)
            ball.moved(new_x)
            ball.atBottom = self.check_ball_at_bottom(ball, self.gridObj)

    def run_all_balls(self):
        self.initiate_balls()
        for ball in self.balls:
            self.run_ball(ball)

        return self.gridObj.get_base_level()


system = BallSystem(5, 10)
baseLevel = system.run_all_balls()
print(baseLevel)
