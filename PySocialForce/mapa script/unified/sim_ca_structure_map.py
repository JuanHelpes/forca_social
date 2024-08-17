# -*- coding:utf-8 -*-

from colour import Color
from PIL import Image
from PIL import ImageDraw
from pathlib import Path

from sim_ca_constants import Constants

class StructureMap(object):
    """Responsable to store the map fisical informations: doors, walls, etc.

    ...

    Attributes
    ----------
    label : str
        The name of the static map.
        
    map : list of list of int
        The map with values of static fields.

    len_row : int
        The horizontal size of the map.

    len_col : int
        The vertical size of the map.

    path : str
        Directory path which contains the map file.

    Methods
    -------
    load_map()
        Read the map file to construct the structure map.

    get_empty_positions()
        Returns a list which contains the empty positions of the structure map.
    
    Authors
    -------
        Eduardo Miranda <eduardokira08@gmail.com>
        Luiz E. Pereira <luizedupereira000@gmail.com>
    """

    def __init__(self, label, path):
        self.label = label
        self.path = path
        self.map = []
        self.len_row = 0
        self.len_col = 0
        self.exits = []

    def load_map(self):
        """Read the map file to construct the structure map.
        """
        file = open(self.path, 'r')
        for line in file:
            line = line.strip('\n')
            self.map.append([])
            for col in line:
                self.map[self.len_row].append(int(col))
            self.len_row += 1
        file.close()
        self.len_col = len(self.map[0])

        self.exits = self.get_exits()


    def get_empty_positions(self):
        """Returns a list which contains the empty positions of the structure map.

        Returns
        -------
        list of tuple
            List that contains the empty positions of the structure map.
        """
        empty_positions = []
        for i in range(self.len_row):
            for j in range(self.len_col):
                if (self.map[i][j] == Constants.M_EMPTY):
                    empty_positions.append((i, j))
        return empty_positions

    def isSaida(self, row, col):
        """Returns if the position is an exit or not.

        Returns
        -------
        logical
            Return if the structure map in the position i,j is an exit
        """
        return self.map[row][col] == Constants.M_DOOR 

    def get_exits(self):
        """Returns a list which contains the exits of the structure map.

        Returns
        -------
        list of tuple
            List that contains the exits of the structure map.
        """
        exits = []
        for i in range(self.len_row):
            for j in range(self.len_col):
                if (self.map[i][j] == Constants.M_DOOR):
                    exits.append((i, j))
        return exits

    def rewrite_doors(self, new_doors):
        for exit in self.exits:
            self.map[exit[0]][exit[1]] = Constants.M_WALL
        
        for new_door in new_doors:
            if new_door['direction'] == 'V':
                for i in range(0, new_door['size']):
                    self.map[new_door['row'] + i][new_door['col']] = Constants.M_DOOR
            else:
                for i in range(0, new_door['size']): 
                    self.map[new_door['row']][new_door['col'] + i] = Constants.M_DOOR         

        self.exits = self.get_exits()


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
                elif (self.structure_map.map[i][j] == Constants.M_COMODO):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_GRAY, Constants.C_GRAY)
                elif (self.structure_map.map[i][j] == Constants.M_SAIDACOMODO):
                    draw.rectangle((j * field_size, i * field_size, (j + 1) * field_size, (i + 1) * field_size), Constants.C_RED, Constants.C_BLACK)
                # Novas cores para as constantes novas
                # Ajustar caminhos para salvar e buscar os mapas

        Path(directory).mkdir(parents=True, exist_ok=True)
        image_name = directory + "/" + self.label + "_mapa_comodo.png"
        image.save(image_name)