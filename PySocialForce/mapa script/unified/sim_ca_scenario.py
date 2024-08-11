
from sim_ca_crowd_map import CrowdMap
from sim_ca_individual import Individual
from sim_ca_dinamic_map import DinamicMap
from sim_ca_static_map import StaticMap
from sim_ca_structure_map import StructureMap
from sim_ca_wall_map import WallMap

import random
import os
import json

class Scenario(object):


    def __init__(self, experiment, doors=None, draw=False, scenario_seed=0, simulation_seed=0):
        self.directory = experiment

        self.sep = os.path.sep
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath("simulator"))) + self.sep        
        self.draw_path = self.root_path + "output" + self.sep + self.directory + self.sep
        
        self.structure_map = self.load_structure_map()
        self.doors_configurations = self.extract_doors_info()

        if doors is None and draw==False and scenario_seed==0 and simulation_seed==0:
            return

        self.draw = draw
        self.scenario_seed = scenario_seed
        self.simulation_seed = simulation_seed

        self.num_simulation = 0
        self.num_scenario = 0

        self.wall_map = None
        self.static_map = None
        self.crowd_map = None
        self.dinamic_map = None
        self.individuals = None

        if doors is not None:
            self.map_reset(doors)
        else:
            self.load_wall_map()
            self.load_static_map()
            self.load_dinamic_map()
            self.load_individuals()
            random.seed(self.scenario_seed)
            self.load_crowd_map()


    def load_structure_map(self):
        structure_map = StructureMap(self.directory, self.root_path + "input" + self.sep + self.directory + self.sep + "map.txt")
        structure_map.load_map()
        return structure_map


    def load_wall_map(self):
        self.wall_map = WallMap(self.directory, self.structure_map)
        self.wall_map.load_map()
        if (self.draw):
            self.wall_map.draw_map(self.root_path + "output" + self.sep + self.directory)


    def load_static_map(self):
        self.static_map = StaticMap(self.directory, self.structure_map)
        self.static_map.load_map()
        if (self.draw):
            self.static_map.draw_map(self.root_path + "output" + self.sep + self.directory)


    def load_dinamic_map(self):
        self.dinamic_map = DinamicMap(self.directory, self.structure_map)
        self.dinamic_map.load_map()


    def load_individuals(self):
        self.individuals = []
        with open(self.root_path + "input" + self.sep + self.directory + self.sep + "individuals.json", 'r') as json_file:
            data = json.load(json_file)
            for caracterization in data['caracterizations']:
                for _ in range(caracterization['amount']):
                    self.individuals.append(Individual(caracterization, 0, 0))

    
    def load_crowd_map(self):
        self.crowd_map = CrowdMap(self.directory, self.structure_map)
        random.seed(self.scenario_seed)
        self.crowd_map.load_map(self.individuals)
        if (self.draw):
            self.crowd_map.draw_map(self.root_path + "output" + self.sep + self.directory, 0)


    def extract_doors_info(self):
        doors_info = []
        visited = set()

        for row in range(len(self.structure_map.map)):
            for col in range(len(self.structure_map.map[row])):
                if self.structure_map.map[row][col] == 2 and (row, col) not in visited:
                    door_info = {'row': row, 'col': col, 'size': 0, 'direction': ''}

                    if col < len(self.structure_map.map[row]) - 1 and self.structure_map.map[row][col + 1] == 2:
                        door_info['direction'] = 'H'

                        c = col
                        while c < len(self.structure_map.map[row]) and self.structure_map.map[row][c] == 2:
                            door_info['size'] += 1
                            visited.add((row, c))
                            c += 1
                    elif row < len(self.structure_map.map) - 1 and self.structure_map.map[row + 1][col] == 2:
                        door_info['direction'] = 'V'

                        l = row
                        while l < len(self.structure_map.map) and self.structure_map.map[l][col] == 2:
                            door_info['size'] += 1
                            visited.add((l, col))
                            l += 1

                    doors_info.append(door_info)

        return doors_info


    def soft_reset_individuals(self):
        for individual in self.individuals:
            individual.row
            individual.col = 0
            individual.old_direction = -1
            individual.evacuated = False
            individual.steps = 0


    def simulation_reset(self, simulation_seed=0):
        self.simulation_seed = simulation_seed
        self.num_simulation += 1
        self.dinamic_map.reset_map()
        self.soft_reset_individuals()
        random.seed(self.simulation_seed)
        # As pessoas vao ficar todas nas saidas


    def scenario_reset(self, scenario_seed=0, simulation_seed=0):
        self.scenario_seed = scenario_seed
        self.simulation_seed = simulation_seed
        self.num_scenario += 1
        self.dinamic_map.reset_map()
        self.soft_reset_individuals()
        self.load_crowd_map()
        random.seed(self.simulation_seed)


    def map_reset(self, new_doors):
        self.structure_map.rewrite_doors(new_doors)
        self.load_wall_map()
        self.load_static_map()
        self.load_dinamic_map()
        if self.individuals:
            self.soft_reset_individuals()
        else:
            self.load_individuals()
        self.load_crowd_map()

