# Define a class for graph nodes
class GraphNode:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors or []

# Create some nodes and link them together to form a graph
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node1.neighbors.append(node2)
node1.neighbors.append(node3)
node2.neighbors.append(node1)
node2.neighbors.append(node3)
node3.neighbors.append(node1)
node3.neighbors.append(node2)

# Print the graph
def print_graph(node):
    visited = set()
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        print(current.value)
        visited.add(current)
        queue.extend(current.neighbors)

print_graph(node1)
