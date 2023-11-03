names = []

for i in range(5):
    name = input("What is your name (LastName-FirstName)")
    names.append(name)


for name in names:
    split_name = name.split("-")
    print(f"Nice to meet you, {split_name[1]} {split_name[0]}")
