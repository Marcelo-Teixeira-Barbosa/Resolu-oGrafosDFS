from collections import defaultdict
 
# 
# cria lista de adjacencia
 
 
class Graph:
    
 
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)
        self.isCycle = False
 
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def getCycle(self):
        if(self.isCycle == True):print("\nÉ UM GRAFO CÍCLICO\n")
        else: print("\nNÃO É UM GRAFO CÍCLICO\n")

    
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
 
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
            else: self.isCycle = True
 
    
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
 
def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    #g.addEdge(6, 6)

    b = Graph()
    b.addEdge(0,1)
    b.addEdge(0,2)
    b.addEdge(1,2)
    b.addEdge(2,0)
    b.addEdge(2,3)
    print("O GRAFO: ")
    g.DFS(0)
    g.getCycle()
    print("O GRAFO: ")
    b.DFS(0)
    b.getCycle()

main()