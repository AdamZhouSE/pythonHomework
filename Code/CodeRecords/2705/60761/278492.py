a=input().replace(" ","")
pairs=list(map(str,a[2:-2].split("],[")))
joinsets=[]
ans=[]
for pair in pairs:
    u,v=map(int,pair.split(","))
    k=1
    if(not joinsets):
        joinsets.append([u,v])
    else:
        for i in range(len(joinsets)):
            if(u in joinsets[i] and v in joinsets[i]):
                ans.append([u,v])
                k=0
                break
            elif(u in joinsets[i]):
                joinsets[i].append(v)
                k=0
                break
            elif(v in joinsets[i]):
                joinsets[i].append(u)
                k=0
                break
        if(k==1):
            joinsets.append(u,v)
print(ans[-1])
            