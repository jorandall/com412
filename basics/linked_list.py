# Nodes for in the Linked List
class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
  
  def link(self, otherNode):
    self.next = otherNode
    otherNode.prev = self

  def __str__(self):
    return self.data.__str__()



n1 = Node("Fred")
n2 = Node("Tom")
n3 = Node("Harry")

print(n1)
print(n2)

n1.link(n2)
n2.link(n3)

print(n1.next)
print(n1.prev)
print(n2.next)
print(n2.prev)

