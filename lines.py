import sys

def main():
    #1 validate cmd line arguments
    check_arguments()
    #DO a try bar that opens the file
    try:
        #2. open file
        with open(sys.argv[1], "r") as file:
            count = 0
            for line in file:
                if is_code(line):
                    count += 1
            print(count)
    #Exception if file is not found
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arguments():
    #Validats sys.argv per requirements (i.e. if there's too few or too much cmd line args)
    if len (sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    #check for .py extension (if not, exit)
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

def is_code(line):
    #Returns true if line is actual code, false if not
    # .lstrip() removes leading whitespace (the indentations caused by f(x), loops, try's if stats, etc)
    stripped_line = line.lstrip()

    #Check if line was empty(Only white space)
    if not stripped_line:
        return False

    #check if line starts with a comment
    if stripped_line.startswith("#"):
        return False
    #return true
    return True
#Run function
if __name__ == "__main__":
    main()
