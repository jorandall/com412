import collections
from heapq import heappush, heappop
import sys

class Node:
  def __init__(self, name):
    self.dist = sys.maxsize
    self.name = name
    self.parent = None
    self.to_check = True
    self.edges = []

  def add_edge(self, edge):
    self.edges.append(edge)

  # Converting items in tuple for program to understand and check less than
  def __lt__(self, other):
    return self.name < other.name

class Edge:
  def __init__(self, start, end, dist):
    self.start = start
    self.end = end
    self.dist = dist

class Graph:
  def add_edge(self, start, end, dist):
    start.add_edge(Edge(start, end, dist))
    end.add_edge(Edge(end, start, dist))

  def dijkstra(self, start, end):
    # Control variable to keep track of current node
    current_node = None
    # Control variable to keep track of nodes needing consideration
    open_list = []

    # Set total distance of the start node to 0
    start.dist = 0
    # Add the starting node to list of nodes to search
    heappush(open_list, (0, start))

    # While there are nodes to our list to search
    while len(open_list) > 0:
      #  Retrieve the next node and its distance and remove from list
      dist, current_node = heappop(open_list)

      # Check each edge of the node
      for edge in current_node.edges:
        # If the next node has already been checked, move on
        if edge.end.to_check == False:
          continue

        # Work out total distance to current node from the start
        path_dist = dist + edge.dist
        # Control variable for shortest distance, set to total distance as default
        shortest_dist = edge.end.dist

        # If new shortest path discovered, update parent of next node to current node and update shortest distance variable accordingly
        if path_dist < edge.end.dist:
          edge.end.parent = current_node
          shortest_dist = path_dist
        
        # Set total distance of the next node to new shortest distance, or keep it as was if no new path found
        edge.end.dist = shortest_dist

        # Add the next node to the list of nodes to be checked
        heappush(open_list, (shortest_dist, edge.end))

      # Updated current node to checked
      current_node.to_check = False

    # Once path identified, store in a queue
    route = collections.deque([])

    # Starting from end node, check each parent and add to the route list until we're back at the start
    while current_node is not None:
      route.appendleft(current_node)
      current_node = current_node.parent

    # Return the compiled route
    return route


# Create a graph
graph = Graph()

# Create all of the nodes
london    = Node("London")
munich    = Node("Munich")
brussels  = Node("Brussels")
paris     = Node("Paris")
amsterdam = Node("Amsterdam")
cologne   = Node("Cologne")
frankfurt = Node("Frankfurt")
stuttgart = Node("Stuttgart")
dublin    = Node("Dublin")

# Create all of the edges
graph.add_edge(london,     brussels,   370)
graph.add_edge(london,     paris,      461)
graph.add_edge(brussels,   amsterdam,  211)
graph.add_edge(brussels,   cologne,    211)
graph.add_edge(amsterdam,  cologne,    263)
graph.add_edge(cologne,    frankfurt,  190)
graph.add_edge(frankfurt,  stuttgart,  207)
graph.add_edge(frankfurt,  munich,     393)
graph.add_edge(paris,      frankfurt,  572)
graph.add_edge(paris,      stuttgart,  624)
graph.add_edge(stuttgart,  munich,     221)

# Find the route
route = graph.dijkstra(london, munich)

# Print out the results
print("Route:")
for node in route:
  print("   {}".format(node.name))
  print("--->")

print("")
print("Total distance: {}".format(route[-1].dist))