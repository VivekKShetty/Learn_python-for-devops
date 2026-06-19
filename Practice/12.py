import os

folders = input("Please enter the folder names with spaces in between:").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Enter a valid folder name")
        continue
    except PermissionError:
        print("You do not have required permission")
        break
    print("Files in folder:", folder)
    for file in files:
        print(file)


