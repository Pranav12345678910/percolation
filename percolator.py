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
        pass

    def graphWithoutVertex(graph, v):
        #returns a new graph without the original vertex v and without its corresponding edges
        newV = {x for x in graph.V if x!= v}
        newE = {y for y in graph.E if y.a != v or y.b != v}
        return Graph(newV, newE)

    def Searchthingy(graph, v):
        frontier = [graph]
        #list that contains several tuple pairs, where the first element is a graph (state) and the second element is the depth in the tree (sort of like count)
        neighboring_states = []
        count = 0
        while len(frontier) != 0:
            current_state = frontier.pop(0)
            #if we have fully reached the 2 step depth, then return
            #we know if we have fully searched a depth if the number of vertices that we could have removed
            #on the previous level is equivalent to the number of states we have discovered 
            pass
            if neighboring_states[len(neighboring_states) - 1][1] == 2:
                #return all the 2 depth graphs in neighboring state
                pass
            for neighbor in computeFutureGraph(current_state, v):
                #having trouble figuring out how to do an entire graph depth and then move on to the next depth. Because then how do I fill frontier. 
                #I need to fill it with all of one depth and then search that depth after I have fully searched the previous one
                #I don't want to search just one thing at a time and then keep doing it again and again
                pass
        pass
            
                    