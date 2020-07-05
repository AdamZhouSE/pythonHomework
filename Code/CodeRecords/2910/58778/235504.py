n=int(input())
clist=[]
for i in range(n):
    s=input()
    str2=s.split( )
    temp=[]
    temp.append(int(str2[0]))
    temp.append(int(str2[1]))
    clist.append(temp)
tlist=[]
tlist.append(max(clist[0]))
m=0
for i in range(1,n):
    b=max(clist[i])
    sm=min(clist[i])
    if(b<=tlist[len(tlist)-1]):
        tlist.append(b)
    elif sm<=tlist[len(tlist)-1]:
        tlist.append(sm)
    else:
        m=1
        break;
if m==1:
    print("NO")
else:
    print("YES")
