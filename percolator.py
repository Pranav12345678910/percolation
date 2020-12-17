import random
import heapq

class PercolationPlayer:
	def IncidentEdges(graph, vertex):
		return [e for e in graph.E if (e.a == vertex or e.b == vertex)]

	def Neighbors(graph, v):
		adjacent = []
		for i in graph.E:
			if i.a == v:
				adjacent.append(i.b)
			if i.b == v:
				adjacent.append(i.a)	
		return adjacent

	def numVerticesNotOurs(graph, v, player):
		return len(PercolationPlayer.Neighbors(graph, v))

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		uncolored = [i for i in graph.V if i.color == -1]
		num_color = {i: PercolationPlayer.numVerticesNotOurs(graph, i, player) for i in uncolored}
		best_vertex_pair = sorted(num_color.items(), key=lambda x: x[1], reverse = True)[0]
		return best_vertex_pair[0]

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 7:
					return v
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 6:
					return v
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 5:
					return v
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 4:
					return v	
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 3:
					return v
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 2:
					return v				
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]) > 1:
					return v
		for v in graph.V:
			if v.color == player:
				if len([x for x in PercolationPlayer.Neighbors(graph, v) if x.color != player]):
					return v		
		return random.choice([v for v in graph.V if v.color == player])		