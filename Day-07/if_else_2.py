import sys

type = sys.argv[1]

if type == "t2.micro":
    print("A instance of type t2.micro will be created")
else:
    print("your input is not t2.micro, so we cannot create")

    #this can be used when we have single condition. For multiple condition use if else if