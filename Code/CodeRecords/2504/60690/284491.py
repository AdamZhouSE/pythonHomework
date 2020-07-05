s=input()[2:-2].split("],[")
k=int(input())
res=[]
distance=[]
for i in range(len(s)):
    l=s[i].split(",")
    l[0]=int(l[0])
    l[1]=int(l[1])
    thisdis=l[0]**2+l[1]**2
    if len(res)<k:
        res.append(l)
        distance.append(thisdis)
    else:
        if thisdis<max(distance):
            maxindex=distance.index(max(distance))
            res[maxindex]=l
            distance[maxindex]=thisdis
print(res)