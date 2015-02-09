#Siyang Li
#Lab 5: Load Graph
#2.26.2013

from vertex import Vertex

#definition of load_graph function that takes a CSV file and creates a dictionary
#of Vertex objects
def load_graph(file_name):
    data_file = open(file_name, "r") #opens file
    
    vertex_dictionary = {} #creates empty dictionary to be appended onto
        
    #for-loop that takes each line in the text file and returns a dictionary with CSV data
    for raw_data_string in data_file:
        data_string = raw_data_string.strip() #strips white space
        data = data_string.split(";") #splits along ; which breaks to name, adjacent string,
        #and x, y coordinate string
        
        position_coordinates = data[2].split(",") #splits x, y coordinate into list
        
        x_position = int(position_coordinates[0]) #stores x, y position as integers into variables
        y_position = int(position_coordinates[1])

        #initializes object with obtained data; leave adjacent list as blank list
        vertex_object = Vertex(data[0], [], x_position, y_position)
        
        vertex_dictionary[data[0]] = (vertex_object) #appends dictionary with references
        #to created objects
    
    data_file.close() #closes file
    
    data_file = open(file_name, "r") #opens file again for second loop-around
    
    for raw_data_string in data_file: #for loop that goes through the the data file
        #again and adds list of references of adjacent vertices into self.adjacent
        data_string = raw_data_string.strip() #strips white space again
        data = data_string.split(";") #splits along ; which breaks to name, adjacent string,
        #and x, y coordinate string
        
        adjacent_data = data[1].split(",") #splits the string of vertices into list of vertices
        
        for raw_adjacent_vertex in adjacent_data: #for loop that takes each vertex and appends to self.adjacent
            #of object in dictionary
            adjacent_vertex = raw_adjacent_vertex.strip() #strips white space
            vertex_dictionary[data[0]].adjacent.append(vertex_dictionary[adjacent_vertex]) #appends to object
            
    data_file.close() #closes file
        
    return vertex_dictionary #returns the complete vertex dictionary