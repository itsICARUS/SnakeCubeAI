import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as Rotate, Rotation


class Simulator:

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


def cube_rotate(self, cube_number, action_degree, axis):
    for i in range(cube_number, 27):
        r = Rotate.from_euler(axis, action_degree, degrees=True)
        self.coordinates[i] = r.apply(self.coordinates[i])
        self.coordinates[i] = self.coordinates[i].tolist()  # to check
        self.coordinates[i] = list(map(int, self.coordinates[i]))


# def cubeRotate(self, CubeNumber, actionDegree):
#     for i in range(CubeNumber, 27):
#         r = Rotate.from_euler('y', actionDegree, degrees=True)
#         self.coordinates[i] = r.apply(self.coordinates[i])
#         self.coordinates[i] = self.coordinates[i].tolist()


coordinates = [[0, 0, 0], [1, 0, 0], [2, 0, 0],
               [2, 1, 0],#[2,0,-1]
               [3, 1, 0], [3, 2, 0], [3, 3, 0],
               [4, 3, 0], [4, 4, 0], [4, 5, 0],
               [3, 5, 0],
               [3, 6, 0], [2, 6, 0], [1, 6, 0],
               [1, 7, 0],
               [1, 8, 0], [2, 8, 0],
               [2, 9, 0],
               [3, 9, 0], [3, 10, 0], [3, 11, 0],
               [2, 11, 0],
               [1, 11, 0], [1, 12, 0], [1, 13, 0],
               [0, 13, 0], [-1, 13, 0]
               ]

connected = [[25, 26]]
game = Simulator(coordinates, connected)
# before
display(game.coordinates)
cube_rotate(game, 7-1, 90 ,'z')
display(game.coordinates)
print(game.coordinates)
# after
