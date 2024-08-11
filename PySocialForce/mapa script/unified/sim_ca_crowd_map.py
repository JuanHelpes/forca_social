# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from random import randint
from os import mkdir
from os.path import isdir, sep

from sim_ca_constants import Constants

class CrowdMap(object):
    """Responsable to control the individual's location in the map.


    Attributes
    ----------
    label : str
        The name of the crowd map.

    structure_map : StructureMap
        The structure map contains information about the physical map.

    map : list of list of int
        The map with the individual's location.

    len_row : int
        The horizontal size of the map.

    len_col : int
        The vertical size of the map.

    Methods
    -------
    load_map(individuals)
        Based on the structure map the crowd map is started to be constructed.

    place_individuals(individuals)
        Based on the structure map the individuals are placed in the crowd map.

    draw_map(directory, iteration)
        Draw the crowd map using the individual's location.
        
    Authors
    -------
        Eduardo Miranda <eduardokira08@gmail.com>
        Luiz E. Pereira <luizedupereira000@gmail.com>
    """

    def __init__(self, label, structure_map):
        self.label = label
        self.structure_map = structure_map
        self.map = []
        self.len_row = structure_map.len_row
        self.len_col = structure_map.len_col

    def load_map(self, individuals):
        """Based on the structure map and individuals, the crowd map is constructed.

        Parameters
        ----------
        individuals : list of Individual
            Contains specific information about individuals.
        """
        self.map = []

        self.map = [[0] * self.len_col for _ in range(self.len_row)]
        self.place_individuals(individuals)

    def place_individuals(self, individuals):
        """Based on the structure map the individuals are placed in the crowd map.

        Parameters
        ----------
        individuals : list of Individual
            Contains specific information about individuals.
        """        
        empty_positions = self.structure_map.get_empty_positions()
        for individual in individuals:
            individual.row, individual.col = empty_positions.pop(randint(0, len(empty_positions) - 1))
            self.map[individual.row][individual.col] = individual

    def check_empty_position(self, row, col):
        """Check if a position in the map is empty

        Parameters
        ----------
        row : int
            Row index.
        col : int
            Column index.
            
        Returns
        -------
        boolean
            Returns True for empty position
        """
        if (self.map[row][col] == 0):
            return True
        return False

    def update_individual_position(self, original_row, original_col, new_row, new_col):
        """Update the position of an individual

        Parameters
        ----------
        original_row : int
            Row of the map that the individual was.
        original_col : int
            Column of the map that the individual was.
        new_row : int
            Row of the map that the individual will be.
        new_col : int
            Column of the map that the individual will be.
        """  
        self.map[new_row][new_col] = self.map[original_row][original_col]
        self.map[original_row][original_col] = 0

    def free_exit_gates(self):
        """Set all the positions in the map that are exits as 0
        """
        for exit in self.structure_map.exits:
            self.map[exit[0]][exit[1]] = 0

    def draw_map(self, directory, iteration):
        """Draw the crowd map using the structe map and the individuals colors.

        Parameters
        ----------
        directory : str
            Contain the directory that the image will be saved.

        iteration : int
            Number of the iteration.
        """

        if not isdir(directory):
            mkdir(directory)

        if not isdir(directory + "/crowd_map"):
            mkdir(directory + "/crowd_map")

        directory += "/crowd_map"

        field_size = 20
        image = Image.new("RGB", (field_size * self.len_col, field_size * self.len_row), Constants.C_WHITE)
        draw = ImageDraw.Draw(image)

        for i in range(self.len_row):
            for j in range(self.len_col):
                if (self.structure_map.map[i][j] == Constants.M_WALL):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_BLACK, Constants.C_BLACK)
                elif (self.structure_map.map[i][j] == Constants.M_OBJECT):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_GRAY, Constants.C_GRAY)
                elif (self.structure_map.map[i][j] == Constants.M_VOID):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_LIGHT_BLACK, Constants.C_LIGHT_BLACK)
                elif (self.structure_map.map[i][j] == Constants.M_EMPTY):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_WHITE, Constants.C_BLACK)             
                elif (self.structure_map.map[i][j] == Constants.M_DOOR):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_RED, Constants.C_BLACK)
                if (self.map[i][j] != 0): # If the field have an individual
                    if (self.structure_map.map[i][j] != Constants.M_DOOR):
                        draw.ellipse((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), self.map[i][j].color, Constants.C_BLACK) 
        
        # image_name = directory + str(iteration) + ".png"
        image_name = directory + sep + "crowd_map" + str(iteration) + ".png"
        # image_name = directory + "/" + self.label + "_crowd_map_" + str(iteration) + ".png"
        image.save(image_name)