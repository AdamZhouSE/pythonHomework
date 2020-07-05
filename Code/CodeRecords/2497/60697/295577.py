target=int(input())
position=eval(input())
speed=eval(input())
leng=len(position)
res=[]
for i in range(leng):
    res.append([position[i],speed[i]])
res.sort(key=lambda x:(x[0],x[1]))
times=[float((target-car[0])/car[1]) for car in res]
ans=0
while len(times)>1:
    lead=times.pop()
    if(lead<times[-1]):
        ans+=1
    else:
        times[-1]=lead
print(ans+bool(times))

