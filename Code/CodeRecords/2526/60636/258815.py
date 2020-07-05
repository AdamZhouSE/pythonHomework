root=input()
if(root!="null"):
    root1=eval(root)
else:
    root1=[]
root2=eval(input())
res=[]
for i in root1:
    res.append(i)
for i in root2:
    res.append(i)
res.sort()
print(res)