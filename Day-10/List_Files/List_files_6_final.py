import os

folders = input("Please enter folder names with spaces:").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Enter a valid folder name")
        break                              #use continue to continue the execution
    except PermissionError:
        print("No Permission")
        break
    
    print("Files present in folder" + folder)
    for file in files:
        print(file)



