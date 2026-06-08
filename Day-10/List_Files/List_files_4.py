import os

folders = input("Please enter folder names with spaces: ").split()

for folder in folders:
    files=os.listdir(folder)
    print(files)


# Output:
# ['containerd', 'oryx', 'python', 'dotnet', 'conda', 'tmp']
# ['vscode-git-cf6e05c8e8.sock', 'vscode-ipc-87385f11-9b22-4921-8bed-b09d0aa6813c.sock', 'dockerd.log', 'storage_version.txt', 'codespaces_logs', 'vscode-ipc-6a05b56a-1418-4ee0-a22e-0491e309451b.sock', 'sshd.log']