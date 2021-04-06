"""Standard ship types for the Battleship game.

   Author: Russ Lewis

   Defines a function for each of the well-known ship types in Battleship;
   the function creates a new Ship object every time that it is called.
   The code in this module builds a standard shape, which always includes
   the point (0,0); the caller passes these functions a 'rot' field, which
   is used to rotate the shape before we pass it to the Ship constructor.

   Primary functions:
      Carrier   (rot)
      Battleship(rot)
      Cruiser   (rot)
      Submarine (rot)
      Destroyer (rot)

   Utility functions:
      rotate_shape(shape,rot)
"""



from battleship import Ship



def Carrier(rot):
    retval = Ship("Aircraft Carrier", [(0,0), (1,0), (2,0), (3,0), (4,0)] )
    retval.rotate(rot)
    return retval

def Battleship(rot):
    retval = Ship("Battleship", [(0,0), (1,0), (2,0), (3,0)] )
    retval.rotate(rot)
    return retval

def Cruiser(rot):
    retval = Ship("Cruiser", [(0,0), (1,0), (2,0)] )
    retval.rotate(rot)
    return retval

def Submarine(rot):
    retval = Ship("Submarine", [(0,0), (1,0), (2,0)] )
    retval.rotate(rot)
    return retval

def Destroyer(rot):
    retval = Ship("Destroyer", [(0,0), (1,0)] )
    retval.rotate(rot)
    return retval


