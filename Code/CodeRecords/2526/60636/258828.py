root=input().replace('null', '"1"')
root1=eval(root)
while("1" in root1):
    root1.pop(root1.index("1"))
root2=eval(input())
res=[]
for i in root1:
    res.append(i)
for i in root2:
    res.append(i)
res.sort()
print(res)