# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0
  for value in range(1, n+1):
    sum += value
  print(sum)

sum_to(10)

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  largest = 0
  for n in list:
    if n > largest:
      largest = n
  return largest

print(largest([1, 2, 3, 4, 0]))

# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'p'))

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  num = 1
  for arg in args:
    num *= arg
  return num

print(product(2, 5, 5))