t=int(input())
alls=[]
for i in range(t):
    x=list(input())
    x.sort()
    while(" " in x):
        x.pop(x.index(" "))
    if(not x in alls):
        alls.append(x)
print(len(alls),ends="")