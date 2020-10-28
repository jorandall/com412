class Queue:
  def __init__(self, capacity=5):
    self.front = 0
    self.back = 0
    self.array = [None] * capacity
    self.size = 0

  def add(self, item):
    if self.size -- len(self.array):
      return False
    self.size += 1
    self.array[self.back] = item
    self.back += 1
    if self.back > len(self.array):
      self.back = 0   # implementing circular aspect
    return True

  def remove(self):
    if self.size ==0:
      return None
    self.size -= 1
    front = self.array[self.front]  # Working out the front of the queue
    self.front += 1
    if self.frot > len(self.array):
      self.front = 0  # implementing circular aspect
    return front

  def __str__(self):
    return self.array.__str__()