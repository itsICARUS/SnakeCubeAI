from scipy.spatial.transform import Rotation as Rotate
import random
import numpy


class Simulator:

    def __init__(self, coordinates, sticky_cubes):
        self.coordinates = numpy.asarray(coordinates)
        self.sticky_cubes = self.change_sticky_cubes(sticky_cubes)

    @staticmethod
    def change_sticky_cubes(sticky_cubes_original):
        helper_sticky_cubes = []
        a = 0
        ep = len(sticky_cubes_original) - 1
        for i in range(0, ep):
            if i + 1 + a <= len(sticky_cubes_original) - 1:
                if (sticky_cubes_original[i + a][len(sticky_cubes_original[i + a]) - 1] ==
                        sticky_cubes_original[i + a + 1][
                            0]):
                    helper_sticky_cubes.append(sticky_cubes_original[i + a])
                    helper_sticky_cubes[i].append(sticky_cubes_original[i + a + 1][1])
                    sticky_cubes_original.pop(i + a + 1)

                    a = a - 1
                else:
                    helper_sticky_cubes.append(sticky_cubes_original[i + a])
        return sticky_cubes_original

    def open_cube(self):
        coo = numpy.asarray(self.coordinates.copy())
        random_cube = random.randint(1, 27)
        random_axis = random.randint(1, 3)
        random_degree = random.randrange(90, 270, 90)
        print(f"{random_cube}:{random_degree}:{random_axis}")
        if random_axis == 1:
            axis = 'x'
        elif random_axis == 2:
            axis = 'y'
        else:
            axis = 'z'
        self.take_action(random_cube - 1, axis, random_degree)
        print(f"{coo.tolist()}\nvs cs\n{self.coordinates.tolist()}")
        if numpy.array_equiv(coo, self.coordinates):
            self.open_cube()

    def get_axis(self, cube_num):

        axis = ''
        if self.coordinates[cube_num][0] != self.coordinates[cube_num + 1][0]:
            axis = 'x'
        elif self.coordinates[cube_num][1] != self.coordinates[cube_num + 1][1]:
            axis = 'y'
        elif self.coordinates[cube_num][2] != self.coordinates[cube_num + 1][2]:
            axis = 'z'

        return axis

    def is_connected(self, action_cube_num):

        flag = False
        index = -1
        array_connected = []

        for i in range(0, len(self.sticky_cubes)):
            for j in range(0, len(self.sticky_cubes[i])):
                if self.sticky_cubes[i][j] == action_cube_num:
                    flag = True
                    array_connected = self.sticky_cubes[i]
                    index = j

        return flag, array_connected, index

    def cube_rotate(self, cube_number, action_degree, axis):

        self.coordinates = numpy.array(self.coordinates).astype(int)
        to_minus = self.coordinates[cube_number]
        self.coordinates = self.coordinates - to_minus
        for i in range(cube_number, 27):
            r = Rotate.from_euler(axis, action_degree, degrees=True)
            rr = r.as_matrix().T.astype(int)
            self.coordinates[i] = self.coordinates[i] @ rr

        numpy.array(self.coordinates).astype(int)
        self.coordinates = self.coordinates + to_minus

    def check_coordinates(self):
        for i in range(0, len(self.coordinates)):
            for j in range(0, len(self.coordinates)):
                if i != j:
                    temp = 0
                    for z in range(0, 3):
                        if self.coordinates[i][z] == self.coordinates[j][z]:
                            temp += 1
                    if temp == 3:
                        return False
        return True

    def take_action(self, action_cube_num, action_axis, action_degree):
        coo = self.coordinates.copy()
        bool_connected, array_connected, index_connected = self.is_connected(action_cube_num - 1)
        if not bool_connected:
            self.cube_rotate(action_cube_num - 1, action_degree, action_axis)

        else:
            if len(array_connected) == index_connected + 1:
                self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
            else:
                if self.get_axis(array_connected[-1]) == action_axis:
                    self.cube_rotate(array_connected[-1] - 1, action_degree, action_axis)

        if not check_coordinates(self.coordinates):
            self.coordinates = coo
            print("attention !!!!!\nnothing happen!\n attention !!!!!")


def dis(coo1, coo2):
    return abs(coo1[0] - coo2[0]) + abs(coo1[1] - coo2[1]) + abs(coo1[2] - coo2[2])


def heuristic(coo):
    max_d = 6
    for i in range(0, 27):
        for j in range(0, 27):
            d = dis(coo[j], coo[i])
            max_d = max(d, max_d)
    return max_d - 6


