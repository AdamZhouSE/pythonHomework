inlist=input().split()
modlist=[]
last=1+int(list[1])
for i in inlist[2,last]:
    moi=i%list[0]
    if moi not in modlist:
        list.append(moi)
    else:
        print(i)
        break
    
    
