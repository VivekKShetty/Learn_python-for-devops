import sys

type = sys.argv[1]

if type == "t2.micro":
    print("You will be charged 4 dollars for this instance")
elif type == "t3.micro":
    print("You will be charged 6 dollars for this instance")
elif type == "t3.large":
    print("You will be charged 8 dollars for this instance")
else:
    print("Nothing will be created")