class Interface:

    def __init__(self, game):
        self.game = Simulator(game.coordinates, game.sticky_cubes)
        pass

    # an example for what this class is supposed to do
    # here, it will make sure the action that is being
    # requested is in a correct format. this func won't return anything
    # the actual simulator must only deal with the game logic and nothing more
    def evolve(self, action):
        action_num = action[0]
        action_axis = action[1]
        action_degree = action[2]

        if type(action_num) is not int:
            raise ("action_num is not a int")
        if type(action_axis) is not str:
            raise ("action_axis is not a str")
        if type(action_degree) is not int:
            raise ("action_degree is not a int")
        # action = action.upper()
        if action_num not in self.valid_actions_cube():
            raise ("action_num is not valid")
        if action_axis not in self.valid_actions_axis():
            raise ("action_axis is not valid")
        if action_degree not in self.valid_actions_degree():
            raise ("action_degree is not valid")

        self.game.take_action(action_num, action_axis, action_degree)

    def goal_test(self):

        # TODO return if goal has been reached
        counter = 0
        for row in self.game.coordinates:
            counter = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    for k in range(0, 3):
                        for point in self.game.coordinates:
                            if row[0] + i == point[0] and row[1] + j == point[1] and row[2] + k == point[2]:  # and ...
                                counter += 1
            if counter == 27:
                break
        if counter == 27:
            return True
        else:
            return False

    @staticmethod
    def valid_actions_cube():

        # TODO return list of legal actions
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

    @staticmethod
    def valid_actions_axis():
        return ['x', 'y', 'z']

    @staticmethod
    def valid_actions_degree():

        # TODO return list of legal actions
        return [90, -90, 180]

    def perceive(self):
        perc = "{\"coordinates\": " + \
               f"{self.game.coordinates.tolist()}, \"stick_together\":" \
               f" {numpy.asarray(self.game.sticky_cubes, dtype=object).tolist()}" \
               + "}"
        return perc

    def valid_actions(self):

        return self.filter_impossibles()

    def filter_impossibles(self):
        true_actions = []
        for action_cube_num in range(1, 28):
            possible_axes_place = self.get_possible_axes_place(action_cube_num - 1)
            if len(possible_axes_place) == 0:
                continue
            possible_axes = possible_axes_place[:, 0]
            actions_space = cartesian_product(possible_axes,
                                              self.valid_actions_degree())
            for act in actions_space:
                action_axis = act[0]
                for axis_place in possible_axes_place:
                    if axis_place[0] == action_axis:
                        coo = self.is_a_possible_degree(action_cube_num, act, axis_place[1])
                        if coo is not None:
                            true_act = [action_cube_num, action_axis, act[1], coo]
                            true_actions.append(true_act)

        return true_actions

    def get_possible_axes_place(self, cube_num):
        axes = []
        connected, array_connected, index = self.game.is_connected(cube_num)
        if not connected:
            if 26 > cube_num > 0:
                ax_before = self.game.get_axis(cube_num - 1)
                ax_after = self.game.get_axis(cube_num)
                if ax_after != ax_before:
                    axes.append([ax_after, 0])
        else:
            flag = True
            if index == 0:
                '''it is sticky_cubes to next one'''
                for i in array_connected:
                    i -= 1
                    if i > 23:
                        flag = False
                        break
                    if self.game.get_axis(i) != self.game.get_axis(i + 1):
                        flag = False
                        break
                if flag:
                    axes.append([self.game.get_axis(array_connected[0] - 2),
                                 len(array_connected) - 1])
            elif array_connected[index] == array_connected[-1]:
                """it is sticky_cubes to the prev one"""
                if cube_num < 26:
                    axes.append([self.game.get_axis(cube_num), 0])
        return numpy.asarray(axes)

    def is_a_possible_degree(self, action_cube_num, act, which_neighbor_cube_if_is_con):
        action_axis = act[0]
        action_degree = act[1]
        coo = self.cube_rotate(action_cube_num + int(which_neighbor_cube_if_is_con), action_degree, action_axis)
        if check_coordinates(coo):
            return coo
        return None

    def cube_rotate(self, action_cube_num, action_degree, action_axis):
        coo = numpy.asarray(self.game.coordinates).copy()
        coo = numpy.array(coo).astype(int)
        to_minus = coo[action_cube_num]
        coo = coo - to_minus
        for i in range(action_cube_num, 27):
            r = Rotate.from_euler(action_axis, action_degree, degrees=True)
            rr = r.as_matrix().T.astype(int)
            coo[i] = coo[i] @ rr

        numpy.array(coo).astype(int)
        coo = coo + to_minus
        return coo


def cartesian_product(*arrays):
    la = len(arrays)
    arr = numpy.empty([len(a) for a in arrays] + [la], dtype=object)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[..., i] = a
    return arr.reshape(-1, la)


def check_coordinates(coordinates):
    for i in range(0, len(coordinates)):
        for j in range(0, len(coordinates)):
            if i != j:
                temp = 0
                for z in range(0, 3):
                    if coordinates[i][z] == coordinates[j][z]:
                        temp += 1
                if temp == 3:
                    return False
    return True
