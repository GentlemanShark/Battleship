#! /usr/bin/python3


"""Main program for Battleship

   Author: Russ Lewis

   Creates a board.  Right now, the code hard-codes the board in one of two
   arrangements: a standard one, using 5 standard ship types, and a "tetris"
   one, where the board (kind of) looks like a Tetris game in progress.

   After creating the board, enters a while loop, which runs until
"""




from battleship     import *

from standard_ships import *
#from   tetris_ships import *



def main():

    # TODO: I'd like to make the who board-generation process more flexible,
    #       someday.   Right now, everything is hard-coded


    # Style hint: if you have an important variable which is not *currently*
    #             changing, but which you anticipate might change in the
    #             future, then do it in all caps to mark it as a "CONSTANT."
    #
    #             A constant *must never* change during a program run.
    #             However, it's quite reasonable (common even) for a
    #             programmer to change the constant - meaning that this
    #             error might go away.

    SIZE = 10
    player_A_board = Board(SIZE)



    # what type of board does the user want?

    type = input("Standard or Tetris board?   ").lower().strip()
    print()

    if type != "tetris":
        # NOTICE how I allcoate all of th ships and put them into an array,
        #        before I use them.  This is so it's easy to iterate over
        #        them later.

        player_A_ships = [Battleship(3),
                          Cruiser   (0),
                          Carrier   (0),
                          Submarine (0),
                          Destroyer (3) ]

        player_A_board.add_ship(player_A_ships[0], (1,5))
        player_A_board.add_ship(player_A_ships[1], (1,2))
        player_A_board.add_ship(player_A_ships[2], (4,5))
        player_A_board.add_ship(player_A_ships[3], (5,8))
        player_A_board.add_ship(player_A_ships[4], (9,2))

    else:
        player_A_ships = [Bar(0),
                          Tee(0),
                          R_ZigZag(0),
                          L_ZigZag(3),
                          L_Boot(0),
                          Tee(2),
                          Bar(2),
                          Tee(3),
                          Tee(1),
                          L_Boot(2),
                          R_Boot(2),
                          R_Boot(2),
                          Bar(3), ]

        player_A_board.add_ship(player_A_ships[ 0], (0,0))
        player_A_board.add_ship(player_A_ships[ 1], (2,1))
        player_A_board.add_ship(player_A_ships[ 2], (0,1))
        player_A_board.add_ship(player_A_ships[ 3], (2,5))
        player_A_board.add_ship(player_A_ships[ 4], (4,0))
        player_A_board.add_ship(player_A_ships[ 5], (6,1))
        player_A_board.add_ship(player_A_ships[ 6], (8,2))
        player_A_board.add_ship(player_A_ships[ 7], (5,4))
        player_A_board.add_ship(player_A_ships[ 8], (7,4))
        player_A_board.add_ship(player_A_ships[ 9], (6,6))
        player_A_board.add_ship(player_A_ships[10], (4,7))
        player_A_board.add_ship(player_A_ships[11], (3,8))
        player_A_board.add_ship(player_A_ships[12], (9,6))


    print("Welcome to Battleship!")
    print()
    print("This is the target side of the game")
    print()


    # ------------------ GAME LOOP -------------------------

    move_result = None
    while not all_sunk(player_A_ships):
        if move_result is not None:
            print()
            print()
            print()

        player_A_board.print()
        print()

        print("Ship list:")
        print("----------")
        for s in player_A_ships:
            s.print()
        print()

        if move_result is not None:
            print("RESULT: "+move_result)
            print()

        move = input("What is the next move? ")
        move = move.split()
        print()

        if len(move) != 2:
            print("Invalid move.  Move format must be: x y")
            input("  Press ENTER to continue")
            continue

        try:
            x = int(move[0])
            y = int(move[1])
        except:
            print("Invalid move.  Move format must be: x y")
            input("  Press ENTER to continue")
            continue

        if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
            print("Invalid move.  The range of valid moves is 0 through {} (inclusive)".format(SIZE))
            input("  Press ENTER to continue")
            continue

        if player_A_board.has_been_used((x,y)):
            print("Invalid move.  The location {},{} has already been used.".format(x,y))
            input("  Press ENTER to continue")
            continue

        # ****** THIS IS THE REASON WE'RE HERE! *****

        move_result = player_A_board.attempt_move((x,y))


    print()
    print()
    print()
    print(" *** GAME OVER ***")
    print()

    player_A_board.print()



def all_sunk(ships):
    for s in ships:
        if not s.is_sunk():
            return False
    return True



if __name__ == "__main__":
    main()

