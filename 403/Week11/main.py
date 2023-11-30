
def write_to_file():
    file = open("test.txt", 'w')
    file.write("This is a test!")
    file.close()


def read_from_file():
    file = open("test.txt", 'r')
    print(file.readlines())
    file.close()


def main():
    write_to_file()
    read_from_file()

    while True:
        file_name = open("output.txt", 'w')
        if input("Type 'Hello' to skip!").lower() == 'hello':
            continue

        file_name.close()


main()
