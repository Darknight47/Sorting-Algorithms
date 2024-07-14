def dfs(graph, start):
    """
        Perform a depth-first search (DFS) on the given graph starting from the specified node.

        Parameters:
        graph (dict): The graph represented as an adjacency list.
        start (any): The starting node for DFS.

        Returns:
        list: A list of nodes in the order they were visited.
    """
    # Stack datastructure for DFS and push the starting node
    stack = [start]

    # Mark the starting node as visited
    visited = set([start])

    # List to store the order of visited node
    dfs_order = []

    while stack:
        # Pop a node from the stack
        current_node = stack.pop()

        # Process the current_node 
        dfs_order.append(current_node)

        # Get all adjacent nodes of the current node
        # Push unvisited neighbors onto the stack
        for neighbor in reversed(graph[current_node]):
            if(neighbor not in visited):
                # Mark the neighbor as visited
                visited.add(neighbor)
                # Push the neighbor onto the stack
                stack.append(neighbor)
        
    return dfs_order
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
print("DFS Order:", dfs(graph, start_node))

"""
DFS Order: ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
    A
   / \
  B   C
 /|   |\
D E   F G
  |
  H

DFS explores as far as possible along each branch before backtracking. In your example graph, it starts with 'A', explores all reachable nodes from 'A', 
then backtracks and explores deeper branches from 'B' and 'C' in a depth-first manner. The order in which nodes are visited is influenced by the stack, 
where nodes are pushed and popped according to the last-in, first-out (LIFO) principle. 
"""