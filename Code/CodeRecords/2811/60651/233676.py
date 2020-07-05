inlist=input().split()
position=int(inlist[0])
n=int(inlist[1])
molist=[]
for i in range(n):
    innumber=int(input())
    mo=innumber%position
    if mo not in molist:
        molist.append(mo)
    else:
        print(i+1)
        break
if(len(molist)==n):
    print(-1)
        
