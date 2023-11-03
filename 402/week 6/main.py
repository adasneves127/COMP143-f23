
max_num = input("What is the max number to sum to? ")

max_num = int(max_num)

sum = 0
for num in range(2, max_num + 1):
    sum = sum + num

print(sum)
