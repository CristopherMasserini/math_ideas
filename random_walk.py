import random
import numpy as np
import matplotlib.pyplot as plt


random_lookup_table = {'uniform': lambda: random.uniform(-1, 1),
                       'triangular': lambda: random.triangular(-1, 1),
                       'gauss': lambda: random.gauss(0, 1),
                       'expovariate': lambda: random.expovariate(1) + random.expovariate(-1),
                       'lognormvariate': lambda: random.lognormvariate(0, 1),
                       'normalvariate': lambda: random.normalvariate(0, 1)
                       }


def addition_vector(variable_x=True, random_type='uniform'):
    if variable_x:
        x = random_lookup_table[random_type]()
    else:
        x = 1

    y = random_lookup_table[random_type]()
    vec = np.array([[x], [y]])
    return vec


def movement(walk, perturbation):
    return walk + perturbation


def graph(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()


def run(iters, starting_point, variable_x=True, random_type='uniform'):
    all_x = [starting_point[0][0]]
    all_y = [starting_point[1][0]]
    current_point = starting_point
    for i in range(0, iters):
        perturbation = addition_vector(variable_x, random_type)
        current_point = movement(current_point, perturbation)
        all_x.append(current_point[0][0])
        all_y.append(current_point[1][0])

    graph(all_x, all_y)


if __name__ == '__main__':
    '''
    Ideas: 
    - Can we come up with some general shapes of a random walk that correspond to different market trends?
    - Since randomness on computers isn't true randomness, can we get a model to predict the trend or next move?
    '''
    origin_point = np.array([[0], [1]])
    run(100, origin_point, False, 'gauss')

