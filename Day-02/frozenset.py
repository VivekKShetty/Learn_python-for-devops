numbers = frozenset([1,2,3,4,5,6,7,8,8])  #unordered, no duplicates, imutables
print(numbers)
numbers.add(10)


# output
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}