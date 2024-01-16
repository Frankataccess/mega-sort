import os

temp_data = 

def main_menu () :
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("1) Recursion")
    print("2) Linear Search")
    print("3) Binary Search")
    print("4) Bubble Sort")
    print("5) Insertion Sort")
    print("6) Merge Sort")
    print("7) Add Data")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    
    choice = int(input("Enter your choice: "))
    if choice <1 or choice >7:
        print("INVALID CHOICE")
        return main_menu()
    else:
        selection()
    
    def selection():
        if choice == 1 :
            print()
        if choice ==2:
            print()
        if choice == 3:
            print()
        if choice == 4:
            print()
        if choice == 5:
            print()
        if choice == 6:
            print()
        if choice ==7:
            filemenu()
            
    def filemenu():
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Add existing file")
        print("2) Create new file")
        print("~~~~~~~~~~~~~~~~~~~~~~~")

        filechoice = int(input("Enter choice: "))
        if filechoice == 1:
            file_path = input("Enter file path")
            if os.path.exists(file_path):
                print("file found")
            else:
                print("Error file not found")

        elif filechoice ==2: 
            print()
        else:
            return filemenu()
main_menu()