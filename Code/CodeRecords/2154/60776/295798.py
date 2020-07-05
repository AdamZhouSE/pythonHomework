a=input()
b=[]
for i in range(0,len(a)):
    b.append(a[i])
c=[]
c.extend(b)
b.reverse()
print(b==c)