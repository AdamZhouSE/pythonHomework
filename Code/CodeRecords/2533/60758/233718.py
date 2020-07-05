a=input()
b=[]
c=[]
d=[]
for i in range(0,len(a)):
    if(str.isdigit(a[i])):
        x=int(a[i])
        if(x%2==0):
            b.append(x)
        else:
            c.append(x)
d=b+c
print(d)