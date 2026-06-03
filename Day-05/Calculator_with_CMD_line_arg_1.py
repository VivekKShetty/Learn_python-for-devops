import sys

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    diff = num1 - num2
    return diff

def mul(num1,num2):
    prod = num1 * num2
    return prod

num1 =float(sys.argv[1])             #use int or float for numbers or else it will take as string and just concatinate it
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation==("add"):
    output = add(num1,num2)
    print(output)

if operation==("sub"):
    output = sub(num1,num2)
    print(output)

if operation==("mul"):
    output = mul(num1,num2)
    print(output)

