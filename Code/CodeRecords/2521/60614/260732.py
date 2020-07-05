origin=eval(input())
i=0
times=[]
while i<len(origin):
    count=1
    key=origin.pop(0)
    while key in origin:
        count+=1
        origin.remove(key)
    times.append([key,count])
result=[]
key=-1
while len(times)>0:
    times.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(times)):
        if times[i][0]!=key:
            times[i][1]-=1
            key=times[i][0]
            result.append(key)
            if times[i][1]==0:
                del times[i]
            break
print(result)