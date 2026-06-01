my_set = {1,2,3,4,5,6,7,8,8,9}    #unordered, mutable
print(my_set)
#my_set[1]=10                      #indexing is not allowed
my_set.add(10)
print(my_set)

# #output          #duplicates are not allowed
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}