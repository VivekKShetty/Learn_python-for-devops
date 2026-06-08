import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

try:
    quo = num1/num2
except ZeroDivisionError:
    print("invalid Number")
     
sum = num1 + num2
print(sum)
