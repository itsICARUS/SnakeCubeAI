from Sim import *
import numpy as np
import matplotlib.pyplot as plt
from Test0101 import main


def display(coordinates):
    coordinates = np.asarray(coordinates)
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    z = coordinates[:, 2]
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'gray')
    ax.scatter(x, y, z, c=z)
    plt.show()


coordinates = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 2], [0, 1, 1], [0, 1, 0], [0, 2, 0], [0, 2, 1], [0, 2, 2],
               [1, 2, 2], [1, 2, 1], [1, 2, 0], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 0, 2], [1, 0, 1], [1, 0, 0],
               [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 2], [2, 1, 1], [2, 1, 0], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

game = Simulator(coordinates, [])
# print(game.check_coordinates())
game.open_cube()
print(game.coordinates.tolist())
display(game.coordinates)
main(game.coordinates)
