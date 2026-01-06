import os
def p_create_text():
    name = input("Enter File Name with (.txt): ").strip()

    if not name:
        print("Please Enter File Name!")
        return

    file = open(name, "w")
    file.close()
    print("File created successfully!")

def p_write_text():
    name = input("Enter existing file name: ").strip()

    if os.path.isfile(name) == False:
        print("File does not exist! Please create it first.")
        return

    content = input("Enter data to write: ")

    f = open(name, "w")
    f.write(content)
    f.close()

    print("Data written successfully!")

def p_read_text():
    name = input("Enter existing file name: ").strip()

    if not os.path.isfile(name):
        print("File does not exist!")
        return

    print("File Content:")
    f = open(name, "r")
    print(f.read())
    f.close()

def p_append_text():
    name = input("Enter existing file name: ").strip()

    if os.path.isfile(name) == False:
        print("File does not exist!")
        return

    extra = input("Enter data to append: ")

    f = open(name, "a")
    f.write("\n" + extra)
    f.close()

    print("Data appended successfully!")
