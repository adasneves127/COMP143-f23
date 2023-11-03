# Week 5

# Loops and Indentation


my_other_list = []

for i in range(4):
    my_other_list.append(input("Enter a string: "))

print(my_other_list)

print(
    [
        i
        for i
        in range(1000)
        if i % 2 != 1
    ]
)

