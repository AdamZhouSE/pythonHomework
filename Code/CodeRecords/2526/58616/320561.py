root1=input()[1:-1].split(",")
root2=input()[1:-1]
root=[]
for i in root1:
    if i.lstrip("-").isdigit():
        root.append(int(i))
for i in root2:
    if i.lstrip("-").isdigit():
        root.append(int(i))
root.sort()
print(root)