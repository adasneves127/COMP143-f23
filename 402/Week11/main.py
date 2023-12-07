
# Reading
file = open("test.txt", 'r')

for line in file:
    print(line)

file.close()

# Writing
file = open("output.txt", "w")

file.write("Hello, world!\n")

file.close()

# print(file.readline())
# print(file.readline())
