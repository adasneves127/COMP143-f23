import my_utils


def f():
    for i in range(10):
        print(i)


# f()
print(my_utils.calculate_area(3))


print(my_utils.calculate_area(5))
print(my_utils.calculate_area(10))
print(my_utils.calculate_area(100))
print("Done!")  # This will never run!
