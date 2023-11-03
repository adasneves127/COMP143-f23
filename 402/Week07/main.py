
# Basic Calculator
left_number = float(input("Enter a number: "))
operator = input("Enter an operator (+, -, *, /)")
right_number = float(input("Enter a second number: "))

result = 0

if operator == '+':
    result = left_number + right_number  # type: ignore
elif operator == '-':
    result = left_number - right_number  # type: ignore
elif operator == '*':
    result = left_number * right_number  # type: ignore
elif operator == '/':
    result = left_number / right_number  # type: ignore
else:
    # This introduces a small bug into our code
    # print(f"")
    # Without this exit line it will still print the results
    # exit(-1)
    raise ValueError(f"Operator {operator} is not valid!")


print(f'{left_number} {operator} {right_number} is equal to {result}')
