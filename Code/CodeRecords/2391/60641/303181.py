num_of_student = int(input())
names = []
for i in range(0, num_of_student):
    names.append(input())
num_of_orders = int(input())
names_ordered = []
for i in range(0, num_of_orders):
    name = input()
    if name in names_ordered:
        print("REPEAT")
    elif name in names:
        print("OK")
        names_ordered.append(name)
    else:
        print("WRONG")