import random
import copy 
from multiprocessing import Pool

class PercolationPlayer:
    #helper function that figures out the number of neighboring vertices with the opposite color
    def numVerticesNotOurs(graph, v, player):
        return len(PercolationPlayer.Neighbors(graph, v))

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
        #first element in the pair is a graph that the bot can create and the second element is the root vertex
        #if the game is over in less than 4 moves, then run hardcoded end game case
        bot_graphs = PercolationPlayer.Searchthingy(graph, player)
        if bot_graphs == []:
            edges = list(graph.V)[0]
            #return vertex with most connections period because its end game cases and that is very effective for end game
            for vertex in list(graph.V):
                if vertex.color == player:
                    if len(PercolationPlayer.IncidentEdges(graph, vertex)) > len(PercolationPlayer.IncidentEdges(graph, edges)):
                        edges = vertex
            return edges
        else: 
            return PercolationPlayer.RankOppositeStates(bot_graphs, player, graph)
        
    def RankOppositeStates(botGraphs, player, original_graph):
        optionsOfEdgeNumbers = []
        original_count = 0
        v_dict = {}
        ourTeamColor = player
        #figure out count for inital graph
        for original_graph_edge in original_graph.E:
            if (original_graph_edge.a.color != ourTeamColor and original_graph_edge.b.color == ourTeamColor) or (original_graph_edge.a.color == ourTeamColor and original_graph_edge.b.color != ourTeamColor):
                original_count += 1
            if (original_graph_edge.a.color != ourTeamColor and original_graph_edge.b.color != ourTeamColor):
                original_count -= 1
            if original_graph_edge.a.color == ourTeamColor and original_graph_edge.b.color == ourTeamColor:
                original_count += 1
        for graphRepresentation in botGraphs:
            graph1 = graphRepresentation[0]
            count = 0
            for edge in graph1.E:
                if (edge.a.color != ourTeamColor and edge.b.color == ourTeamColor) or (edge.a.color == ourTeamColor and edge.b.color != ourTeamColor):
                    count += 1
                if (edge.a.color != ourTeamColor and edge.b.color != ourTeamColor):
                    count -= 1
                if edge.a.color == ourTeamColor and edge.b.color == ourTeamColor:
                    count += 1 
            result = [graphRepresentation[1], count - original_count]
            optionsOfEdgeNumbers.append(result)
        #figure out the average count for each pair with the same vertex
        #split options of edge numbers so that there is a 2d list for each subtree
        for x in optionsOfEdgeNumbers:
            y = x[0]
            try: 
                if y in v_dict:
                    print(var_doesnt_exist)
                else:
                    v_dict[y] = [x[1]]
            except:
                v_dict[y].append(x[1])
        #average each of the second values (counts) for each of the subtrees
        for x in v_dict:
	        y = sum(v_dict[x])/len(v_dict[x])
	        v_dict[x] = y
        #pick root vertex of subtree that has the highest average count
        final_result = sorted(v_dict.items(), key=lambda x: x[1])[0][0]
        return final_result

    def IncidentEdges(graph, v):
        return [e for e in graph.E if (e.a == v or e.b == v)]

    def findVertex(graph_find, index):
        return [x for x in graph_find.V if x.index == index][0]

    '''
    def graphWithoutVertex(graph_with, index):
        #returns a new graph without the original vertex v and without its corresponding edges and without vertices that may get isolated
        graphB = copy.deepcopy(graph_with)
        vertex = PercolationPlayer.findVertex(graphB, index)
        edge_copy = copy.deepcopy(graphB.E)
        for x in edge_copy:
            if x.a == vertex or x.b == vertex:
                graphB.E.remove(x)
        graphB.V.remove(vertex)
        vertex_copy = copy.deepcopy(graphB.V)
        for x in vertex_copy:
            for y in graphB.E:
                if y.a == x or y.b == x:
                    break
            graphB.V.remove(PercolationPlayer.findVertex(graphB, x.index))
        return graphB
    '''

    def Percolate(graph, index):
        graphB = copy.deepcopy(graph)
        v = PercolationPlayer.findVertex(graphB, index)
        # Get attached edges to this vertex, remove them.
        for e in PercolationPlayer.IncidentEdges(graphB, v):
            graphB.E.remove(e)
        # Remove this vertex.
        graphB.V.remove(v)
        # Remove all isolated vertices.
        to_remove = {u for u in graphB.V if len(PercolationPlayer.IncidentEdges(graphB, u)) == 0}
        graphB.V.difference_update(to_remove)
        return graphB
    
    def Searchthingy(graph_search, player):
        bot_graphs = []
        ourColor = player
        #list with tuple pairs, where first element in pair is graph that is created and second element is vertex
        graphs_without_vertices_pairs = []          
        for x in graph_search.V:
            if x.color == ourColor:
                graphs_without_vertices_pairs.append((PercolationPlayer.Percolate(graph_search, x.index), x))
        for x in graphs_without_vertices_pairs:
            z = x[0]
            for y in z.V: 
                if y != ourColor:
                    bot_graphs.append((PercolationPlayer.Percolate(graph_search, y.index), graphs_without_vertices_pairs[graphs_without_vertices_pairs.index(x)][1]))
        return bot_graphs   