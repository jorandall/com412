from heapq import heappush, heappop

# Create an empty list. This will be converted to a heap.
heap = []

# Add tuples containing a numerical value and another item of data (place name here) to the priority queue. If tuples are added, the queue will be prioritised using the first item in the tuple.
heappush(heap, (461, 'Paris'))
heappush(heap, (370, 'Brussels'))
heappush(heap, (1164, 'Munich'))
heappush(heap, (771, 'Frankfurt'))

# Remove each item one by one from the priority queue until it's empty.
while len(heap) > 0:
    hp = heappop(heap)
    print(hp)