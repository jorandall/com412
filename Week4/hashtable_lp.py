class Hashtable:
  def __init__(self, capacity=127, factor=31):
    self.size = capacity
    self.array = [None] * self.size
    self.factor = factor
    
  # Work out ASCII code for the key
  def hash(self, key):
    hashCode = 0

    for index in range(0, len(key)):
     letter = key[index]
     asciiCode = ord(letter)
     hashCode += asciiCode * (self.factor ** index)
    
    hashCode = hashCode % self.size
    return hashCode

# Add a new item to the hashtable
  def put(self, key, value):
    hashCode = self.hash(key)

    for i in range(0, self.size):
      index = (i + hashCode) % self.size

      if self.array[index] == None:
        self.array[index] = (key, value)
        return

    print("Table is full")


# Find an item in the hashtable
  def get(self, key):
    hashCode = self.hash(key)

    for i in range (0, self.size):
      index = (i + hashCode) % self.size
      entry = self.array[index]

      if entry != None and entry[0] == key:
        return entry[1]
    
    return None

  def __str__(self):
    return self.array.__str__()

table = Hashtable(10, 31)

table.put("cat", "meow")
table.put("dog", "woof")
table.put("act", "to do something")
table.put("sea", "a large body of water")

print(table)

print(table.get("act"))
print(table.get("dog"))