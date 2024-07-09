import numpy as np
import random

num = 0.5
A = np.array([[num, -num], [num, num]])
b = np.array([[1], [0]])

x = np.array([[1], [1]])

# Transforms: f1 = Ax, f2 = Ax + b
# pick random point to start (x), apply transforms. Plot the new points.
# Pick random of the new points to use as new x and repeat.

y1 = np.matmul(A, x)
y2 = np.matmul(A, x) + b

# random.randint(0, 1)
print(y1)
print(y2)
