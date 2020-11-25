import collections 

# Define Node class
class TreeNode:
  def __init__(self,value):
    self.left = None
    self.value = value  
    self.right = None

# To insert a new node
  def insert_node(self, value):

# Check if the new node's value is less than the root value
    if value < self.value:
# If node to the left is empty, place new node to the left  
      if self.left is None: 
        self.left = TreeNode(value)
# If node to the left isn't empty, repeat until empty left node found
      else:
        self.left.insert_node(value)
# Check if the new node's value is greater than the root value 
    elif value > self.value:
# If the node to the right is empty, place new node to the right 
      if self.right is None:  
        self.right = TreeNode(value)
# If node to the right isn't empty, repeat until empty right node found
      else:
        self.right.insert_node(value)  


# Define Tree class
class BinaryTree:
  def __init__(self):
    self.root = None

# To insert new nodes into the Tree
  def insert(self, value):
    if self.root is None:
      self.root = TreeNode(value)
    else:
      self.root.insert_node(value)

# Print out the nodes
  def printTree(self, current_node):
# Check to see if there is a node to the left
    if current_node.left is not None:
      self.printTree(current_node.left)

    print(current_node.value)

# Check to see if there is a node to the right
    if current_node.right is not None:
      self.printTree(current_node.right)

# Breadth-first search method for tree
  def bfs(self, item):
    queue = collections.deque([])
    queue.append(self.root)

    while len(queue) != 0:
      node = queue.popleft()
      if node.value == item:
        return item
      else:
        if node.left is not None:
          queue.append(node.left)
        if node.right is not None:
          queue.append(node.right)


    
# Main program

tree = BinaryTree()

tree.insert(10)
tree.insert(3)
tree.insert(14)
tree.insert(6)
tree.insert(18)

#tree.printTree(tree.root)

print(tree.bfs(18))