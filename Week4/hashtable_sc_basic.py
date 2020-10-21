class Hashtable:
  def __init__(self, capacity=127):
    self.size = capacity
    self.array = [None] * self.size
    
  # Work out ASCII code for the key
  def hash(self, key):
    hashCode = 0

    for letter in key:
      hashCode += ord(letter)
    
    hashCode = hashCode % self.size
    return hashCode

# Add a new item to the hashtable
  def put(self, key, value):
    hashCode = self.hash(key)

    if self.array[hashCode] == None:
      self.array[hashCode] = []

    self.array[hashCode].append((key, value))


# Find an item in the hashtable
  def get(self, key):
    hashCode = self.hash(key)

    bucket = self.array[hashCode]

    if bucket == None:
      return None
    
    for entry in bucket:
      if entry[0] == key:
        return entry[1]
    
    return None

  def __str__(self):
    return self.array.__str__()

table = Hashtable(10)

table.put("cat", "meow")
table.put("dog", "woof")
table.put("act", "to do something")

print(table.get("cat"))