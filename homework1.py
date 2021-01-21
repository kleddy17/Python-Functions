# Write a function named sum_to() that takes a number parameter n and returns the sum of 
# the numbers from 1 to n.
# For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55


# def sum_to (n):
#     total = []
#     for i in range(n+1):
#         total.append(i)
#         finalTotal = sum(total)
#         print("the total is", finalTotal)


# print(sum_to(6))


# Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:
# largest([10, 4, 2, 231, 91, 54])  # returns 231
# largest([1,2,3,4,0])  # returns 4


# def largest(list): 
#    nums =[]
#    numsMax = []
#    for i in list:
#        nums.append(i)
#        numsMax.append(max(nums))
#     print(numsMax)


# largest([10, 4, 2, 231, 91, 54]) 

# 3
# Write a function named occurances() that takes two string parameters and
# counts the number of occurrances of the second string inside the first string. For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

# def occourances(str1, str2):
#     times_matched = 0
#     for i in str1:
#         if i == str2:
#             times_matched = times_matched+1
#     print(times_matched)

# occourances("fleep floop", "e")


#4
# Write a function named product() that takes an arbitrary number of parameters,
# multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

def product(*args):
  product = 1
  print(args)
  for arg in args:
    product *= arg
    print(product)
  return product

product(1,3,4,5)