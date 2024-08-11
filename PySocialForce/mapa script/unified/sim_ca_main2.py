# -*- coding:utf-8 -*-

import argparse
import cProfile as profile
import pstats
import random
import os

from sim_ca_simulator import Simulator
from sim_ca_scenario import Scenario

parser = argparse.ArgumentParser(description='Simulator')
parser.add_argument('-e', action="store", dest='experiment', type=str, required=True, help="Experiment Folder.")
parser.add_argument('-d', action="store_const", dest='draw', const=True, default=False, help="Enable Draw Mode.")
parser.add_argument('-m', action="store", dest='scenario_seed', type=int, required=False, help="Seed to generate the scenario.")
parser.add_argument('-s', action="store", dest='simulation_seed', type=int, required=False, help="Seed to guide the simulation.")

if __name__ == "__main__":
    args = parser.parse_args()

    # p = profile.Profile()
    # p.enable()

    if args.scenario_seed:
        random.seed(args.scenario_seed)

    scen = Scenario(args.experiment, None, args.draw, 5, 12)
    # scen = Scenario("cult_experiment", None, True,5,12)
    simulator = Simulator(scen)
    iterations, qtdDistance = simulator.simulate()

    print("qtd iteracoes " + str(iterations))
    print("qtd distancia " + str(qtdDistance))
    # p.disable()
    # pstats.Stats(p).sort_stats('cumulative').print_stats(30)
