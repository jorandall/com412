class Stack:
  def __init__(self):
    self.internalArray = []
  
  def push(self, item):
    self.internalArray.append(item)

  def pop(self):
    if len(self.internalArray) != 0:
      a = self.internalArray[-1]
      del self.internalArray[-1]
      return a
    else:
      print("Stack is empty.")
  
  def peek(self):
    b = self.internalArray[-1]
    return b

  def __str__(self):
    return self.internalArray.__str__()


stack1 = Stack()

stack1.push(1)
stack1.push(4)
stack1.push(9)

print(stack1)

popped1 = stack1.pop()
print(popped1)
popped2 = stack1.pop()
print(popped2)
popped3= stack1.pop()
print(popped3)
popped4= stack1.pop()
print(popped4)

stack1.push("Linux")
stack1.push("Windows")
stack1.push("Mac OS X")
print(stack1)

peeked = stack1.peek()
print(peeked)
