# Lab 1, Part 2c: Heuristics.
# Name(s): Vedic Patel, Alisona Le
 
from search_heuristics import *
from spotlessroomba_problem import *
import math

# TODO If applicable, argue for why this is admissible / consistent!
def spotlessroomba_first_heuristic(state : SpotlessRoombaState)  -> float:
#This heuristic is admissible because it will always give an optimistic answer. 
#It takes the hamming value meaning the shortest possible path if there were no walls to block your path
#It is not very consistent because there are many times that there are walls in the way
#and because it is impossible to go diagonal the hamming value will always be to optimistic and not on point


    if not state.dirty_locations:                               #Checks to make sure that the original position is not a dirty location
        return 0                                                #Give a heuristic of 0 if you start on a dirty square
    
    best_start = 0                                              #Sets up a variable responsible for choosing the best dirty square to start from

    length = len(state.dirty_locations)                         #sets variable length to number of dirty locations

    for x in range(length):                                     #Set a loop to go through all dirty locations
        lowest_cost = INF                                       #Sets lowest cost to Infinity so any real cost is less then it
        closest_dirty = 0                                       #Sets up the closest dirty variable
        dirty_locations = list(state.dirty_locations)           #Creates a list of all dirty locations
        current_pos = dirty_locations.pop(x)                    #Assigns current_pos to the last value of dirty_locations

        while dirty_locations:                                  #Creates a for loop that is active while there are dirty squares
            for i in range(len(dirty_locations)):               #Goes through each coord in the dirty location list
            
                X_Current = current_pos.row                     #assigns x current to the current_pos row value
                Y_Current = current_pos.col                     #assings y current to the current_pos column value
                X_Dirty = dirty_locations[i].row                #assigns x dirty to the dirty location being evaluated row value
                Y_Dirty = dirty_locations[i].col                #assigns y dirty to the dirty locations being evaluated column value

                ham = ( ( ( (abs(X_Current - X_Dirty) )**2) + ( (abs(Y_Current - Y_Dirty) )**2) ) ) 
                hamming = math.sqrt(ham)                        #Finds hypotenuse value between the current and dirty square

                if hamming < lowest_cost:                       #If this value is lower then the lowest value
                    lowest_cost = hamming                       #Turn this hamming value into the new lowest cost value
                    closest_dirty = i                           #Set the closest dirty the the lowest hamming value dirty square

            current_pos = dirty_locations.pop(closest_dirty)    #assign the current pos to the closest dirty 
            lowest_cost = INF                                   #reset lowest cost

        best_start = x                                          #sets the best start to the x value evaluated

    current_pos = state.position                                #resets current_pos

    x_Current = current_pos.row                                 #assigns x current to the current_pos row value
    y_Current = current_pos.col                                 #assings y current to the current_pos column value
    x_Dirty = state.dirty_locations[best_start].row             #assigns x dirty to the best dirty location row value
    y_Dirty = state.dirty_locations[best_start].col             #assigns y dirty to the best dirty locations column value
                
    ham_dist = ( ( ( (abs(x_Current - x_Dirty) )**2) + ( (abs(y_Current - y_Dirty) )**2) ) ) 
    dist_to_start = math.sqrt(ham_dist)                         #Finds hypotenuse value between the current and dirty square

    return dist_to_start                                        #returns final value


