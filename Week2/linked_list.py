# Nodes for in the Linked List
class Node:

  # Initialise the new node
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
  
  # Create link between nodes
  def link(self, other_node):
    self.next = other_node
    other_node.prev = self

  def __str__(self):
    return self.data.__str__()


# Create the Linked List
class Linked_list:

  # Initialise the new list
  def __init__(self):
    self.first = None
    self.last = None

  # Adds a new node to the linked list
  def add_node(self, data):
    new_node = Node(data)

    # Check to see if there is any nodes in the list, if not create at beginning
    if self.first == None:
      self.first = new_node
    else:
      self.last.link(new_node)

    self.last = new_node
 
  # Retrieves node from the linked list
  def get_node(self, index):
    # Check to see if any nodes within list and print message if not
    if self.first == None:
      print("List is empty.")
      return
    
    current_node = self.first
    current_index = 0

    # Check to see if node requested is within the limits of the Linked List
    if current_node.next == None:
      print("Index out of bounds.")
      return

    # Check each node until it matches the node called
    while (current_index < index) and (current_node is not None):
      current_node = current_node.next
      current_index +=1
      
    if current_node is None:
      raise Exception("Cannot find item requested.")

    return current_node



# Main Progam

llist = Linked_list()

# Add nodes to list
llist.add_node("spam")
llist.add_node("eggs")
llist.add_node("bacon")

try: 
  print(llist.get_node(0))
  print(llist.get_node(1))
  print(llist.get_node(2))
  print(llist.get_node(10))
except Exception as e:
  print(e)
  