##Write a Python program that takes a list of random integers as input and returns the sum of the even numbers in the list. However, you are not allowed to use built-in Python functions such as `sum()` or `filter()`.

##Your program should include the following helper functions:

##`num_list_generator(n, low, high)`: Generates a list of `n` random integer numbers within \[`low`, `high`\]

##`is_even(num)`: A function that takes an integer `num` as input and returns `True` if `num` is even, and `False` otherwise.

##`sum_even_numbers(int_lst)`: A function that takes a list of integers `int_lst` as input and returns the sum of the even numbers in the list.



import random

def num_list_generator(n, low, high):
  """Generates a list of n random integer numbers within [low, high]."""
  return [random.randint(low, high) for _ in range(n)]

def is_even(num):
  """Checks if a number is even."""
  return num % 2 == 0

def sum_even_numbers(int_lst):
  """Calculates the sum of even numbers in a list without using sum() or filter()."""
  even_sum = 0
  for num in int_lst:
    if is_even(num):
      even_sum += num
  return even_sum

# Generate a list of random numbers
random_list = num_list_generator(10, 1, 100)
print("Generated list:", random_list)

# Calculate the sum of even numbers
even_sum_result = sum_even_numbers(random_list)
print("Sum of even numbers:", even_sum_result)