import numpy as np
import matplotlib.pyplot as plt
import random


def run_computations(num, x, b, iters=25000):
    # Transforms: f1 = Ax, f2 = Ax + b
    # pick random point to start (x), apply transforms. Plot the new points.
    # Pick random of the new points to use as new x and repeat.

    points_x1x = []
    points_x1y = []
    points_x2x = []
    points_x2y = []
    picked = []

    A = np.array([[num, -num], [num, num]])

    for _ in range(0, iters):
        y1 = np.matmul(A, x)
        y2 = np.matmul(A, x) + b

        points_x1x.append(y1[0][0])
        points_x1y.append(y1[1][0])
        points_x2x.append(y2[0][0])
        points_x2y.append(y2[1][0])

        rand_num = random.randint(0, 1)

        if rand_num == 0:
            x = y1
            picked.append(0)
        else:
            x = y2
            picked.append(1)

    return points_x1x, points_x1y, points_x2x, points_x2y, picked


def run_graph(points):
    points_x1x, points_x1y, points_x2x, points_x2y, picked = points
    plt.scatter(points_x1x, points_x1y, color='red', s=0.5)
    plt.scatter(points_x2x, points_x2y, color='blue', s=0.5)
    plt.show()


def check_nums(lst: list):
    for entry in lst:
        if entry is not float:
            return False

    return True


def inputs():
    valid = False
    num = 0.0
    b_list = []
    x_list = []

    while not valid:
        num = float(input('Please enter a decimal less than one. This is to build matrix: '))
        b_raw = input('Please enter two comma separated numbers. This is transformation additon vector: ')
        x_raw = input('Please enter two comma separated numbers. This is starting vector: ')

        b_list = b_raw.split(',')
        x_list = x_raw.split(',')

        if check_nums(b_list) and check_nums(x_list):
            valid = True
        else:
            print('Not valid entries, try again')

    b_array = np.array([[b_list[0]], [b_list[1]]])
    x_array = np.array([[x_list[0]], [x_list[1]]])
    a_matrix = np.array([[num, -num], [num, num]])

    return b_array, x_array, a_matrix


if __name__ == '__main__':
    # matrix_num = 0.5
    # b_vec = np.array([[1], [0]])
    # x_init = np.array([[1], [1]])
    # computed_points = run_computations(matrix_num, x_init, b_vec)
    # run_graph(computed_points)
    inputs()


