import random

class PercolationPlayer:
    
    #helper function that figures out the number of neighboring vertices with the opposite color
    def numVerticesNotOurs(graph, v, player):
        if player == 0:
            opposite_color = 1
        if player == 1:
            opposite_color = 0
        print(opposite_color)
        count = 0
        for x in PercolationPlayer.Neighbors(graph, v):
            if (x.color == opposite_color) or (x.color == -1):
                count += 1
        return count

    def Neighbors(graph, v):
        adjacent = []   
        for i in graph.E:
            if i.a == v:
                adjacent.append(i.b)
            if i.b == v:
                adjacent.append(i.a)
        return adjacent

    def ChooseVertexToColor(graph, player):
        #do not create patches of only your color (connections involving two of your own vertices are harmful)
        #try to connect to their vertices as much as possible and our own vertices as little as possible
        #for a defensive strategy, try to have the max number of connections to vertices with a large number of connections
        uncolored = [x for x in graph.V if x.color == -1]
        num_color = {i: PercolationPlayer.numVerticesNotOurs(graph, i, player) for i in uncolored}  
        best_vertex_pair = sorted(num_color.items(), key=lambda x: x[1], reverse = True)[0]
        return best_vertex_pair[0]


    def ChooseVertexToRemove(graph, player):
        #want to minimize isolation of your own vertices    
        #delete ones that have the least amount of connections to your vertices and the most amount of connections to other vertices
        #very bad to have several of your own vertices touching
        color = 0
        if player == 1:
            color = 1
        else:
            color = 0
        opposite_colored = [x for x in graph.V if x.color != color]
        num_color = {i: PercolationPlayer.numVerticesNotOurs(graph, i, player) for i in opposite_colored} 
        print(num_color.items())
        best_vertex_pair = sorted(num_color.items(), key=lambda x: x[1], reverse = True)[0]
        return best_vertex_pair[0]