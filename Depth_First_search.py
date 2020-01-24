#Time Complexity: O(V+E) where V is number of vertices 
# in the graph and E is number of edges in the graph. 
#This code is only for undirected graphs

from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited[v] = True
        print(v, end = "")	#python3 function

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i,visited)

    def DFS(self, v):
        visited = [False]*len(self.graph)
        self.DFSUtil(v, visited)
'''
    def DFS(self): 
        V = len(self.graph)  #total vertices 
  
        # Mark all the vertices as not visited 
        visited =[False]*(V) 
  
        # Call the recursive helper function to print 
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(V): 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
'''
g = Graph()
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2)    #g.DFS()
