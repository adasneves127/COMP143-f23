from getpass import getpass

# print(True)
# print(False)

target = "Hi"
user = getpass("Enter a string: ")

while target != user:
    user = input("Enter a string: ")
