def main():
    op = 1
    while (op != 4):
        print("File Handling\n")
        op = int(input("Select an option:\n1)Create file\n2)Read file\n3)Append to file\n4)Exit\n"))
        if (op == 1):
            name = input("Enter the name of the file: ")
            name += ".txt"
            msg = input("Enter the message: ")
            createFile(name, msg)
        elif (op == 2):
            name = input("Enter the name of the file: ")
            name += ".txt"
            readFile(name)
        elif (op == 3):
            name = input("Enter the name of the file: ")
            name += ".txt"
            msg = input("Message to append to file: ")
            appendFile(name, msg)
    exit()


def createFile(name, msg):
    f = open(name, "w")
    if f.write(msg + "\n"):
        print("File written successfully!")
    closeFile(f)
    #We can do the same like this:
    """
    with open(name, "w") as file:
        file.write("Something")
        
    !!Without calling close()
    """


def readFile(name):
    f = open(name)  # 'r' is the default processing mode
    for line in f.readlines():
        print(line, end='')
    print()
    # print(f.read())
    closeFile(f)


def appendFile(name, msg):
    f = open(name, "a")
    f.write(msg)
    closeFile(f)


def closeFile(f):
    f.close()


if __name__ == '__main__':
    main()
