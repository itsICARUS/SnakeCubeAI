from gui import display
from ai import *
import numpy as np

if __name__ == "__main__":
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

    display(game.coordinates)
    action_count = 0
    while not (interface.goal_test()):
        # input_n1 = int(input("Enter first cube number (not change): "))
        # input_n2 = int(input("Enter second cube numberToChange: "))
        # inputDegree = int(input("Enter Degree (90 -90 or 180): "))

        action = agent.act(interface.perceive())
        print("attempting", action)

        interface.evolve(action)
        # input_n1, input_n2, inputDegree
        display(game.coordinates)
        action_count += 1
    print("And finally , It's a CUBE !!")
else:
    print("What's this??")
