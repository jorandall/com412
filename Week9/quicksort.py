import math

def hoare_partition(data, start, end):
  i = start
  j = end
  mid = math.floor((start + end) / 2)
  pivot = data[mid]

  while True:
    while (data[i] < pivot):
      i += 1
    while (data[j] > pivot):
      j = j-1

    if i >= j:
      return j
    else:
      temp = data[i]
      data[i] = data[j]
      data[j] = temp

def quicksort(data, start, end):

  if end >= start:
    pivot = hoare_partition(data, start, end)
    quicksort(data, start, pivot-1)
    quicksort(data, pivot+1, end)


numbers = [5, 78, 36, 1, 17, 23, 80, 6, 11, 41]
quicksort(numbers, 0, len(numbers)-1)

print(numbers)
