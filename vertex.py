#Siyang Li
#Lab 5: Vertex Class
#2.26.2013

from cs1lib import *

VERTEX_RADIUS = 7 #constant set for the radius of vertex points
EDGE_WIDTH = 3 #constant set for the width of the edges

#definition for Vertex class; has __init__ function that creates instance variables 
#from actual parameters and __str__ function that generates string that describes
#object and its variables
class Vertex:
    def __init__(self, name, adjacency_list, x_position, y_position):
        self.name = name
        self.adjacent = adjacency_list
        self.x = x_position
        self.y = y_position
        
        self.back = None #back-pointer to used for BFS
        
    def __str__(self):
        adjacent_string = "" #creates a blank string to be appended on to
        
        for adjacent_vertex in self.adjacent: #for loop that loops through list stored in self.adjacent
            adjacent_string += str(adjacent_vertex.name) + ", " #takes string of name, adds a ", " to it,
            #appends it to string
        
        #returns a string w/ proper formats (, and white space added in and extra , 
        #and white space taken out)                
        return str(self.name) + "; Location: " + str(self.x) + ", " + str(self.y) +\
             "; Adjacent vertices: " + adjacent_string.strip().strip(",")
    
    #method to draw circle (vertex) with constant radius at x, y position given RGB color        
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        
        draw_circle(self.x, self.y, VERTEX_RADIUS)
    
    #method to draw edge of constant width from vertex to given out-vertex with given RGB color    
    def draw_edge(self, out_vertex, r, g, b):
        enable_stroke()
        set_stroke_width(EDGE_WIDTH)
        set_stroke_color(r, g, b)
        
        draw_line(self.x, self.y, out_vertex.x, out_vertex.y)
    
    #method that takes draw_edges method and draws edges between the vertex and all its adjacent vertices   
    def draw_adjacent_edges(self, r, g, b):
        for adjacent_edge in self.adjacent:
            self.draw_edge(adjacent_edge, r, g, b)
    
    #method that checks if mouse is in the area of smallest square that contains circle; 
    #returns Boolean True or False depending on the result       
    def check_vertex_on(self, x_mouse, y_mouse):
        if x_mouse in range(self.x-VERTEX_RADIUS+1, self.x+VERTEX_RADIUS) and y_mouse in range(self.y-VERTEX_RADIUS+1, self.y+VERTEX_RADIUS):
            return True
        else:
            return False