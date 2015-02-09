#Siyang Li
#Lab 5: Breadth-First Search
#3.2.2013

from collections import deque

#Breadth-first search function; takes start and goal vertices to find shortest point
#between the two
def breadth_first_search(start, goal):
    
    q = deque() #creates an empty deque to store the frontier
    q.append(start) #appends start to the frontier
    x = None #initializes x, a variable to store the last popped (as well as to get goal at end);
    #set as None to be set later on
    
    #while loop that keeps running until goal is reached (goal was last popped from queue)
    while x != goal:
        x = q.popleft() #stores last_popped from queue (from frontier) into x
        
        #for-loop that goes through the adjacent vertices of last-popped (from frontier)
        #to search for vertices not yet reached
        for adjacent_vertex in x.adjacent:
            if adjacent_vertex.back == None and adjacent_vertex != start: #new vertices
                #are those that have no back-pointer set and is not the start vertex
                adjacent_vertex.back = x #sets the adjacent vertex's back-pointer to itself
                q.append(adjacent_vertex) #appends the vertex into the queue/frontier
                
        #process will keep going on with the queue growing and being popped until goal is met;
        #back-pointers should be assigned in process
    
    #back-tracking process
    
    path_list = [] #initializes an empty list to contain the back-tracked list of vertex in path
    #of start to goal
    
    #while-loop that takes x (which after previous while-loop now contains goal) and back-traces to the start
    #adding vertices to path_list as it goes
    while x != None: #runs until None is hit (since there will be nothing to append)
        path_list.append(x) #appends vertex to path list
        x = x.back #sets x to x.back to back-track after each iteration of while-loop, going towards start
    
    #once while-loop ends, path list is complete
    
    return path_list #return path_list as final result