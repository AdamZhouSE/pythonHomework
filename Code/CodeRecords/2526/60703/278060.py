root1 = input()[1:-1].split(",")
root2 = input()[1:-1].split(",")


while "null" in root1:
    root1.remove("null")
while "null" in root2:
    root2.remove("null")
while "" in root1:
    root1.remove("")
while "" in root2:
    root2.remove("")

sadasd = map(int,root1)
root1 = list(map(int,root1))
root2 = list(map(int,root2))
root1.extend(root2)
root1.sort()
print(root1)