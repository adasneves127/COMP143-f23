input_file = open("count.txt", "r")

number_as_str = input_file.readline()

number = int(number_as_str)

input_file.close()

output_file = open("count.txt", "w")

output_file.write(str(number + 1))

output_file.close()
