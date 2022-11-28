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
            # print(sticky_cubes_original)
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
        # self.cube_rotate(random_cube-1, random_degree, axis)
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

    # def cube_rotate(self, cube_number, action_degree, axis):
    #     self.coordinates = numpy.array(self.coordinates).astype(int)
    #     to_minus = self.coordinates[cube_number]
    #     self.coordinates = self.coordinates - to_minus
    #     for problem in range(cube_number, 27):
    #         r = Rotate.from_euler(axis, action_degree, degrees=True)
    #         self.coordinates[problem] = r.apply(self.coordinates[problem])
    # # def cube_rotate(self, cube_number, action_degree, axis):
    # #     for problem in range(cube_number, 27):
    # #         r = Rotate.from_euler(axis, action_degree, degrees=True)
    # #         self.coordinates[problem] = r.apply(self.coordinates[problem])
    # #         self.coordinates[problem] = self.coordinates[problem].tolist()  # to check
    # #         self.coordinates[problem] = list(map(int, self.coordinates[problem]))

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
        coo = self.coordinates
        # axis1, axis2 = self.get_axis(actionCubeNum1 - 1, actionCubeNum2 - 1)
        # print(axis1)
        # print(axis2)
        # boolConnected, d1ArrayConnected, indexConnected = self.isConnected(actionCubeNum2 - 1)
        #
        # if (boolConnected == False and axis1 == axis2):  # firsh part
        #     print("nothing happend !")
        # elif (boolConnected == False and axis1 != axis2):  # second part
        #     print("ssss")
        #     self.cubeRotate(actionCubeNum2 - 1, actionDegree)
        # elif (boolConnected == True and axis1 != axis2):  # second part
        #     self.cubeRotate(actionCubeNum2 - 1, actionDegree)
        # axis = self.get_axis(action_cube_num - 1) \\todo commented by mohamad javad
        bool_connected, array_connected, index_connected = self.is_connected(action_cube_num - 1)

        if not bool_connected:  # second part
            self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
        # # self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
        # # if not bool_connected and action_axis == axis:  # first part \\\\todo commented by mohamad javad
        # # #     print("nothing happened !")
        # # elif not bool_connected and action_axis != axis:  # second part
        # #     self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
        # # # elif bool_connected and action_axis != axis:  # second part
        # # #     self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
        # # TODO !!!!!
        # if bool_connected:
        #
        #     for iConnected in array_connected:
        #         '''for all sticky_cubes cubes to the action_cube'''
        #         if iConnected != index_connected:
        #             '''is not the action cube itself'''
        #             if iConnected + 1 not in array_connected:
        #                 '''and its the last one'''
        #                 temp_axis = self.get_axis(iConnected - 1)
        #                 '''get axis of <the last one and the one after it>'''
        #                 if action_axis != temp_axis:
        #                     '''if they are not same'''
        #                     self.cube_rotate(iConnected - 1, action_degree, action_axis)
        real_action_axis = self.get_axis(action_cube_num - 1)
        flag = False
        if action_cube_num < 26:
            flag = True
            next_action_axis = self.get_axis(action_cube_num - 1 + 1)
        if bool_connected:
            if flag and real_action_axis != next_action_axis:  # second part
                self.cube_rotate(action_cube_num - 1 + 1, action_degree, action_axis)
            for iConnected in array_connected:
                '''for all sticky_cubes cubes to the action_cube'''
                if iConnected != index_connected:
                    '''is not the action cube itself'''
                    if iConnected + 1 not in array_connected:
                        '''and its the last one'''
                        temp_axis = self.get_axis(iConnected - 1)
                        '''get axis of <the last one and the one after it>'''
                        if action_axis != temp_axis:
                            '''if they are not same'''
                            self.cube_rotate(iConnected - 1, action_degree, action_axis)
        if not check_coordinates(self.coordinates):
            self.coordinates = coo


def dis(coo1, coo2):
    return abs(coo1[0] - coo2[0]) + abs(coo1[1] - coo2[1]) + abs(coo1[2] - coo2[2])


