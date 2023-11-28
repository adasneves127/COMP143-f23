# File I/O (Input/Output)

# What is a file?
# A location on your computer's disk where data is stored (Long term)

# What types of files are there?
# Text and Binary

# How can we read from a file?
#

my_file = open("file.txt")

for line in my_file:
    print(line, end="")
print()

my_file.close()
# How can we write to a file?
#

file_two = open("other.txt", "w")

file_two.write("Hello Class!")

file_two.close()
