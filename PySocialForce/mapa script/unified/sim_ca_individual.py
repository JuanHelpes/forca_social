# -*- coding:utf-8 -*-

from sim_ca_constants import Constants

from random import randint
from math import exp

class Individual(object):

    def __init__(self, configuration, col, row):
        self.label = configuration["label"]
        self.color = (configuration["red"], configuration["green"], configuration["blue"])
        self.speed = configuration["speed"]
        self.KD = configuration["KD"] # Dinamic map const
        self.KS = configuration["KS"] # Static map const
        self.KW = configuration["KW"] # Wall map const
        self.KI = configuration["KI"] # Inertia const
        self.old_direction = -1

        self.row = row
        self.col = col
        self.evacuated = False
        self.steps = 0


    def move(self, structure_map, wall_map, static_map, crowd_map, dinamic_map):
        directions = [   Constants.D_TOP,
            Constants.D_TOP_RIGHT,
            Constants.D_RIGHT,
            Constants.D_BOTTOM_RIGHT,
            Constants.D_BOTTOM,
            Constants.D_BOTTOM_LEFT,
            Constants.D_LEFT,
            Constants.D_TOP_LEFT
        ]

        initial_directions = []
        for direction in directions:
            initial_directions.append((self.row + direction[0], self.col + direction[1]))

        for direction in initial_directions:
            if structure_map.isSaida(direction[0], direction[1]):
                crowd_map.update_individual_position(self.row, self.col, direction[0], direction[1])
                self.row = direction[0]
                self.col = direction[1]
                return {"row":direction[0], "col":direction[1], "direct":-2}

        possible_directions = []
        for i in range(len(initial_directions)):
            if static_map.field_exist(initial_directions[i]) and crowd_map.check_empty_position(initial_directions[i][0], initial_directions[i][1]):
                if structure_map.map[initial_directions[i][0]][initial_directions[i][1]] in [Constants.M_EMPTY, Constants.M_DOOR]:
                    possible_directions.append({"direct":i, "row":initial_directions[i][0], "col":initial_directions[i][1]})

        if not possible_directions:
            self.old_direction = -1
            return

        total = 0
        for direction in possible_directions:
            D = dinamic_map.calc_dinamic_value(direction["row"], direction["col"], self.KD)
            S = static_map.calc_static_value(direction["row"], direction["col"], self.KS)
            I = self.calc_inertial_value(direction["direct"])
            W = wall_map.calc_wall_value(direction["row"], direction["col"], self.KW)
            direction["move_chance"] = D * S * I * W
            total += direction["move_chance"]

        possible_directions[0]["move_chance"] /= total
        for i in range(1, len(possible_directions)):
            possible_directions[i]["move_chance"] = possible_directions[i-1]["move_chance"] + possible_directions[i]["move_chance"] / total

        init = 0
        sorted_number = randint(0, 100) / 100
        new_direction = possible_directions[0]
        for i in range(len(possible_directions)):
            if sorted_number < possible_directions[i]["move_chance"] and sorted_number > init:
                new_direction = possible_directions[i]
                break
            init = possible_directions[i]["move_chance"]



        if not (new_direction["row"] == self.row and new_direction["col"] == self.col):
            crowd_map.update_individual_position(self.row, self.col, new_direction["row"], new_direction["col"])
            self.row = new_direction["row"]
            self.col = new_direction["col"]
            self.old_direction = new_direction["direct"]
            return {"row":new_direction["row"], "col":new_direction["col"], "direct":new_direction["direct"]}

        self.old_direction = -1
        return 


    def calc_inertial_value(self, new_direction):
        if new_direction == self.old_direction:
            return exp(self.KI)
        return 1


    def __str__(self):
        string = f"Label: {self.label}\t R:{self.red}\t G:{self.green}\t B:{self.blue}\t Speed:{self.speed}\t"
        string += f"KD: {self.KD}\t KS:{self.KS}\t KW:{self.KW}\t KI:{self.KI}\t KD:{self.KD}"
        return string
