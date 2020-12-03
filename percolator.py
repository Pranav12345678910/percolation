import random

class PercolationPlayer:
    
    #helper function that figures out the number of neighboring vertices with the opposite color
    def numVerticesNotOurs(self, graph, v, player):
        if player == 0:
            opposite_color = 1
        if player == 1:
            opposite_color = 0
        count = 0
        for x in v.Neighbors():
            if (x.color == opposite_color) or (x.color == -1):
                count += 1
        return count

    def Neighbors(self, graph, v):
        adjacent = []   
        for i in graph.E:
            if i.a == v:
                adjacent.append(i.b)
            if i.b == v:
                adjacent.append(i.a)
        return adjacent

    def ChooseVertexToColor(self, graph, player):
        #do not create patches of only your color (connections involving two of your own vertices are harmful)
        #try to connect to their vertices as much as possible and our own vertices as little as possible
        #for a defensive strategy, try to have the max number of connections to vertices with a large number of connections
        uncolored = []
        num_color = {}
        print(graph)
        for x in graph.V:
            if x.color == -1:  
                uncolored.append(x)
        if len(uncolored) == len(graph.self.V):
            print(player)
        for i in uncolored:
            num_color[i] = self.numVerticesNotOurs(graph, i, player)
        vertex_to_color = sorted(num_color.items(), key=lambda x: x[1], reverse = True)[0]
        return vertex_to_color

    def ChooseVertexToRemove(self, graph, player):
        #want to minimize isolation of your own vertices    
        #delete ones that have the least amount of connections to your vertices and the most amount of connections to other vertices
        #very bad to have several of your own vertices touching
        uncolored = []
        num_color = {}
        for x in graph.V:
            if x.color == -1:  
                uncolored.append(x)
        for i in uncolored:
            numVerticesOurs = len(graph.self.V) - self.numVerticesNotOurs(graph, i, player) 
            num_color[i] = self.numVerticesNotOurs(graph, i, player) - numVerticesOurs
        vertex_to_color = sorted(num_color.items(), key=lambda x: x[1], reverse = True)[0]
        return vertex_to_color