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
        #discovered needs to be a set with tuples that represent 1d states 
        discovered = set(v)  
        #state is a 2d tuple already, so since it is hashable I can immediately add it
        parents = {graph : ()}
        while len(frontier) != 0:
            current_state = frontier.pop(0)
            discovered.add()
            if isGoal(current_state):
                #return every key in the dictionary (node) in the order of most recently to last recently placed nodes
                return parents[tuple(map(tuple, current_state))]
            neighbors = convertStates(computeNeighbors(current_state))  
            for neighbor in range(len(neighbors)):
                active_state = neighbors[neighbor]
                if tuple(flatten(active_state)) not in discovered:
                    frontier.append(active_state)
                    discovered.add(tuple(flatten(active_state)))
                    new_path = list(parents[(tuple(map(tuple, current_state)))])
                    new_path.append(computeNeighbors(current_state)[neighbor][0])
                    parents[tuple(map(tuple, active_state))] = tuple(new_path)