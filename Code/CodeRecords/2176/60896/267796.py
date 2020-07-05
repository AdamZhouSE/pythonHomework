a=input()
b=len(a)
c=[]
for i in range(0,len(a)):
    c.append(a[i:len(a)])
b=sorted(range(len(c)), key=lambda k: c[k])
for i in range(0,len(c)-1):
    print(b[i]+1,end=' ')
print(b[-1]+1)