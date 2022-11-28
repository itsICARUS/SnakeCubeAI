from Sim import heuristic, Interface
from gui import display
import matplotlib.pyplot as plt


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, act=None):
        self.parent = parent
        if act is not None:
            self.act = act[0:3]
            self.coo = act[3]
            self.h = heuristic(self.coo)
            self.g = parent.g + 1
        else:
            self.act = None
            self.h = float("inf")
            self.g = 0
            self.coo = None

    def f_getter(self):
        return self.g + self.h

    def __eq__(self, other):
        for index, coord in enumerate(self.coo, 0):
            if other.coo is None:
                return False
            for i in range(0, 3):
                if coord[i] != other.coo[index][i]:
                    return False
        return True


def return_parents(current_node):
    parent_list = []
    while current_node is not None:
        parent_list.append(current_node)
        current_node = current_node.parent
    if parent_list:
        parent_list.pop()
    list1 = parent_list.copy()
    list1.reverse()
    # for i in list1:
    #     print(f"\tdisplaying be: {game_init.coordinates.tolist()}\n\n\n\n\n\n")
    #     x = game_init.coordinates[:, 0]
    #     y = game_init.coordinates[:, 1]
    #     z = game_init.coordinates[:, 2]
    #     ax = plt.axes(projection='3d')
    #     ax.plot3D(x, y, z, 'gray')
    #     ax.scatter(x, y, z, c=z)
    #     plt.show()
    #
    #     x = i.act
    #     game_init.take_action(i.act[0], i.act[1], i.act[2])
    #     # game_init.cube_rotate(i.act[0] - 1, i.act[2], i.act[1])
    #     print(f"act is {i.act}")
    #     print(f"\tdisplaying af: {game_init.coordinates.tolist()}\n\n\n\n\n\n")
    #     x = game_init.coordinates[:, 0]
    #     y = game_init.coordinates[:, 1]
    #     z = game_init.coordinates[:, 2]
    #     ax = plt.axes(projection='3d')
    #     ax.plot3D(x, y, z, 'gray')
    #     ax.scatter(x, y, z, c=z)
    #     plt.show()
    return parent_list


def astar(game):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    interface = Interface(game)
    # Create start and end node
    start_node = Node(None, None)
    """ f(=:total cost) = g + h """
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    actions_list = interface.valid_actions()
    for act in actions_list:
        # Create new node
        new_node = Node(start_node, act)
        # Append
        open_list.append(new_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        # finding the best index & node
        for index, item in enumerate(open_list):
            if item.f_getter() < current_node.f_getter():
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        # take action

        # print(f"\nAI: before I think more :{game.coordinates.tolist()}"
        #       f"\nact: {current_node.act}:g:{current_node.g}:h:{current_node.h}")
        # # current_node
        interface.game.coordinates = current_node.coo
        # # interface.evolve(current_node.act)
        # print(f"AI: after I think more :{game.coordinates.tolist()}\n\n")
        closed_list.append(current_node)
        # Found the goal
        if interface.goal_test():
            parents = return_parents(current_node)
            # for i in parents:
            #     print(i.act)
            # display(game.coordinates)
            # print("\n\tAI: I know a solution ...\n\n")

            return parents

        # Generate children
        children = []
        actions_list = interface.valid_actions()
        for act in actions_list:
            # Create new node
            new_node = Node(current_node, act)
            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
