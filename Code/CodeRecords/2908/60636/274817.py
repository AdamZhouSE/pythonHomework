t=int(input())
alls=[]
for i in range(t):
    x=list(input())
    x.sort()

    if(not x in alls):
        alls.append(x)
a=len(alls)
print(a,end="")