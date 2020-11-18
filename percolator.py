import random

def ChooseVertexToColor(graph, player):
    return random.choice([v for v in graph.V if v.color == -1])

def ChooseVertexToRemove(graph, player):
    return random.choice([v for v in graph.V if v.color == player])
