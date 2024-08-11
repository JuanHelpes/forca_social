# -*- coding:utf-8 -*-

from sim_ca_logs import Logs

class Simulator(object):

    MAX_ITERATIONS = 200

    # def __init__(self, structure_map, wall_map, static_map, crowd_map, dinamic_map, individuals, directory):

    #     self.structure_map = structure_map
    #     self.wall_map = wall_map
    #     self.static_map = static_map
    #     self.crowd_map = crowd_map
    #     self.dinamic_map = dinamic_map
    #     self.individuals = individuals
    #     self.directory = directory # *********************************************
    #     self.iteration = 0
    #     self.log = Logs.Logs()
    
    def __init__(self, scenario):
        self.structure_map = scenario.structure_map
        self.wall_map = scenario.wall_map
        self.static_map = scenario.static_map
        self.crowd_map = scenario.crowd_map
        self.dinamic_map = scenario.dinamic_map
        self.individuals = scenario.individuals
        self.directory = scenario.root_path
        self.draw_path = scenario.draw_path
        self.draw = scenario.draw
        self.iteration = 0
        self.log = Logs()

    def simulate(self):
        while (not self.check_evacuated_individuals() and self.iteration < self.MAX_ITERATIONS):
            #self.crowd_map.draw_map("../output/" + self.directory, self.individuals, self.iteration)
            if self.draw:
                # print(self.iteration)
                self.crowd_map.draw_map(self.draw_path, self.iteration)
                self.dinamic_map.draw_map(self.draw_path, self.iteration)
            self.iteration += 1

            self.sort_individuals_by_distance()

            for individual in self.individuals:
                # Increment the amount of steps for the individual to move based in individual's speed
                individual.steps += 1 
                if (not individual.evacuated):
                    if (individual.steps == individual.speed):

                        direction = individual.move(self.structure_map, self.wall_map, self.static_map, self.crowd_map, self.dinamic_map)
                        # Increase the dinamic map if someone move to the direction
                        if direction:
                            self.dinamic_map.map[direction['row']][direction['col']] += 1

                        if(self.structure_map.isSaida(individual.row, individual.col)):
                            individual.evacuated = True

                        individual.steps = 0

            # After moving all the individuals free the exit gates that are occupied
            self.crowd_map.free_exit_gates()

            # After the iteration it's recalculed the pheromone map
            self.dinamic_map.difusion_decay()

            # Save people
            self.log.saveIterationDistances(self.individuals, self.static_map)

        if self.draw:
            self.log.generateHTML(self.draw_path, self.iteration, len(self.individuals), 1)

        return self.iteration, self.log.calculateDistances()

    
    # Pode ser melhorado, remover o individuo da lista ganha em processamento ***********************************
    def check_evacuated_individuals(self):
        for i in range(len(self.individuals)):
            if (not self.individuals[i].evacuated):
                return False
        return True
        
    def sort_individuals_by_distance(self):
        #a ordenacao eh util para que os movimentos dos individuos sejam feitas pelas distancias mais proximas
        self.individuals.sort(key = self.individual_exit_distance, reverse = False)

    def individual_exit_distance(self, individual):
        # retorna distancia da porta
        return self.static_map.map[individual.row][individual.col]

