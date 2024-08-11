
from copy import deepcopy
from math import exp 
from PIL import Image
from PIL import ImageDraw
from os import mkdir
from os.path import isdir 

from sim_ca_constants import Constants


class DinamicMap(object):
    """Responsable to control the individual's tracing in the map.


    Attributes
    ----------
    label : str
        The name of the dinamic map.

    structure_map : StructureMap
        The structure map contains information about the physical map.

    map : list of list of int *******************************************************************************************
        The map with the individual's location.*************************************************************

    len_row : int
        The horizontal size of the map.

    len_col : int
        The vertical size of the map.

    Methods
    -------
    
        
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

    
    def load_map(self):
        for i in range(self.len_row):
            self.map.append([])
            for _ in range(self.len_col):
                self.map[i].append(0)

    def draw_map(self, directory, iteration):
        """Draw the crowd map using the structe map and the individuals colors.

        Parameters
        ----------
        directory : str
            Contain the directory that the image will be saved.

        iteration : int
            Number of the iteration.
        """
        if not isdir(directory + "/dinamic_map"):
            mkdir(directory + "/dinamic_map")

        directory += "/dinamic_map"

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
                elif (self.structure_map.map[i][j] == Constants.M_DOOR):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_RED, Constants.C_BLACK)
                else:
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), (255, 255 - 20 * int(self.map[i][j]), 255), Constants.C_BLACK)
        
        #image_name = directory + "/" + self.label + "_dinamic_map_" + str(iteration) + ".png"
        image_name = directory + "/" + "dinamic_map_" + str(iteration) + ".png"
        image.save(image_name)


    def difusion_decay(self):
        aux_map = deepcopy(self.map)
        for i in range(1, len(self.map) - 1):
            for j in range(1, len(self.map[i]) - 1):
                self.map[i][j] = aux_map[i][j] + Constants.DIFUSIONDECAY_ALFA * (aux_map[i+1][j] + aux_map[i-1][j] + aux_map[i][j+1] + aux_map[i][j-1] + 
                                                                                aux_map[i-1][j-1] + aux_map[i-1][j+1] + aux_map[i+1][j-1] + aux_map[i+1][j+1])
        for i in range(1, len(self.map) - 1):
            for j in range(1, len(self.map[i]) - 1):
                self.map[i][j] = self.map[i][j]  * Constants.DIFUSIONDECAY_SIGMA


    def calc_dinamic_value(self, row, col, individual_KW):
        return exp(individual_KW * self.map[row][col])


    def reset_map(self):
        for i in range(self.len_row):
            for j in range(self.len_col):
                self.map[i][j] = 0