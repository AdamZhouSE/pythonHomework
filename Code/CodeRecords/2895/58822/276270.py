n=input()
b=eval(n)
li=[]
for i in range(int(b[0]),int(b[1]+1)):
    li.append(i)
b=li.copy()
a=b[0]
for i in range(1,len(b)):
    a=a&(int)(b[i])
print(a)