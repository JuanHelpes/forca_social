class Constants(object):

    def __init__(self):
        pass
    
    # Object Map Constant
    M_EMPTY = 0
    M_WALL = 1
    M_DOOR = 2
    M_OBJECT = 3
    M_VOID = 4
    
    # Static Field Constant
    S_WALL = 9999

    # Directions Constant
    D_TOP = (-1, 0, 1)
    D_TOP_RIGHT = (-1, 1, 1.5)
    D_RIGHT = (0, 1, 1)
    D_BOTTOM_RIGHT = (1, 1, 1.5)
    D_BOTTOM = (1, 0, 1)
    D_BOTTOM_LEFT = (1, -1, 1.5)
    D_LEFT = (0, -1, 1)
    D_TOP_LEFT = (-1, -1, 1.5)

    # Map Colors
    C_WHITE = (255, 255, 255)
    C_BLACK = (0, 0, 0)
    C_GRAY = (75, 75, 75)
    C_LIGHT_BLACK = (35, 35, 35)
    C_RED = (255, 0, 0)

    # Difusion and Decay Constant
    DIFUSIONDECAY_ALFA = 0.05
    DIFUSIONDECAY_SIGMA = 0.7

    # Constant to multiply the index of distance from the individuals to the closest door
    DISTANCE_MULTIPLIER = 0.25