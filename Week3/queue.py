class Queue:
# Initialise the queue
  def __init__ (self, capacity):
    self.internalArray = [None] * capacity
    self.front = 0
    self.back = 0
    self.size = 0
    self.maxSize = capacity

# Add new item to the queue
  def add(self, item):
    # Check to see if queue is at capacity
    if self.size == self.maxSize:
      print("Queue Full.")
   
    # If not, work out the next available space and add new item
    else:
      avail = (self.front + self.size) % len(self.internalArray)
      self.internalArray[avail] = item
      self.size += 1
      print(item, "added to queue.")


# Remove item from the queue
  def remove(self):
    # Check to see if queue is empty
    if self.size == 0:
      print("Queue Empty.")
    
    # If not, work out the front of the work and remove item
    else:
      item = self.internalArray[self.front]
      self.front = (self.front + 1) % len(self.internalArray)
      self.size -= 1
      print(item, "removed from queue.") 
 
  def __str__(self):
    return self.internalArray.__str__()
    return self.internalArray[self.front]
    return self.internalArray[self.back]

queue1 = Queue(2)

queue1.remove()       # Expected result: queue empty
queue1.add("spam")    # Expected result: spam added to queue
queue1.add("eggs")    # Expected result: eggs added to queue
queue1.add ("bacon")  # Expected result: queue full

queue1.remove()       # Expected result: spam removed from queue

queue1.add("bacon")   # Expected result: bacon added to queue
queue1.add("chips")   # Expected result: queue full

queue1.remove()       # Expected result: eggs removed from queue
queue1.add("chips")   # Expected result: chips added to queue
queue1.remove()       # Expected result: bacon removed from queue
queue1.remove()       # Expected result: chips removed from queue
queue1.remove()       # Expected result: queue empty

