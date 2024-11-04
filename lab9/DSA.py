from collections import deque

# Exercise 1
class Graph:
    def __init__(self):
        # Initialize the graph as an adjacency list
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph if it doesn't already exist
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an edge between vertex1 and vertex2 (undirected)
        self.add_vertex(vertex1)  # Ensure vertex1 exists
        self.add_vertex(vertex2)  # Ensure vertex2 exists
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def print_graph(self):
        # Print each vertex and its adjacent vertices
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")
            
    # Exercise 2
            
    def dfs(self, start_vertex):
        # Start DFS from a given vertex
        visited = set()  # Set to keep track of visited vertices
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        # Recursive helper method for DFS
        visited.add(vertex)  # Mark the current vertex as visited
        print(vertex, end=' ')  # Print the current vertex

        # Recur for all adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
                
    # Exercise 3            
                
    def bfs(self, start_vertex):
        # Start BFS from a given vertex
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start_vertex])  # Initialize the queue with the start vertex
        visited.add(start_vertex)  # Mark the start vertex as visited

        while queue:
            vertex = queue.popleft()  # Remove a vertex from the front of the queue
            print(vertex, end=' ')  # Print the current vertex

            # Visit all the adjacent vertices
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
    # Exercise 4
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        # Find all paths from start_vertex to end_vertex
        path = path + [start_vertex]  # Create a new path including the current vertex
        if start_vertex == end_vertex:
            return [path]  # Return the path if the start and end vertices are the same
        if start_vertex not in self.graph:
            return []  # Return an empty list if the start vertex is not in the graph

        paths = []  # List to store all paths
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:  # Avoid cycles by checking if neighbor is already in the path
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()


print("\nDFS starting from vertex 0:")
g.dfs(0)

print("\nBFS starting from vertex 0:")
g.bfs(0)

print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))
