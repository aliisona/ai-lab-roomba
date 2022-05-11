# Lab 1, Part 2c: Heuristics.
# Name(s): Vedic Patel, Alisona Le
 
#from tkinter import Y
#from numpy import Infinity
from search_heuristics import *
from spotlessroomba_problem import *
import math

# TODO If applicable, argue for why this is admissible / consistent!
def spotlessroomba_first_heuristic(state : SpotlessRoombaState)  -> float:

    if not state.dirty_locations:
        return 0
    
    best_start = 0

    for x in range(len(state.dirty_locations)):
        lowest_cost = INF
        closest_dirty = 0
        dirty_locations = list(state.dirty_locations)
        current_pos = dirty_locations.pop(x)

        while dirty_locations:
            for i in range(len(dirty_locations)):
            
                X_Current = current_pos.row
                Y_Current = current_pos.col
                X_Dirty = dirty_locations[i].row
                Y_Dirty = dirty_locations[i].col

                ham = ( ( ( (abs(X_Current - X_Dirty) )**2) + ( (abs(Y_Current - Y_Dirty) )**2) ) ) 
                hamming = math.sqrt(ham)

                if hamming < lowest_cost:
                    lowest_cost = hamming
                    closest_dirty = i

            current_pos = dirty_locations.pop(closest_dirty)
            lowest_cost = INF

        best_start = x

    current_pos = state.position

    x_Current = current_pos.row
    y_Current = current_pos.col
    x_Dirty = state.dirty_locations[best_start].row
    y_Dirty = state.dirty_locations[best_start].col

    dist_to_start = abs(x_Current - x_Dirty) + abs(y_Current - y_Dirty)

    return dist_to_start 


def spotlessroomba_second_heuristic(state : SpotlessRoombaState)  -> float:

    if not state.dirty_locations:
        return 0
    
    best_start = 0

    for x in range(len(state.dirty_locations)):
        lowest_cost = INF
        closest_dirty = 0
        dirty_locations = list(state.dirty_locations)
        current_pos = dirty_locations.pop(x)

        while dirty_locations:
            for i in range(len(dirty_locations)):
            
                X_Current = current_pos.row
                Y_Current = current_pos.col
                X_Dirty = dirty_locations[i].row
                Y_Dirty = dirty_locations[i].col

                manhattan = (abs(X_Current - X_Dirty) + abs(Y_Current - Y_Dirty))

                if manhattan < lowest_cost:
                    lowest_cost = manhattan
                    closest_dirty = i

            current_pos = dirty_locations.pop(closest_dirty)
            lowest_cost = INF

        best_start = x

    current_pos = state.position

    x_Current = current_pos.row
    y_Current = current_pos.col
    x_Dirty = state.dirty_locations[best_start].row
    y_Dirty = state.dirty_locations[best_start].col

    dist_to_start = abs(x_Current - x_Dirty) + abs(y_Current - y_Dirty)

    return dist_to_start 


# TODO Update heuristic names and functions below. If you make more than two, add them here.
SPOTLESSROOMBA_HEURISTICS = {"Zero" : zero_heuristic,
                        "Arbitrary": arbitrary_heuristic, 
                        "Custom Heur. 1": spotlessroomba_first_heuristic,
                        "Custom Heur. 2" : spotlessroomba_second_heuristic
                        }
