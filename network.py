import sys

MAX = 10

def min_distance(dist, visited, n):
    """
    Find the vertex with the minimum distance value that hasn't been visited.
    """
    min_val = sys.maxsize
    min_index = -1

    for i in range(n):
        if not visited[i] and dist[i] <= min_val:
            min_val = dist[i]
            min_index = i
    return min_index

def print_path(parent, j):
    """
    Print the path from the source node to the given node.
    """
    if parent[j] == -1:
        print(j, end="")
        return
    print_path(parent, parent[j])
    print(f" -> {j}", end="")

def dijkstra(graph, n, start):
    """
    Implement Dijkstra's algorithm to find the shortest path from the start node.
    """
    dist = [sys.maxsize] * n  # Array to store the shortest distance from the start node
    visited = [False] * n     # Array to track which nodes have been visited
    parent = [-1] * n         # Array to store the shortest path tree

    # Distance to the source node is 0
    dist[start] = 0

    for _ in range(n - 1):
        # Get the vertex with the minimum distance that hasn't been visited
        u = min_distance(dist, visited, n)
        visited[u] = True

        # Update the distance value for all neighboring nodes of u
        for v in range(n):
            if not visited[v] and graph[u][v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u

    # Print the shortest distance and the path for each node
    print("Node\tDistance from Source\tPath")
    for i in range(n):
        print(f"{i}\t{dist[i]}\t\t\t", end="")
        print_path(parent, i)
        print()

def main():
    """
    Main program to demonstrate Dijkstra's algorithm.
    """
    n = int(input("Enter the number of nodes in the graph: "))

    print("Enter the adjacency matrix (enter 0 if there is no edge between nodes):")
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    start = int(input("Enter the starting node: "))
    dijkstra(graph, n, start)

if __name__ == "__main__":
    main()
