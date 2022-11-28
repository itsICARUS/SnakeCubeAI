import json

from AStarAlg import astar
from time import time
from Sim import Simulator


# *** you can change everything except the name of the class, the act function and the percept ***


def action_extractor(act):
    # act : [0] = cube num , [1] = axis , [2] = degree
    axis = 0  # 'x'
    if act[1] == 'y':
        axis = 1
    elif act[1] == 'z':
        axis = 2

    degree = 1  # 90
    if act[2] == 180:
        degree = 2
    elif act[2] == -90:
        degree = -1
    return [act[0], axis, degree]


class Agent:
    # ^^^ DO NOT change the name of the class ***

    def __init__(self):
        self.predicted_actions = []

    def act(self, percept):
        sensor_data = json.loads(percept)
        alg = astar

        if not self.predicted_actions:
            '''runs for first time'''
            t0 = time()
            sticky = sensor_data["stick_together"]
            for i in sticky:
                for j in range(0, len(i)):
                    i[j] += 1
            initial_state = Simulator(sensor_data["coordinates"], sticky)
            self.predicted_actions = alg(initial_state)
            print("run time :\t", time() - t0)
        action_node = self.predicted_actions.pop()

        print(f"They want to do {action_node.act}")

        action = action_extractor(action_node.act)
        # print(f"They want to do {action}")
        return action
