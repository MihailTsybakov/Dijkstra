# Realization of Dijkstra's algorithm of calculating shortest ways in planar graphs
# Node input template: [number of node, status, distance mark, number of neighbour nodes, <neighbour nodes + weights>]

import math

class Graph():
    def __init__(self, node_array):
        print("New graph initialized")
        print("-"*20)
        self.node_array = node_array

def graph_input():
    graph = []
    number_of_nodes = int(input("Enter number of graph's verticies: "))
    for i in range (0, number_of_nodes):
        temp_node = []
        temp_node.append(i+1)
        temp_node.append("Unvisited")
        temp_node.append(0) # Place for distance mark
        current_neighbours_number = int(input("Enter number of neighbours for {0} node: ".format(i+1)))
        temp_node.append(current_neighbours_number)
        temp_neighbours = []
        for j in range (0, current_neighbours_number):
            temp_neighbours.append(int(input("Enter number of current neighbour: ")))
            temp_neighbours.append(int(input("Enter weight of current connection: ")))
        temp_node.append(temp_neighbours)
        graph.append(temp_node)
        print("-"*20)
    return Graph(graph)

def dijkstra(graph):
    start_node = int(input("Enter number of start node: "))
    if (start_node <= 0  or start_node > len(graph.node_array)):
        print("Error: wrong node number")
        exit(-1)
    if (str(type(start_node)) != "<class 'int'>"):
        print("Error: entered number is not int")
        exit(-2)
    for i in range(0, len(graph.node_array)):
        if graph.node_array[i][0] != start_node:
            graph.node_array[i][2] = math.inf
    # Internal function which calculates mark for current node
    def mark_calculator(graph_node):
        neighbours = []
        for j in range(0, graph_node[3]):
            neighbours.append(graph_node[4][2*j] - 1)
        marks = []
        for i in range(0, len(neighbours)):
            marks.append(graph.node_array[neighbours[i]][2] + graph_node[4][2*i + 1])
        if (len(marks) > 0):
            if (min(marks) < graph_node[2]):
                graph_node[2] = min(marks)
            return min(marks)
        else:
            print("Error in mark calculator: incorrect input")
            return -1
        
    def processing_node(graph_node):
        neighbours = []
        for j in range(0, graph_node[3]):
            neighbours.append(graph_node[4][2*j] - 1)
        for i in range(0, len(neighbours)):
            mark_calculator(graph.node_array[neighbours[i]])
        graph_node[1] = "Visited"
        for i in range(0, len(neighbours)):
            if (graph.node_array[neighbours[i]][1] != "Visited"):
                processing_node(graph.node_array[neighbours[i]])
    
    processing_node(graph.node_array[start_node - 1])

def graph_print(graph):
    for node in graph.node_array:
        print("Node {0} - neighbours: {1}".format(node[0], node[4]))
    print("-"*20)
        
def way_print(graph):
    for current_node in graph.node_array:
        print("To node {0} shortest way is {1}".format(current_node[0], current_node[2]))
        
graph_ = graph_input()
#graph_print(graph_)
dijkstra(graph_)
way_print(graph_)
            
        
    
    
        
            
        
        
        