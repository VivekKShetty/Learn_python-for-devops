import sys

def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(num1 , num2):
    diff = num1 - num2
    return diff

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    print(add(num1, num2))
if operation == "sub":
    print(sub(num1, num2))
