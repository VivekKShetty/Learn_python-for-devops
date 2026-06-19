import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder Not found"
        
    except PermissionError:
        return files, "No Permission"


def main():
    folder_path = input("Please enter folder names:").split()

    for folder in folder_path:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in folder", {folder_path})
                for file in files:
                    print(file)
        else:
            print("Folder not found", {error_message})

if __name__ == "__main__":
    main()