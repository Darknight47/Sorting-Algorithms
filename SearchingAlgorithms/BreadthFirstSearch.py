from collections import deque

def bfs(graph, start):
    """
        Perform a breadth-first search (BFS) on the given graph starting from the specified node.

        Parameters:
        graph (dict): The graph represented as an adjacency list.
        start (any): The starting node for BFS.

        Returns:
        list: A list of nodes in the order they were visited.
    """
    # Create a queue for BFS and enqueue the starting node
    queue = deque([start])

    # Mark the starting node as visited
    visited = set([start])

    # List to store the order of visited nodes
    bfs_order = []

    while queue:
        # Dequeue a node from the queue
        current_node = queue.popleft()

        # Process the current node (here we did it to the BFS order)
        bfs_order.append(current_node)

        # Get all adjacent nodes of the current node
        for neighbor in graph[current_node]:
            if(neighbor not in visited):
                # Mark the neighbor as visited
                visited.add(neighbor)
                # Enqueue the neighbor
                queue.append(neighbor)
    
    return bfs_order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
start_node = 'A'
print("BFS Order:", bfs(graph, start_node))