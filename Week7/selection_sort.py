numbers = [64, 25, 12, 22, 11]

for i in range(len(numbers)):
  lowest_num = i
  for j in range(i + 1, len(numbers)):
    if numbers[lowest_num] > numbers[j]:
      lowest_num = j
  
  numbers[i], numbers[lowest_num] = numbers[lowest_num], numbers[i]

print(numbers)