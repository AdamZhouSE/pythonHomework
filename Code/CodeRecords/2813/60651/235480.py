n=int(input())
namelist=[]
plist=[]
namelist2=[]
plist2=[]
namelist3=[]
plist3=[]
for i in range(n):
    list1=input().split()
    name=list1[0]
    p=int(list1[1])
    namelist2.append(name)
    plist2.append(p)
    if name in namelist:
        position=namelist.index(name)
        plist[position]+=p
    else:
        namelist.append(name)
        plist.append(p)
maxp=max(plist)

for m in range(n):
    name2=namelist2[m]
    p2=plist2[m]
    if name2 in namelist3:
      
        position2=namelist3.index(name2)
        plist3[position2]+=p2
        if plist3[position2]==maxp:
            print(name2)
            break
    else:
        namelist3.append(name2)
        plist3.append(p2)
        if p2==maxp:
            print(name2)
            break
    

        
        
