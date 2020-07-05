times=input().replace('[','').replace(']','').replace('"','').split(',')
res=[]
for time in times:
    num = int(time[0:2])*60+int(time[3:5])
    res.append(num)
res.sort()
ans=res[0]+24*60-res[-1]
for i in range(1,len(res)):
    ans=min(ans,res[i]-res[i-1])
print(ans)
