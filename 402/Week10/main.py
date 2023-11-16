import func_test


# What are Functions?
# An excerpt of code with a given name

# Why do we use them?
# 1. Clean Code and Organization
# 2. Highly Re-usable

# How do we make them?
def test_function():
    print("It works!")
# Not automatically called on program starting


# How can we use them?
test_function()

# How do we know when to use them?
# Large Blocks of Code that accomplish one (or more) task
# Code that is used often
test_function()

func_return = func_test.test(15)
print(func_return)


print(func_test.compound_interest(100, 1500, 0.10))