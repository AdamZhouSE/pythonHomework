root1=input()
root2=input()
root1=root1[1:-1].split(",")
root2=root2[1:-1].split(",")
root=root1+root2
n=root.count("null")
for i in range(n):
    root.remove("null")
index=0
for i in range(len(root)):
    if root[i]=="":
        index+=1
    else:
        root[i]=int(root[i])
for i in range(index):
    root.remove("")
root.sort()
print(root)