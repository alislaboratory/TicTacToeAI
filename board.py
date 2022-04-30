# TIC-TAC-TOE CLI AND AI
# WRITTEN BY ANONYMOIST


# Here, we create a class that stores the data of the board. This allows us to make multiple instances of a board if needed,
# and acts as a new datatype.

# Alternating turns and other game logic is handled outside of the Board class. The class only
# handles the board itself and its methods, such as checking if the game was won, updating the board, etc.
class Board:

    # Initialise the board with empty positions when an instance is created.
    def __init__(self):
        self.board = [[None, None, None], # Create a 2-dimensional array in which the positions are stored.
                      [None, None, None],
                      [None, None, None]]

    # This method of the Board class takes in a position, and returns the current player in that position
    # "X", "O" or NoneType
    def who(self, position):
        return self.board[position[1] - 1][position[0] - 1]

    # Private function to return True if the game is finished
    def __is_finished(self):
        count = 0
        finished = None
        for row in self.board: # Check if each row contains 3 Xs or Os
            if row[0] != None and row[1] != None and row[2] != None:
                count += 1

        if count == 3: # If all 3 rows didn't contain NoneTypes, then the game is finished
            finished = True
        else: # If there was a NoneType, return False because the game is not finished
            finished = False

        return finished

        # This function returns the winner of the game. Also checks if the game has finished before checking winner for redundancy.
        # Uses a custom-made algorithm to find diagonals/horizontals/verticals of
    def __winner(self, won = "X"):  # We use double underscore (__) in front of the method name to make it private and only accessible from inside the class's other methods. It couldn't be accessed from outside the class and acts as a convenience function (aren't all functions for convenience).

        # Logic: Loop through elements in the first row and first column. For each element in the first row, for example, find where it
        # can follow the rules for 3 straight positions. Then check each position for its respective first element (X, O) with a counter.
        # If the counter = 3, you have your line and the player of that counter wins.
        return won



    # This function takes the current player ("X" or "O"), and the position [x, y] starting at 1 for the first element
    # Also checks for winners before and after turns,
    def turn(self, player, position): # Holy shit, there is definitely a better way to do this logic, but I'm lazy, and it works. nvm i fixed it
        if self.__is_finished() == False:
            self.board[position[1] - 1][position[0] - 1] = player
        return self.__winner()