def heuristic(coo):
    max_d = 6
    for i in range(0, 27):
        for j in range(0, 27):
            d = dis(coo[j], coo[i])
            max_d = max(d, max_d)
    # print(f"max_d : ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n {max_d}")
    return max_d - 6
    # x = coordinates[:, 0]
    # y = coordinates[:, 1]
    # z = coordinates[:, 2]
    # a = abs(numpy.unique(x, return_counts=True)[1]).sum() \
    #     + abs(numpy.unique(y, return_counts=True)[1]).sum() + abs(numpy.unique(z, return_counts=True)[1].sum())
    # # b = (a - 81) / len(state.real_joints)
    # return a - 81


class Interface:

    def __init__(self, game):
        self.game = game
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
            # print(row)
            for i in range(0, 3):
                for j in range(0, 3):
                    for k in range(0, 3):
                        for point in self.game.coordinates:
                            if row[0] + i == point[0] and row[1] + j == point[1] and row[2] + k == point[2]:  # and ...
                                counter += 1
                            # else:
                            # break
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

    # def getEachPosition(self):
    # for(int problem = 0 ; problem<27 ; problem++):
    def perceive(self):
        return [self.game.coordinates, self.game.sticky_cubes]

    def valid_actions(self):

        return self.filter_impossibles()

    def filter_impossibles(self):
        coordinates = self.game.coordinates
        true_actions = []
        for action_cube_num in range(1, 28):
            possible_axes_place = self.get_possible_axes_place(action_cube_num - 1)
            # print(f"possible axes :{possible_axes_place} in cube={action_cube_num}\n")
            if len(possible_axes_place) == 0:
                continue
            possible_axes = possible_axes_place[:, 0]
            # print(f"possible axes :{possible_axes} in cube={action_cube_num}\n")
            actions_space = cartesian_product(possible_axes,
                                              self.valid_actions_degree()
                                              )
            # for act in actions_space[action_cube_num * 9: (action_cube_num + 1) * 9]:
            for act in actions_space:
                # print(f"act:{act}")
                # print(f"(ACT SPACE).pop() IS :{actions_space[-1]}\n")
                action_axis = act[0]
                # print(f"possible axes :{possible_axes} ,cube_num={action_cube_num}\n act axis_place is :{
                # action_axis}")
                # if action_axis in possible_axes:
                for axis_place in possible_axes_place:
                    # print(f"axis_place: {axis_place}\taction_axis: {action_axis}")
                    if axis_place[0] == action_axis:
                        # print("action_cube_num Have 1")
                        # print(f"act :{act} in axis_place[1]={axis_place[1]}\n")
                        coo = self.is_a_possible_degree(action_cube_num, act, axis_place[1])
                        if coo is not None:
                            # true_act = [action_cube_num, act[0], act[1], int(axis_place[1]), heuristic(coo)]
                            # print(f"\nit's valid : {true_act} on {coordinates}\nto coo: {coo}")
                            true_act = [action_cube_num, act[0], act[1], coo]
                            true_actions.append(true_act)
                            # print(f"true_actions.append(act) :{true_act} \n")
                #             print(f"\nit's valid : {act} on {coordinates[action_cube_num]}\n")  # //TODO
            # axis_place = self.game.get_axis(action_cube_num - 1)
            # bool_connected, array_connected, index_connected = self.is_connected(action_cube_num - 1)
            # if not bool_connected and action_axis == axis_place:  # first part
            #     print("nothing happened !")
            # elif not bool_connected and action_axis != axis_place:  # second part
            #     self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
            # elif bool_connected and action_axis != axis_place:  # second part
            #     self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
            #
            # if bool_connected:
            #     z = 1
            #     for iConnected in array_connected:
            #         if iConnected != index_connected:
            #             if iConnected + 1 not in array_connected:
            #                 temp_axis = self.get_axis(iConnected - 1)
            #                 if action_axis != temp_axis:
            #                     self.cube_rotate(iConnected - 1, action_degree, action_axis)

            # if x[0] != 26:
            #     print(x[2])

        return true_actions

    def get_possible_axes_place(self, cube_num):
        axes = []
        connected, array_connected, index = self.game.is_connected(cube_num)

        if not connected:
            # print(f"CUBE NUMBER started is :{cube_num}\n")
            if 26 > cube_num > 0:
                ax_before = self.game.get_axis(cube_num - 1)
                ax_after = self.game.get_axis(cube_num)
                if ax_after != ax_before:
                    axes.append([ax_after, 0])
                # print(f"CUBE NUMBER IS less than 26 :{cube_num}\n")
            # if cube_num > 0:
            #     # print(f"CUBE NUMBER IS more than 0 :{cube_num}\n")
            #     axes.append([self.game.get_axis(cube_num - 1), -1])
            '''it was the left hand which is commented(deleted) up'''
        else:
            flag = True
            if index == 0:
                '''it is sticky_cubes to next one'''
                # if cube_num > 0:
                #     axes.append([self.game.get_axis(cube_num - 1), -1])
                '''it was the left hand which is commented(deleted) up '''
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
                # for problem in range(1, len(array_connected)):
                #     if cube_num - problem < 2:
                #         flag = False
                #         break
                #     if self.game.get_axis(cube_num - problem) != self.game.get_axis(cube_num - problem - 1):
                #         flag = False
                #         break
                # if flag:
                #     axes.append([self.game.get_axis(array_connected[-1] - 2),
                #                  -len(array_connected) + 1])
                '''it was the left hand which is commented(deleted) up '''
        return numpy.asarray(axes)

    def is_a_possible_degree(self, action_cube_num, act, which_neighbor_cube_if_is_con):
        # print(f"coordinates : {self.game.coordinates}\nselll: {action_cube_num}:{act}:{
        # which_neighbor_cube_if_is_con}")
        action_axis = act[0]
        action_degree = act[1]
        coo = self.cube_rotate(action_cube_num + int(which_neighbor_cube_if_is_con), action_degree, action_axis)
        # print(f"cube_num:{action_cube_num}\tact :{act} ,which_neighbor_cube_if_is_con={
        # which_neighbor_cube_if_is_con}\n" f"{coo}")
        if check_coordinates(coo):
            return coo
            # flag = False
            # # print( f"coo:{coo}\ncoordinates :{self.game.coordinates}")
            # for index, coord in enumerate(coo,0):
            #     for problem in range(0, 3):
            #         if coord[problem] != self.game.coordinates[index][problem]:
            #             flag = True
            # if flag:
            #     return coo
        return None

        # axis = self.game.get_axis(action_cube_num - 1)
        # bool_connected, array_connected, index_connected = self.game.is_connected(action_cube_num - 1)
        # if bool_connected:
        #     for iConnected in array_connected:
        #         if iConnected != index_connected:
        #             '''is not the action cube itself'''
        #             if iConnected + 1 not in array_connected:
        #                 '''and it's the last one'''
        #                 temp_axis = self.game.get_axis(iConnected - 1)
        #                 '''get axis of <the last one and the one after it>'''
        #                 if action_axis != temp_axis:
        #                     '''if they are not in the same axis'''
        #                     self.cube_rotate(iConnected - 1, action_degree, action_axis)
        # else :
        #     if action_axis != axis:  # second part
        #         self.cube_rotate(action_cube_num - 1, action_degree, action_axis)
        #     elif action_axis != axis:

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

        # # print(f"action_cube_num: {action_cube_num} action_degree: {action_degree} action_axis:{action_axis}")
        # # print(f"coo before:{coo}" )
        # for problem in range(action_cube_num, 27):
        #     r = Rotate.from_euler(action_axis, action_degree, degrees=True)
        #     coo[problem] = r.apply(coo[problem])
        #     coo[problem] = coo[problem].tolist()
        #     '''to convert to int'''
        #     coo[problem] = list(map(int, coo[problem]))
        # # print(f"game after{self.game.coordinates}")
        return coo

    # @staticmethod
    # def is_not_ghostly(coo):
    #     new_list = []
    #     for problem in coo:
    #         # if problem not in new_list:
    #         for j in new_list:
    #             flag = True
    #             for x in range(0, len(problem)):
    #                 if problem[x] != j[x]:
    #                     flag = False
    #                     break
    #             if flag:
    #                 # print(f"coo : {coo}\nproblem : {problem} j : {j}\n\n")
    #                 return False
    #         new_list.append(problem)
    #     return True


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
