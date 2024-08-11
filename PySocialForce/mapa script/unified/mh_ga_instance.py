
import json
import os

class Instance:

    def __init__(self, experiment, draw, scenario_seed, simulation_seed):
        self.experiment = experiment
        self.draw = draw
        self.scenario_seed = scenario_seed
        self.simulation_seed = simulation_seed


def read_instance(experiment):
    data = None
    sep = os.path.sep
    root_path = os.path.dirname(os.path.dirname(os.path.abspath("simulator"))) + sep        
    input_file = root_path + "input" + sep + experiment + sep + "experiment.json"
    with open(input_file, 'r') as f:
        data = json.load(f)

    return Instance(data["experiment"], data["draw"], data["scenario_seed"], data["simulation_seed"])

