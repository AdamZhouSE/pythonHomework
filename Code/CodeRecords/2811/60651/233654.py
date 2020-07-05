inlist=input().split()
position=int(inlist[0])
n=int(inlist[1])
molist=[]
for i in range(5):
    innum=int(input())
    mo=innum%position
    if mo not in molist:
        molist.append(mo)
    else:
        print(i+1)
        break
    
    
    
    
