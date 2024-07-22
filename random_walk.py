import random
import numpy as np
import matplotlib.pyplot as plt


def addition_vector():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    vec = np.array([[x], [y]])
    return vec


def movement(walk, perturbation):
    return walk + perturbation


def graph(x_values, y_values):
    plt.scatter(x_values, y_values)
    plt.show()


def run(iters, starting_point):
    all_x = [starting_point[0][0]]
    all_y = [starting_point[1][0]]
    current_point = starting_point
    for i in range(0, iters):
        perturbation = addition_vector()
        current_point = movement(current_point, perturbation)
        all_x.append(current_point[0][0])
        all_y.append(current_point[1][0])

    graph(all_x, all_y)


if __name__ == '__main__':
    origin_point = np.array([[0], [1]])
    general_direction = np.array([[0.5], [0.5]])
    run(100, origin_point)

