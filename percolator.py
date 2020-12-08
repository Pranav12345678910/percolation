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
        #search two moves ahead, look at every move you can make and then every move the opponent can make if you made that move, 
        #and see how good the gameboard is. The vertex that ultimately can yield the greatest number of good states after the opponent makes their 
        #next move is the one we want to pick 
        
    '''
    def pickVertex(graph, player):
        #picks the most promising vertex to search through (we can't search through every vertex)
        best_v_num = 0
        best_v = 0
        for x in self.V:
            if len(Neighbors(x, graph)) > best_v_num:
                best_v_num = len(Neighbors(x, graph))
                best_v = x
        return best_v
    '''

    def Searchthingy(graph, v):
        frontier = [v]
        discovered = set([v])  
        parents = {graph : ()}
        count = 0
        #2d list where each element is a three element tuple, where each tuple represents a game state, and the first element of the tuple is the root vertex, 
        #the second element is number of edges connected to our color vertices, and the third element is the amount of moves so far (including the opponents)
        while len(frontier) != 0:
            current_state = frontier.pop(0)
            discovered.add(current_state)
            #return if two moves ahead    
            if isGoal(current_state):
                #return every key in the dictionary (node) in the order of most recently to last recently placed nodes
                return parents[tuple(map(tuple, current_state))]
            neighboring_vertices = Neighbors(graph, v)  
            for neighbor in range(len(neighboring_vertices)):
                active_v = neighboring_vertices[neighbor]
                if active_v not in discovered:
                    frontier.append(active_v)
                    discovered.add(active_v)
                    