def spotlessroomba_second_heuristic(state : SpotlessRoombaState)  -> float:
#This heuristic is admissible because it will always give an optimistic answer. 
#It takes the manhattan value meaning the shortest possible path while following the square pattern
#and if there were no walls to block your path
#It is not very consistent because there are many times that there are walls in the way

    if not state.dirty_locations:                               #Checks to make sure that the original position is not a dirty location
        return 0                                                #Give a heuristic of 0 if you start on a dirty square
    
    best_start = 0                                              #Sets up a variable responsible for choosing the best dirty square to start from

    length = len(state.dirty_locations)                         #sets variable length to number of dirty locations

    for x in range(length):                                     #Set a loop to go through all dirty locations
        lowest_cost = INF                                       #Sets lowest cost to Infinity so any real cost is less then it
        closest_dirty = 0                                       #Sets up the closest dirty variable
        dirty_locations = list(state.dirty_locations)           #Creates a list of all dirty locations
        current_pos = dirty_locations.pop(x)                    #Assigns current_pos to the last value of dirty_locations

        while dirty_locations:                                  #Creates a for loop that is active while there are dirty squares
            for i in range(len(dirty_locations)):               #Goes through each coord in the dirty location list
            
                X_Current = current_pos.row                     #assigns x current to the current_pos row value
                Y_Current = current_pos.col                     #assings y current to the current_pos column value
                X_Dirty = dirty_locations[i].row                #assigns x dirty to the dirty location being evaluated row value
                Y_Dirty = dirty_locations[i].col                #assigns y dirty to the dirty locations being evaluated column value

                manhattan = (abs(X_Current - X_Dirty) + abs(Y_Current - Y_Dirty))   #finds distance from start to evaluated dirty square

                if manhattan < lowest_cost:                     #If this value is lower then the lowest value
                    lowest_cost = manhattan                     #Turn this manhattan value into the new lowest cost value
                    closest_dirty = i                           #Set the closest dirty the the lowest hamming value dirty square

            current_pos = dirty_locations.pop(closest_dirty)    #assign the current pos to the closest dirty 
            lowest_cost = INF                                   #reset lowest cost

        best_start = x                                          #sets the best start to the x value evaluated

    current_pos = state.position                                #resets current_pos

    x_Current = current_pos.row                                 #assigns x current to the current_pos row value
    y_Current = current_pos.col                                 #assings y current to the current_pos column value
    x_Dirty = state.dirty_locations[best_start].row             #assigns x dirty to the best dirty location row value
    y_Dirty = state.dirty_locations[best_start].col             #assigns y dirty to the best dirty locations column value

    dist_to_start = abs(x_Current - x_Dirty) + abs(y_Current - y_Dirty)     #finds distance from start to best start dirty square

    return dist_to_start 

def spotlessroomba_third_heuristic(state : SpotlessRoombaState)  -> float:
    #go to closest dirty location using manhattan dist, then find the next closest dirty location (also using manhat dist)
    #loops for every dirty
    #this one is the most efficient (yay!!!) ++ super optimistic (goals) too cause it completely ignores walls and carpet
    #this is total manhat dist AS long as its the closest tile each time (which it should be ;)!)  

    h = 0 #heuristic

    for x in range(len(state.dirty_locations)): #define 
        lowest_cost = INF #any cost would literally be better than this lol                                      
        closest_dirty = 0                                       
        dirty_locations = list(state.dirty_locations)          
        current_pos = dirty_locations.pop(x) 

        while dirty_locations: #while dirty locations still exist >:(((
            for i in range(len(dirty_locations)): #keep doing this for all of da dirty spots!!
                manhattan = (abs(current_pos.row - dirty_locations[i].row) + abs(current_pos.col - dirty_locations[i].col))   #finds distance from start to evaluated dirty square
                if manhattan < lowest_cost: #rewrite the lowest cost
                    closest_dirty = i 
                    lowest_cost = manhattan 

            h += lowest_cost #new heuristic num (wowwww!)
            current_position = dirty_locations.pop(closest_dirty) #new pos reset
            lowest_cost = INF #reset
                    
    return h #return da heuristic


# TODO Update heuristic names and functions below. If you make more than two, add them here.
SPOTLESSROOMBA_HEURISTICS = {"Zero" : zero_heuristic,
                        "Arbitrary": arbitrary_heuristic, 
                        "Hamming": spotlessroomba_first_heuristic,
                        "Manhattan" : spotlessroomba_second_heuristic,
                        "Wack Manhattan": spotlessroomba_third_heuristic #omg its mine!
                        }
