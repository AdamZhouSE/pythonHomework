root1=input()
root2=input()
root1=root1[1:-1].split(",")
root2=root2[1:-1].split(",")
root=root1+root2
n=root.count("null")
for i in range(n):
    root.remove("null")
for i in range(len(root)):
    if "0"<=root[i]<="9":
        root[i]=int(root[i])
    else:
        print(root[i])
root.sort()
print(root)