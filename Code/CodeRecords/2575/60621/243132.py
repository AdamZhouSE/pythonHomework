a=input()
b=[]
depth=-1
c=[]
for i in a:
    if(i=="("):
        depth+=1
        b.append(depth)
        c.append(depth)
    else:
        c.append(depth)
        b.pop()
        depth-=1
print(c)