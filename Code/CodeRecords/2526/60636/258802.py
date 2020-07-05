root1=eval(input())
root2=eval(input())
res=[]
for i in root1:
    res.append(i)
for i in root2:
    res.append(i)
res.sort()
print(res)