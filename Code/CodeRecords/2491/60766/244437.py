a=eval(input())
b=eval(input())
res=[]
for i in range(len(a)):
    if a[i] in b:
        res.append(a[i])
print(sorted(res))