import networkx as nx
from datetime import datetime

if __name__ == '__main__':
    g = nx.Graph()
    g.add_node("jhon" , {'name':'jhon' , 'age' : 25})
    g.add_node ("peter" , {'name' : 'peter', 'age' : 35})
    g.add_node ("mary" , {'name' : 'mary' , 'age' : 31})

    print(g.nodes())
    print(g.edges())

print(g.has_edge("peter" , "mary"))