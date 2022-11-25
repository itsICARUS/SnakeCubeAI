from queue import PriorityQueue

import numpy as np

from Sim import *

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

connected = [[25, 26]]
# print(np.diff(coo, axis=0))
# print(np.diff(np.diff(coo, axis=0), axis=0))
print(np.transpose([-1, -1, -1])[1])

root_game = Simulator(coo, connected)
interface = Interface(root_game)

q = [[root_game, []]]
# append the first game as (game, action_history)=[root_game, []]

que = PriorityQueue()
que.put((float('inf'), 0))
while not que.empty():
    nextMove = que.get()[1]
    print(nextMove)
