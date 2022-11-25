import json
import numpy as np
from queue import PriorityQueue
from time import time
from ai2.sim import *
# *** you can change everything except the name of the class, the act function and the sensor_data ***


class Agent:
    # ^^^ DO NOT change the name of the class ***

    def __init__(self):
        self.predict_actions = []
        pass

    # the act function takes a json string as input
    # and outputs an action string
    # action example: [1,2,-2]
    # the first number is the joint number (1: the first joint)
    # the second number is the axis number (0: x-axis, 1: y-axis, 2: z-axis)
    # the third number is the degree (1: 90 degree, -2: -180 degree, -1000: -90000 degree)
    def act(self, percept):
        # ^^^ DO NOT change the act function above ***

        sensor_data = json.loads(percept)
        # ^^^ DO NOT change the sensor_data above ***

        # TODO implement your agent here


        if self.predict_actions == [] :
            timeStart = time()
            initial_state = Simulator(sensor_data['coordinates'],sensor_data['stick_together'])
            self.predict_actions = self.BFS(initial_state)
            if self.predict_actions is None : raise Exception("No Solution")
            print("time: ",time()-timeStart)
        action = self.predict_actions.pop()
        # action example: [1,2,-2]
        return action


    def heuristic(self,state):
        axs = state.coordinates.T
        a = abs(np.unique(axs[0],return_counts=True)[1]).sum()+ abs(np.unique(axs[1],return_counts=True)[1]).sum() + abs(np.unique(axs[2],return_counts=True)[1])
        b = (a-81)/len(state.real_joints)
        return

    def AStarRamProblem(self,root_game):
        interface = Interface()

        node=[root_game,[-1,-1,-1]]
        qi = PriorityQueue()
        qi.put((float('inf'),0))
        p =[node]

        #pop first element
        while not qi.empty():
            bestI = qi.get()[1]
            node = p[bestI]
            p[bestI] = None

        #get list of legal actions
        actionList = interface.valid_actions(node[0],np.transpose(node[1])[1])

        for action in actionList:
            #copy the current state
            childState = interface.copy_state(node[0])

            #take action and change copied node
            interface.evolve(childState,action)

            if not interface.valid_state(childState):continue

            #add children to q
            newNode = [childState,[action]+node[1]]
            qi.put((len(node[1])+self.heuristic(childState),len(p)))
            p.append(newNode)

            if interface.goal_test(childState):return [action] + node[1][:-1]

    def BFS(self,root_game):
        interface = Interface()

        q = []
        #append the first state as (State,action_history)
        q.append([root_game,[[-1,-1,-1]]])

        while q:
            #pop first element
            node = q.pop(0)

            #get legal actions
            actionList = interface.valid_actions(node[0],np.transpose(node[1])[1])

            #randomizing the order of child generation
            np.random.shuffle(actionList)

            for action in actionList:
                # copy the current state
                childState = interface.copy_state(node[0])

                interface.evolve(childState,action)

                if not interface.valid_state(childState):continue

                #add children to queue
                q.append([childState,[action]+node[1]])

                #return if goal test is true
                if interface.goal_test(childState):
                    return [action] + node[1][:-1]







