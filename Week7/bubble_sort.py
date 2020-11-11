numbers = [24, 9, 1, 16, 7]

for a in range(len(numbers) - 1):
  for b in range(len(numbers) - a - 1):
    if(numbers[b] > numbers[b + 1]):
      temp = numbers[b]
      numbers[b] = numbers[b + 1]
      numbers[b + 1] = temp

print(numbers)