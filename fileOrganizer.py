import os
import shutil

def organizeFiles():
    path = input("Enter the path of the directory to organize: ")
    if not os.path.exists(path):
        print("Invalid path")
        return
    
    files = os.listdir(path)
    for file in files:
        name, ext = os.path.splitext(file)
        ext = ext[1:]
        if ext == '':
            continue
        if os.path.exists(path + '/' + ext):
            shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
        else:
            os.makedirs(path + '/' + ext)
            shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    print("Files organized successfully")

def main():
    case = 0
    while case != 3:
        case = int(input("What you want to do? \n1. Organize Files \n2. Delete old files \n3. Exit\n"))
        if case == 1:
            organizeFiles()
        elif case == 2:
            break
        elif case == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()