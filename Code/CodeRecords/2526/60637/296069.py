root1=input()[1:-1].split(',')
root2=input()[1:-1].split(',')
root=[]
for i in root1:
    if i.isnumeric() or i[1:].isnumeric():
        root.append((int)(i))
for i in root2:
    if i.isnumeric() or i[1:].isnumeric():
        root.append((int)(i))
root.sort()
print(root)






