import numpy as np

from Sim import *


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, act=None):
        self.parent = parent
        if act is not None:
            self.act = act[0:4]
            self.h = act[4]
            self.g = parent.g + 1
        else:
            self.act = None
            self.h = float("inf")
            self.g = 0

    def f_getter(self):
        return self.g + self.h

    def __eq__(self, other):
        if self.h == other.h:
            for i in range(0, 4):
                if self.act[i] != other.act[i]:
                    return False
            if self.parent == other.parent:
                return True
        return False


def return_parents(current_node):
    parent_list = []
    while current_node is not None:
        parent_list.append(current_node)
        current_node = current_node.parent
    if parent_list:
        parent_list.pop()
    parent_list.reverse()
    return parent_list


def astar(game):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    main_game = game.coordinates
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
        print(f"first branch act : {act}")
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
            # print(f"{item.f_getter()}  and  {current_node.f_getter()}")
            if item.f_getter() < current_node.f_getter():
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        # take action
        print(f"\nbefore :{game.coordinates}\nact: {current_node.act}:g:{current_node.g}:h:{current_node.h}")

        interface.game.coordinates = main_game
        parents = return_parents(current_node)
        current_node
        for parent in parents:
            interface.evolve(parent.act)
        print(f"after :{game.coordinates}\n\n")
        # interface.evolve(current_node.act)
        closed_list.append(current_node)
        # Found the goal
        if interface.goal_test():
            print("\n\tend\n\n")
            return return_parents(current_node)

        # Generate children
        children = []
        actions_list = interface.valid_actions()
        for act in actions_list:
            # Create new node
            new_node = Node(current_node, act)
            # print(f"act : {act}")
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


def main():
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

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)

    path = astar(Simulator(coo, connected))
    print(path)


if __name__ == '__main__':
    main()
