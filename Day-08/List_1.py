My_list = [1, 2, 4, 3, 7, 8,"apple", "banana"]

print(My_list)                  #output is [1, 2, 4, 3, 7, 8, 'apple', 'banana']
print(My_list[6])               #output is banana

My_list.append("watermelon")
print(My_list)                  #output is [1, 2, 4, 3, 7, 8, 'apple', 'banana', 'watermelon']

My_list.remove(4)
print(My_list)                  #output is [1, 2, 3, 7, 8, 'apple', 'banana', 'watermelon']

New_list = My_list + ["Mango"]
print(New_list)                 #output is [1, 2, 3, 7, 8, 'apple', 'banana', 'watermelon', 'Mango']

print(My_list[0] + My_list[4])         #output is 9
print(My_list[6] + "--" + My_list[7])  #output ois banana--watermelon

print(len(My_list))             #output is 8

sub_My_list = My_list[0:4]
print(sub_My_list)              #output is [1, 2, 3, 7]

Unsorted_list = [1 ,3, 2, 6, 4, 9, 8]
Unsorted_list.sort()       #adding print directly to this will return none because this will just sort the list an dreturn nothing. So we need to print the original list
print(Unsorted_list)