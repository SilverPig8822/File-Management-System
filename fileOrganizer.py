import os
import shutil
import time

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

def deleteOldFiles():
    current_time = time.time()
    path = input("Enter the path of the directory to delete old files: ")
    if not os.path.exists(path):
        print("Invalid path")
        return
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)

        # Get the time of the last access of the file in seconds since the epoch
        file_time = os.path.getmtime(file_path)

        
        # If the file is older than 2 years, delete it
        if current_time - file_time > 2*365*24*60*60:  # 2 years in seconds
            try:
                shutil.rmtree(file_path)
                print(f"Deleted {file_path}")
            except OSError:
                print(f"Error deleting {file_path}")
            
    print("Files deleted successfully")

def main():
    case = 0
    while case != 3:
        case = int(input("What you want to do? \n1. Organize Files \n2. Delete old files \n3. Exit\n"))
        if case == 1:
            organizeFiles()
        elif case == 2:
            deleteOldFiles()
        elif case == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()