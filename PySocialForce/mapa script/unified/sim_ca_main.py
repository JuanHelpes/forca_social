# -*- coding:utf-8 -*-

import argparse
import cProfile as profile
import json
import pstats
import random
import os

from sim_ca_crowd_map import CrowdMap
from sim_ca_individual import Individual
from sim_ca_dinamic_map import DinamicMap
from sim_ca_simulator import Simulator
from sim_ca_static_map import StaticMap
from sim_ca_structure_map import StructureMap
from sim_ca_wall_map import WallMap
from sim_ca_scenario import Scenario

parser = argparse.ArgumentParser(description='Simulator')
parser.add_argument('-e', action="store", dest='experiment', type=str, required=True, help="Experiment Folder.")
parser.add_argument('-d', action="store_const", dest='draw', const=True, default=False, help="Enable Draw Mode.")
parser.add_argument('-m', action="store", dest='scenario_seed', type=int, required=False, help="Seed to generate the scenario.")
parser.add_argument('-s', action="store", dest='simulation_seed', type=int, required=False, help="Seed to guide the simulation.")

if __name__ == "__main__":
    args = parser.parse_args()


    if args.scenario_seed:
        random.seed(args.scenario_seed)

    sep = os.path.sep
    root_path = r"D:\Faculdade\TCC\Codigo\TCC\PySocialForce\examples\mapa script\unified"

    structure_map = StructureMap(args.experiment, r'D:\Faculdade\TCC\Codigo\TCC\PySocialForce\mapa script\unified\igreja_comodos copy.map')
    # structure_map = StructureMap(args.experiment, r'D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_6\mapa_exemplo.txt')
    structure_map.load_map()
    structure_map.draw_map(root_path)  


    # static_map = StaticMap(args.experiment, structure_map)
    # static_map.load_map()
    # with open('static_mapa_exemplo.txt', r'w') as arq:
    #         arq.write(str(static_map.map))
    # if (args.draw):
    #     static_map.draw_map(root_path + "output")
  