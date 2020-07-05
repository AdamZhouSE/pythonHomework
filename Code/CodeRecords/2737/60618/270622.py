a=eval(input())
b=len(a)//3
c=list(set(a))
d=[]
for i in range(0,len(c)):
    if a.count(c[i])>b:
        d.append(c[i])
print(d)