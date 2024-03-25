import os
import shutil

main_path = "D:\\program\\project_karishin"

if not os.path.isdir(main_path):
    os.mkdir(main_path)

folders = ["txt", "Docs", "Csv", "Copy"]
for folder in folders:
    folder_path = os.path.join(main_path, folder)
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

for i in range(1, 6):
    filename = os.path.join(main_path + "\\txt", f"{i}.txt")
    with open(filename, "w") as file:
        file.write(f"This is file {i}.txt\n")

if os.path.exists(main_path + "\\Copy"):
    shutil.rmtree(main_path + "\\Copy")

shutil.copytree(main_path + "\\txt", main_path + "\\Copy")

for filename in os.listdir(main_path + "\\txt"):
    source = os.path.join(main_path + "\\txt", filename)
    destination = os.path.join(main_path + "\\Docs", filename)
    shutil.move(source, destination)

shutil.rmtree(main_path + "\\txt")

new_filename = os.path.join(main_path + "\\Docs", "first.txt")
old_filename = os.path.join(main_path + "\\Docs", "1.txt")
if not os.path.isdir(folder_path):
        os.rename(old_filename, new_filename)


def new_file():
    filename = input("Enter the name of the new file: ")
    file_path = os.path.join(main_path, filename)
    with open(file_path, "w") as file:
        print(f"File {filename} has been created.")

def rename_file():
    old_filename = input("Enter the name of the file to rename: ")
    new_filename = input("Enter the new name for the file: ")
    old_file_path = os.path.join(main_path, old_filename)
    new_file_path = os.path.join(main_path, new_filename)
    os.rename(old_file_path, new_file_path)
    print(f"File {old_filename} has been renamed to {new_filename}.")

def delete_file():
    filename = input("Enter the name of the file to delete: ")
    file_path = os.path.join(main_path, filename)
    os.remove(file_path)
    print(f"File {filename} has been deleted.")

def parse_folder(path):
    all_files = []
    all_directories = []
    for root, dirs, files in os.walk(path):
        for file in files:
            all_files.append(file)
        for dir in dirs:
            all_directories.append(dir)
    return all_files, all_directories

command = input("Enter 'new', 'rename' or 'del' to do this command or type 'parse' to scan the directory: ")
if command == "new":
    new_file()
elif command == "rename":
    rename_file()
elif command == "del":
    delete_file()
elif command == "parse":
    files, directories = parse_folder(main_path)
    print("Files:", files)
    print("Directories:", directories)
else:
    print("Invalid command.")
