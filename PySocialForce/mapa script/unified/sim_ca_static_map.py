# -*- coding:utf-8 -*-

from colour import Color
from copy import deepcopy
from math import exp
from pathlib import Path
from PIL import Image
from PIL import ImageDraw
import re

from sim_ca_constants import Constants

class StaticMap(object):
    """Responsable to calc the distance from the exit doors for each field in the map.


    Attributes
    ----------
    label : str
        The name of the static map.

    structure_map : StructureMap
        The structure map contains information about the physical map.

    map : list of list of int
        The map with values of static fields.

    len_row : int
        The horizontal size of the map.

    len_col : int
        The vertical size of the map.

    Methods
    -------
    load_map()
        Based on the structure map the static map is started to be constructed.

    calc_static_field(exit_gates)
        After the static map be pre constructed the real values are calculed using a recursion principle based in FIFO lists.

    is_expansible(field)
        Return if one field is going to be expanded or not based on location and value.

    field_exist(field)
        Check if the position of the field is in the map range.

    calc_static_value(row, col, individual_KS)
        Calculate the static value of a field based in an individual.

    draw_map(directory)
        Draw the static map using a range of colors from red to blue.

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
        """Based on the structure map the static map is started to be constructed.
        """
        self.map = []
        exit_gates = []

        for i in range(self.len_row):
            static_map_row = []
            for j in range(self.len_col):
                if (self.structure_map.map[i][j] == Constants.M_DOOR): # If it is a DOOR
                    exit_gates.append([i, j, 1])
                    static_map_row.append(1)
                elif (self.structure_map.map[i][j] == Constants.M_WALL or self.structure_map.map[i][j] == Constants.M_OBJECT or self.structure_map.map[i][j] == Constants.M_VOID): # If it is a WALL, OBJECT or VOID
                    static_map_row.append(Constants.S_WALL)
                elif (self.structure_map.map[i][j] == Constants.M_EMPTY):
                    static_map_row.append(Constants.M_EMPTY)
            self.map.append(static_map_row)

        self.calc_static_field(deepcopy(exit_gates))

    def calc_static_field(self, exit_gates):
        """After the static map be pre constructed the real values are calculed using 
        a recursion principle based in FIFO lists.

        Parameters
        ----------
        exit_gates : list of list of int
            Contains the location of each door placed in map.
        """
        fifo_list = exit_gates
        for field in exit_gates:
            self.map[field[0]][field[1]] = field[2]
        while fifo_list:
            field = fifo_list.pop(0)  

            for direction in ([Constants.D_TOP, Constants.D_TOP_RIGHT, Constants.D_RIGHT, Constants.D_BOTTOM_RIGHT, Constants.D_BOTTOM, Constants.D_BOTTOM_LEFT, Constants.D_LEFT, Constants.D_TOP_LEFT]):
                new_field = (field[0] + direction[0], field[1] + direction[1], field[2] + direction[2])
                if (self.is_expansible(new_field)):
                    fifo_list.append(new_field)
                    self.map[new_field[0]][new_field[1]] = new_field[2]
        
    def is_expansible(self, field):
        """Return if one field is going to be expanded or not based on location and value.

        Parameters
        ----------
        fields : list of int
            Contain the information of one field of the map (locationX, locationY, value).
            
        Returns
        -------
        bool
            True if the field is going to be expanded, False otherwise.
        """
        if (not self.field_exist(field)):
            return False
        if (self.map[field[0]][field[1]] == Constants.S_WALL):
            return False
        if (self.map[field[0]][field[1]] <= field[2] and self.map[field[0]][field[1]] != 0):
            return False
        return True

    def field_exist(self, field):
        """Check if the position of the field is in the map range.

        Parameters
        ----------
        fields : list of int
            Contain the information of one field of the map (locationX, locationY, value).
        
        Returns
        -------
        bool
            True if the field location is in range of the map, False otherwise.
        """
        if (field[0] < 0 or field[0] >= self.len_row):
            return False
        if (field[1] < 0 or field[1] >= self.len_col):
            return False
        return True

    def calc_static_value(self, row, col, individual_KS):
        """Calculate the static value of a field based in an individual.

        Parameters
        ----------
        row : int
            The row of the field that is going to be calculated the static value.
        col : int
            The col of the field that is going to be calculated the static value.
        individual_KS: float
            The static map constant of an individual.
        Returns
        -------
        float
            Returns the value based in the individual_KS and the new location.
        """
        return exp(individual_KS * -self.map[row][col])

    def draw_map(self, directory):
        """Draw the static map using a range of colors from red to blue.

        Parameters
        ----------
        directory : str
            Contain the directory that the image will be saved
        """
        field_size = 20
        image = Image.new("RGB", (field_size * self.len_col, field_size * self.len_row), Constants.C_WHITE)
        draw = ImageDraw.Draw(image)

        greater_value = 0
        for i in range(self.len_row):
            for j in range(self.len_col):
                if (self.map[i][j] != Constants.S_WALL and self.map[i][j] > greater_value):
                    greater_value = self.map[i][j]
        colors = list(Color("red").range_to(Color("blue"), (int(greater_value) + 1)))

        for i in range(self.len_row):
            for j in range(self.len_col):
                if (self.structure_map.map[i][j] == Constants.M_OBJECT):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_GRAY, Constants.C_GRAY)
                elif (self.structure_map.map[i][j] == Constants.M_VOID):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_LIGHT_BLACK, Constants.C_LIGHT_BLACK)
                elif (self.structure_map.map[i][j] == Constants.M_WALL or self.map[i][j] == Constants.S_WALL):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_BLACK, Constants.C_BLACK)
                elif (self.structure_map.map[i][j] == Constants.M_DOOR):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_RED, Constants.C_BLACK)
                else: # Draw or empty case
                    color = str(colors[int(self.map[i][j])].hex)
                    color = re.sub('[#]', '', color)
                    if (color.__len__() == 3):
                        color = color[0] + color[0] + color[1] + color[1] + color[2] + color[2]
                    color = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
                    if color == (255,0,0):
                        color = (0,0,255)
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), color, Constants.C_BLACK)
        Path(directory).mkdir(parents=True, exist_ok=True)
        image_name = directory + "/" + self.label + "_static-field.png"
        image.save(image_name)