null='null'
a=eval(input())
b=eval(input())
c=[]
for i in a:
    if isinstance(i,int):
        c.append(i)
for i in b:
    if isinstance(i,int):
        c.append(i)
c=sorted(c)
print(c)
