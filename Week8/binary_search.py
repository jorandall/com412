import math

# List comprehension, filling list with the square of every number from 1-100
numbers = [i*i for i in range(1, 101)]

def binary_search(list, item):
# Start of the portion of the list
  start = 0
# End of the porition of the list
  end = len(list)-1

  found = False

  while start <= end and not found:
# Work out the midpoint and round down accordingly
    mid = math.floor((start + end) / 2)
# If midpoint is item, return true
    if list[mid] == item:
      found = True
# If not, keep looking
    else:
# If item is less than midpoint, end is midpoint less 1
      if item < list[mid]:
        end = mid - 1
# If item is more than midpoint, start is midpoint plus 1
      else:
        start = mid + 1
  
  # Return either true or false
  return found

# Search 
print(binary_search(numbers, 4900))