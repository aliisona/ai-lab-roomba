# Lab 1, Part 2a: Heuristics.
# Name(s): Alisona Le, Vedic Patel
from search_heuristics import *
from slidepuzzle_problem import *

INF = float('inf')

#### Lab 1, Part 2a: Heuristics #################################################

# Implement these two heuristic functions for SlidePuzzleState.

""" Return the Hamming distance (number of tiles out of place) of the SlidePuzzleState """
def slidepuzzle_hamming(state : SlidePuzzleState)  -> float:
    goal = 0                                #is the goal value
    hamming = 0                             #number of tiles in the wrong place
    length = state.get_size()               #gets length of the puzzle

    for X in range(length):                 #goes through every row in the plane starting with the topmost one
        row = state.tiles[X]

        for Y in range (len(row)):          #goes through every column in the plan starting with the leftmost one
            col = row[Y]
            if(goal!=0):                    #is built in to accept the 0 first position at the top left corner
                if (goal != col):           #checks if the position matches the goal 
                    hamming += 1            #if the number present is not equal to the goal it adds a value to hamming signifying a tile in the wrong place
            goal += 1                       #Resets goal for next tile
    return hamming                          #returns final value of tiles in the wrong place

  
""" Return the sum of Manhattan distances between tiles and goal of the SlidePuzzleState """
def slidepuzzle_manhattan(state : SlidePuzzleState)  -> float:
    goal = 0                                #is the goal value                                                                    
    manhattan = 0                           #total distances to fix puzzle
    length = state.get_size()               #gets length of the puzzle

    for X in range(length):                 #goes through every row in the plane starting with the topmost one
        row = state.tiles[X]

        for Y in range (len(row)):          #goes through every column in the plan starting with the leftmost one
            col = row[Y]
            if(goal!=0):                    #is built in to accept the 0 first position at the top left corner
                if (goal != col):           #checks if the position matches the goal 
                    Goal_X_Pos = (int)(col % len(row))                  #calculates the intended goal x position
                    Goal_Y_Pos = (int)(col / len(row))                  #calculates the intended goal y position
                    X_Compensation = abs(Goal_X_Pos - X)                #calculates x error
                    Y_Compensation = abs(Goal_Y_Pos - Y)                #calculates y error
                    manhattan += (X_Compensation + Y_Compensation)      #adds total distance to move square to goal position
            goal += 1                       #resets goal for next tile
    return manhattan                        #returns final value of tiles in the wrong place

SLIDEPUZZLE_HEURISTICS = {
    "Zero" : zero_heuristic, 
    "Arbitrary": arbitrary_heuristic, 
    "Hamming" : slidepuzzle_hamming,
    "Manhattan" : slidepuzzle_manhattan
    }

