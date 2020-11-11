numbers = [64, 25, 12, 22, 11, 65]

for i in range(len(numbers)- 1):
  lowest_num = i
  for j in range(i+1, len(numbers)- 1):
    if numbers[j] < numbers[lowest_num]:
      lowest_num = j
  
  numbers[i], numbers[lowest_num] = numbers[lowest_num], numbers[i]

print(numbers)