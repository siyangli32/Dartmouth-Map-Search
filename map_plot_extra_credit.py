#Siyang Li
#Lab 5: Map Plot
#3.2.2013

from cs1lib import *
from load_graph import *
from bfs import breadth_first_search
from random import *

#main function to draw and run interactive map
def map_plot():
    #draws the Dartmouth map in the background; this is drawn only once outside
    #the main animation/calculations loop
    dartmouth_map = load_image("dartmouth_map.png")
    draw_image(dartmouth_map, 0, 0)
    
    #creates the vertex dictionary from load_graph function; has references to objects
    #of map vertices (aka locations)
    vertex_dictionary = load_graph("dartmouth_graph.txt")
    
    #draws the initial vertices and edges (aka locations and roads) on the map;
    #this is done outside loop to prevent overwriting the created paths from BSF
    for vertex in vertex_dictionary:
        vertex_dictionary[vertex].draw_adjacent_edges(0, 0, 1)
        vertex_dictionary[vertex].draw_vertex(0, 0, 1)
    
    #draws labels on all points in map; extra credit option 
    for vertex in vertex_dictionary:
        enable_stroke()
        set_font_bold()
        set_font_size(8)
        set_stroke_color(0, 0, 0)
        draw_text(str(vertex_dictionary[vertex].name), vertex_dictionary[vertex].x + 30, vertex_dictionary[vertex].y - 15, True, True)
    
    #initializes the start, goal, and path_lists to be none; they will be filled in
    #later from input information from graphics screen
    start = None
    goal = None
    path_list = None
    
    #our main while loop that runs as long as program window is open
    while not window_closed():
        #random color generator; makes start vertex flash when set;
        #makes path line join in if in search; extra credit
        r = uniform(0, 1)
        g = uniform(0, 1)
        b = uniform(0, 1)
        
        #our first if-statement to search for a start vertex; will run if mouse is clicked
        if mouse_down():
            #start vertex is found and set through this for-loop; runs through all
            #vertex in dictionary
            for vertex in vertex_dictionary:
                #if-statement to see if a vertex is clicked on (position of mouse is on it when mouse was down)
                if vertex_dictionary[vertex].check_vertex_on(mouse_x(), mouse_y()):
                    start = vertex_dictionary[vertex] #vertex clicked on is set as start vertex
        
        #second if-statement to search for a goal vertex; will run only once start vertex is set    
        if start != None:
            start.draw_vertex(r, g, b) #if the start vertex is found, draw the start vertex (so user can see)
            
            #this for-loop runs through all vertices in the dictionary to search for goal vertex
            for vertex in vertex_dictionary:    
                #goal vertex is found when mouse hovers the vertex (and not clicked since that resets start again)
                if not mouse_down() and vertex_dictionary[vertex].check_vertex_on(mouse_x(), mouse_y()):
                    goal = vertex_dictionary[vertex] #goal is set to this hovered-over vertex
                    
        #this third if-statement is used to find the shortest path between the start 
        #and goal vertices via breadth-first search; will only run if start and goal 
        #vertices have been set
        if start != None and goal != None:
            #sets path_list to a list of vertices in the shortest path between
            #start and goal vertices as found by BFS
            path_list = breadth_first_search(start, goal)     
            #sets goal to None once path has been found so BSF does not keep looping;
            #since we have path list, goal variable is no longer needed unless it changes
            #(for recalculation of path list); only calculates when necessary
            goal = None

        #fourth if-statement that draws the path from path list; will clear all old paths;
        #will only run if we have a path list 
        if path_list != None: 
            #for-loop that clears all old paths drawn; goes through all vertex in 
            #vertex dictionary to redraw vertex and edges; skips those in path list
            #to prevent redundancy (and thus flashing)
            for vertex in vertex_dictionary:
                if vertex_dictionary[vertex] not in path_list: #to avoid drawing in path list
                    vertex_dictionary[vertex].draw_adjacent_edges(0, 0, 1)
                    vertex_dictionary[vertex].draw_vertex(0, 0, 1)
            
            #for-loop to draw new path in; goes through all vertex in path list
            for vertex in path_list:
                if vertex.back != None: #if-statement to prevent unnecessary 
                    #and error-inducing last edge (start to None) from being drawn
                    vertex.draw_edge(vertex.back, r, g, b) #draws edge from vertex to its back-pointer
                    vertex.draw_vertex(r, g, b) #draws the vertex of points in path list
                
                start.draw_vertex(r, g, b) #draws the start vertex again since our for-loop inevitably does not include it
                
            path_list = None #sets the path list to None so that this if-statement will not loop;
            #will only repeat if new path_list is set; will only draw once and when necessary

        #last for-statement to clear the back pointer instance variable from all vertices;
        #this is so that BFS can be run again
        for vertex in vertex_dictionary:
                vertex_dictionary[vertex].back = None
                    
        #request redraw at end so that there should be no flashing (since all
        #draw functions are in ideal order before redraw); sleep also makes more fluid
        request_redraw()
        sleep(.1)
            
#actual start graphics function; sets window height and width to accomodate map            
start_graphics(map_plot, "Dartmouth Interactive Map", 1012, 811)