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

    def computeFutureGraph(graph, v):
        pass
    def computeFutureGraphs(graph, v):
        pass
    def ChooseVertexToColor(graph, player):
        #do not create patches of only your color (connections involving two of your own vertices are harmful)
        #try to connect to their vertices as much as possible and our own vertices as little as possible
        #for a defensive strategy, try to have the max number of connections to vertices with a large number of connections
        uncolored = [x for x in graph.V if x.color == -1]
        num_color = {i: PercolationPlayer.numVerticesNotOurs(graph, i, player) for i in uncolored}  
        best_vertex_pair = sorted(num_color.items(), key=lambda x: x[1], reverse = True)[0]
        return best_vertex_pair[0]


    def ChooseVertexToRemove(graph, player):
        #search two moves ahead, look at every move you can make and then every move the opponent can make if you made that move, 
        #and see how good the gameboard is. The vertex that ultimately can yield the greatest number of good states after the opponent makes their 
        #next move is the one we want to pick 
        bot_graphs = PercolationPlayer.Searchthingy(graph)
        


    def graphWithoutVertex(graph, v):
        #returns a new graph without the original vertex v and without its corresponding edges
        #contructing new graph
        # newV = {x for x in graph.V if x!= v}
        # newE = {y for y in graph.E if y.a != v or y.b != v}
        # return Graph(newV, newE)
        #removing
        graphB = graph.copy()
        graphB.V = graphB.V.remove(v)
        for x in graphB.E:
            if x.a == v or x.b == v:
                graphB.E = graphB.E.remove(x)
        return graphB

    def Searchthingy(graph):
        ourColor = 0
        #list with tuple pairs, where first element in pair is graph that is created and second element is vertex
        graphs_without_vertices_pairs = []
        graphs_without_vertices = []
        bot_graphs = []
        for x in graph.V:
            if x.color == ourColor:
                graphs_without_vertices_pairs.append((PercolationPlayer.graphWithoutVertex(graph, x), x))
        for x in graphs_without_vertices_pairs:
            graphs_without_vertices.append(x[0])
        for x in graphs_without_vertices:
            for y in x.V: 
                if y != ourColor:
                    bot_graphs.append((PercolationPlayer.graphWithoutVertex(graph, y), graphs_without_vertices_pairs[graphs_without_vertices.index([x]), 1]))
        return bot_graphs
        