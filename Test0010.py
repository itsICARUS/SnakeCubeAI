import numpy as np
from gui import display
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
'''in range (0 , 26)'''
game = Simulator(coo, connected)
interface = Interface(game)
interface.is_not_ghostly([[25, 26], [25, 24], [25, 26]])
display(coo)
actions_list = interface.valid_actions()
print(f"valid actions : {actions_list}")
# def cartesian_product(*arrays):
#     la = len(arrays)
#     print(*arrays)
#     # dtypes = numpy.result_type(numpy.asarray(*arrays))
#     # print(f"dtypes{dtypes.type}")
#     arr = numpy.empty([len(a) for a in arrays] + [la], dtype=object)
#     for i, a in enumerate(numpy.ix_(*arrays)):
#         arr[..., i] = a
#     return arr.reshape(-1, la)
#
#
# print(
#     cartesian_product([1, 2, 3],
#                       [1, 2, 's'])
# )
