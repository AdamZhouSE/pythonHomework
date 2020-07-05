t=int(input())
alls=[]
for i in range(t):
    x=list(input())
    x.sort()
    print(x)
    if(not x in alls):
        alls.append(x)
print(len(alls))