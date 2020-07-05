a=input().lstrip('[').rstrip(']').split(',')
b=input().lstrip('[').rstrip(']').split(',')
for i in range(len(a)):
    a[i]=int(a[i])
    
for i in range(len(b)):
    b[i]=int(b[i])
#print(a)
#print(b)
res=[]
for i in a:
    for j in b:
        if i==j and not i in res:
            res.append(i)
res.sort()
print(res)