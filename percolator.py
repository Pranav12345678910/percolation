import random

def ChooseVertexToColor(graph, player):
    #do not create patches of only your color (connections involving two of your own vertices are harmful)
    #try to connect to their vertices as much as possible and our own vertices as little as possible 
    return random.choice([v for v in graph.V if v.color == -1])

def ChooseVertexToRemove(graph, player):
    #want to minimize isolation of your own vertices
    #delete ones that have the least amount of connections to your vertices and the most amount of connections to other vertices
    #very bad to have several of your own vertices touching           
    return random.choice([v for v in graph.V if v.color == player])
