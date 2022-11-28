from ai import *
import numpy as np
import matplotlib.pyplot as plt


def display(coordinates):
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    z = coordinates[:, 2]

    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'gray')
    ax.scatter(x, y, z, c=z)
    plt.show()


coo = np.asarray([[0, 0, 0], [1, 0, 0], [2, 0, 0],
                  [2, 1, 0],
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
                  ])
connected = np.asarray([[0, 0, 0], [1, 0, 0], [2, 0, 0],
                        [2, 1, 0],
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
                        ])
game = Simulator(coo, connected)
interface = Interface(game)
agent = Agent()

action_count = 0
print("initial map")
display(game.coordinates)
while not (interface.goal_test()):
    action = agent.act(interface.perceive())
    print("attempting", action)
    interface.evolve( action)
    display(game)
    print("\n")
    action_count += 1

print(
    "\n\nпобеда!!!",
    "\nyour cost (number of actions):", action_count,
    '\n\ncurrent map game:'
)
