import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as Rotate, Rotation
from Sim import *


# def cube_rotate(self, cube_number, action_degree, axis):
#     self.coordinates = np.array(self.coordinates).astype(int)
#     to_minus = coordinates[cube_number]
#     self.coordinates = self.coordinates - to_minus
#     for i in range(cube_number, 27):
#         r = Rotate.from_euler(axis, action_degree, degrees=True)
#         rr = r.as_matrix().T.astype(int)
#         game.coordinates[i] = game.coordinates[i] @ rr
#
#     np.array(self.coordinates).astype(int)
#     self.coordinates = self.coordinates + to_minus


class Simuslator:

    def __init__(self, coordinates, sticky_cubes):
        self.coordinates = coordinates
        self.sticky_cubes = sticky_cubes


def rotation_matrix(axi, degree90):
    r = Rotation.from_euler({0: 'x', 1: 'y', 2: 'z'}[axi], 90 * degree90, degrees=True)
    return r.as_matrix().T.astype(int)


def display(coordinates):
    coordinates = np.asarray(coordinates)
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    z = coordinates[:, 2]

    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'gray')
    ax.scatter(x, y, z, c=z)
    plt.show()


# def cube_rotate(self, cube_number, action_degree, axis):
#     for problem in range(cube_number, 27):
#         r = Rotate.from_euler(axis, action_degree, degrees=True)
#         self.coordinates[problem] = r.apply(self.coordinates[problem])
#         self.coordinates[problem] = self.coordinates[problem].tolist()  # to check
#         self.coordinates[problem] = list(map(int, self.coordinates[problem]))


# def cubeRotate(self, CubeNumber, actionDegree):
#     for problem in range(CubeNumber, 27):
#         r = Rotate.from_euler('y', actionDegree, degrees=True)
#         self.coordinates[problem] = r.apply(self.coordinates[problem])
#         self.coordinates[problem] = self.coordinates[problem].tolist()

# before :[[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [5, 1, -1], [5, 0, -1], [5, -1, -1], [5, -1, 0], [5, 0, 0], [5, 0, 1], [5, 0, 2], [5, 1, 2], [5, 2, 2], [5, 2, 1], [5, 3, 1], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 5, 1], [5, 5, 2], [5, 4, 2], [5, 3, 2], [5, 3, 3], [5, 3, 4]]
# act: [12, 'x', -90]:g:5:h:9
# after :[[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [5, 1, -1], [5, 0, -1], [5, -1, -1], [5, -1, 0], [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 2, -1], [5, 2, -2], [5, 1, -2], [5, 1, -3], [5, 0, -3], [5, 0, -4], [5, 0, -5], [5, 1, -5], [5, 2, -5], [5, 2, -4], [5, 2, -3], [5, 3, -3], [5, 4, -3]]
# coordinates = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [5, 1, -1], [5, 0, -1], [5, -1, -1], [5, -1, 0], [5, 0, 0], [5, 0, 1], [5, 0, 2], [5, 1, 2], [5, 2, 2], [5, 2, 1], [5, 3, 1], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 5, 1], [5, 5, 2], [5, 4, 2], [5, 3, 2], [5, 3, 3], [5, 3, 4]]
# coordinates = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 2], [0, 1, 1], [0, 1, 0], [0, 2, 0], [0, 2, 1], [0, 2, 2],
#                [1, 2, 2], [1, 2, 1], [1, 2, 0], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 0, 2], [1, 0, 1], [1, 0, 0],
#                [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 2], [2, 1, 1], [2, 1, 0], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


def heuristic(coo):
    max_d = 6
    for i in range(0, 27):
        for j in range(0, 27):
            d = dis(coo[j], coo[i])
            max_d = max(d, max_d)
    # print(f"max_d : ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n {max_d}")
    return max_d - 6


def dis(coo1, coo2):
    return abs(coo1[0] - coo2[0]) + abs(coo1[1] - coo2[1]) + abs(coo1[2] - coo2[2])


coo = [[1, 1, 1], [1, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 2], [-1, 1, 2], [-1, 0, 2], [0, 0, 2],
       [0, -1, 2], [0, -1, 1], [0, -1, 0], [-1, -1, 0], [-2, -1, 0], [-2, -1, 1], [-1, -1, 1], [-1, -1, 2], [-2, -1, 2],
       [-2, 0, 2], [-2, 0, 1], [-1, 0, 1], [-1, 0, 0], [-2, 0, 0], [-2, 1, 0], [-2, 1, 1], [-2, 1, 2]]

sticky = [[0, 1], [1, 2], [2, 3], [5, 6], [6, 7], [9, 10], [10, 11], [11, 12], [17, 18], [20, 21],
          [25, 26]]

# print(coordinates[12-1])
#     # [[0, 0, 0], [1, 0, 0], [2, 0, 0],
#     #            [2, 1, 0],  # [2,0,-1]
#     #            [3, 1, 0], [3, 2, 0], [3, 3, 0],
#     #            [4, 3, 0], [4, 4, 0], [4, 5, 0],
#     #            [3, 5, 0],
#     #            [3, 6, 0], [2, 6, 0], [1, 6, 0],
#     #            [1, 7, 0],
#     #            [1, 8, 0], [2, 8, 0],
#     #            [2, 9, 0],
#     #            [3, 9, 0], [3, 10, 0], [3, 11, 0],
#     #            [2, 11, 0],
#     #            [1, 11, 0], [1, 12, 0], [1, 13, 0],
#     #            [0, 13, 0], [-1, 13, 0]
#     #            ]
#
# sticky_cubes = [[25, 26]]
game = Simulator(coo, sticky)
# # before
display(game.coordinates.tolist())
game.cube_rotate(3, -90, 'z')
display(game.coordinates.tolist())
# print(game.coordinates.tolist())
#
# # after
