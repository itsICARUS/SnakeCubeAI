import random
from queue import PriorityQueue
from time import time
from Sim import Simulator, Interface
import numpy as np
import json


# *** you can change everything except the name of the class, the act function and the percept ***


class Agent:
    # ^^^ DO NOT change the name of the class ***

    def __init__(self):
        self.predicted_actions = []

    # the act function takes a json string as input
    # and outputs an action string
    # ('U' is go up,   'L' is go left,   'Rotate' is go right,   'D' is go down,  'C' is clean tile)
    # def act(self, percept):
    # ^^^ DO NOT change the act function above ***

    # percept = json.loads(percept)
    # ^^^ DO NOT change the percept above ***
    def act(self, percept):
        alg = self.BFS_SAMPLE_CODE

        if not self.predicted_actions:
            '''runs for first time'''
            t0 = time()
            initial_state = Simulator(percept[0], percept[1])
            self.predicted_actions = alg(initial_state)
            print("run time :\t", time() - t0)

        action = self.predicted_actions.pop()
        return action

    def BFS_SAMPLE_CODE(self, root_game):
        interface = Interface(root_game)

        q = [[root_game, []]]
        # append the first game as (game, action_history)=[root_game, []]

        pq = PriorityQueue()
        pq.put((float('inf'), 0))
        while not pq.empty():
            next_move = pq.get()
            print(f"next_move: {next_move}")
            # pop first element from queue

            # get the list of legal actions
            actions_list = interface.valid_actions()

            # # randomizing the order of child generation
            # random.shuffle(actions_list)

            for action in actions_list:
                # copy the current game
                child_state = interface.copy_state(node[0])

                # take action and change the copied node
                interface.evolve(child_state, action)

                # add children to queue
                q.append([child_state, [action] + node[1]])

                # return if goal test is true
                if interface.goal_test(child_state):
                    return [action] + node[1]

    def heuristic(self, coordinates):
        x = coordinates[:, 0]
        y = coordinates[:, 1]
        z = coordinates[:, 2]
        a = abs(np.unique(x, return_counts=True)[1]).sum() \
            + abs(np.unique(y, return_counts=True)[1]).sum() + abs(np.unique(z, return_counts=True)[1])
        # b = (a - 81) / len(state.real_joints)
        return a-81
