'''
File: battleship.py
Author: Stuart Trappe
Course: CSC 120
Purpose: A one-sided, command line based version of the board game battleship.
         It allows differently sized ships to be moved around and placed on a
         game board and for attempts to sink the ship to be made. The game
         displays the game board with icons for ocean, ships, hits, and misses
         as well as a display of the ships.
'''

class Board():
    '''
    This class represents the overall game board which is represented with a 2D
    array of game tiles. Each tile is either an ocean piece or a ship piece.
    It handles adding ships to the board and making moves while also handling
    initalizing an empty array and printing out a graphic representation.
    '''
    def __init__(self, size):
        # Initalizes board with the size and a blank array
        assert size > 0
        self.size = size
        self.board_array = []  # To be used for a 2D array
        for row in range(0, size):  # This is the y (i.e. 0 is first row)
            temp_row = []
            for tile_pos in range(0, size):  # Specific tile (e.g. (0,0))
                temp_row.append(Tile((tile_pos, row)))
            self.board_array.append(temp_row)  # Add row of tiles to the array

    def check_tiles(self, tiles):
        # Sees if the tiles to be placed are within bounds of the board
        for tile in tiles:
            position = tile.get_position()
            assert position[0] >= 0 and position[0] < self.size
            assert position[1] >= 0 and position[1] < self.size
            assert not self.board_array[position[1]][position[0]].is_ship()

    def add_ship(self, ship, position):
        # Adds a ship to the board given a position
        tiles = ship.create_tiles(position)
        self.check_tiles(tiles)  # Check if ship is out of bounds
        for tile in tiles:
            position = tile.get_position()  # Used for x and y coords
            self.board_array[position[1]][position[0]] = tile

    def print(self):
        # Prints out the board in ASCII output
        row_num = len(self.board_array) - 1
        if row_num < 10:  # Single digits
            print('  +' + '-' * (len(self.board_array) * 2 + 1) + '+')
            while row_num >= 0:
                print(str(row_num) + ' | ', end='')  # Prints y axis numbers
                tile_counter = 0
                for tile in self.board_array[row_num]:
                    print(tile.get_name() + ' ', end='')  # Spaces between
                    tile_counter += 1
                print('|')
                row_num -= 1  # Move down a row
            print('  +' + '-' * (len(self.board_array) * 2 + 1) + '+')
            print('    ', end='')
            for col_num in range(0, len(self.board_array)):
                print(str(col_num) + ' ', end='')  # Prints x axis numbers
            print('')
        else:  # Double digits
            print('   +' + '-' * (len(self.board_array) * 2 + 1) + '+')
            for row in self.board_array:
                tile_counter = 0
                if row_num > 9:
                    print(str(row_num) + ' | ', end='')
                    for tile in row:
                        print(tile.get_name() + ' ', end='')
                        tile_counter += 1
                    print('|')
                else:
                    print(' ' + str(row_num) + ' | ', end='')
                    for tile in row:
                        print(tile.get_name() + ' ', end='')
                        tile_counter += 1
                    print('|')
                row_num -= 1
            print('   +' + '-' * (len(self.board_array) * 2 + 1) + '+')
            print('                         ', end='')
            for col_num in range(10, len(self.board_array)):
                num = str(col_num)
                print(num[:1] + ' ', end='')
            print('\n' + '     ', end='')
            for col_num in range(0, len(self.board_array)):
                if col_num > 9:
                    num = str(col_num)
                    print(num[1:] + ' ', end='')
                else:
                    print(str(col_num) + ' ', end='')
            print('')

    def has_been_used(self, position):
        # Determines if a tile has been hit
        x = position[0]
        y = position[1]
        assert position[0] >= 0 and position[0] < self.size
        assert position[1] >= 0 and position[1] < self.size
        return self.board_array[y][x].was_hit()

    def attempt_move(self, position):
        x = position[0]  # Used for row and col
        y = position[1]
        tile = self.board_array[y][x]
        assert x < self.size and x >= 0  # Within bounds
        assert y < self.size and y >= 0
        '''
        Simpler to use tile.was_hit() directly, but used has_been_used()
        to ensure test case coverage and if the provided main method
        ever needs to use it.
        '''
        assert not self.has_been_used((x, y))
        tile.take_hit()
        if tile.is_ship():
            if tile.ship.is_sunk():
                return('Sunk (' + tile.ship_name() + ')')
            else:
                return('Hit')
        else:  # Ocean tile
            return('Miss')


class Ship():
    '''
    This class represents a ship object. It handles creating the tiles for each
    ship component, rotating the ship, and maintaing aspects like which tiles
    have been hit, if the ship is sunk, and several setters and getters.
    '''
    def __init__(self, name, shape):
        # Initalizes ship with its name, coordinates, and empty tile array
        self.name = name  # Name of ship (e.g. Destroyer)
        self.coords = shape  # Each point that forms the shape of the ship
        self.tiles = []

    def print(self):
        # Prints out ship status and name (e.g. SSS Submarine)
        output_string = ''  # What will be printed
        for tile in self.tiles:
            output_string += tile.get_name()  # Adds each tile character
        if 'X' in output_string:  # Case for if ship is sunk
            output_string = '*' * len(output_string)
        print('%-10s' % output_string + self.name)  # Fits 10 spaces

    def is_sunk(self):
        # Returns if ship is sunk
        for tile in self.tiles:
            if not tile.was_hit():
                return False
        return True

    def create_tiles(self, position):
        # Generates tiles for each ship component
        self.tiles = []
        for coord in self.coords:
            tile_position = (position[0] + coord[0], position[1] + coord[1])
            tile = Tile(tile_position, self)
            self.tiles.append(tile)
        return self.tiles

    def rotate(self, amount):
        # Rotates the ship 90 degrees clockwise
        assert amount < 4  # Makes sure amount is less than 4
        for counter in range(amount):
            for i in range(len(self.coords)):
                self.coords[i] = (self.coords[i][1], (self.coords[i][0] * -1))

    def get_name(self):
        return self.name


class Tile():
    '''
    This class represents a game tile that is contained in Board. It is
    used for both ocean and ship tiles. It retains information about its
    position, whether it has been hit, and what character to display.
    '''
    def __init__(self, position, ship = None):
        # Initalizes tile with ship its owned by, position, and being unhit
        self.ship = ship  # Default to known if ocean tile
        self.position = position
        self.been_hit = False

    def was_hit(self):
        # Each tile knows if has been hit or not
        return self.been_hit

    def get_name(self):
        if self.ship == None:  # Ocean tiles
            if self.been_hit:
                return 'o'
            else:
                return '.'
        else:  # Ship tiles
            if self.ship.is_sunk():
                return 'X'
            elif self.been_hit:
                return '*'
            else:
                name = self.ship.get_name()
                return name[0]

    def get_position(self):
        return self.position

    def take_hit(self):
        self.been_hit = True

    def is_ship(self):
        return self.ship != None

    def ship_name(self):
        return self.ship.get_name()