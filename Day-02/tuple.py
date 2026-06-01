my_tuple = (1,2,3,4,5,6,7,8,8)    #ordered, allows duplicate, Immutable and uses ()
print(my_tuple)
my_tuple[1] = 9                    #immutable
my_tuple.append(10)                #immutable


# output
# (1, 2, 3, 4, 5, 6, 7, 8, 8)
# Traceback (most recent call last):
#   File "/workspaces/Learn_python-for-devops/Day-02/tuple.py", line 3, in <module>
#     my_tuple[1] = 9
#     ~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment