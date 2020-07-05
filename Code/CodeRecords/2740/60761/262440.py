times=list(map(str,input()[2:-2].split('","')))
minutes=[]
for time in times:
    minutes.append(int(time[0:2])*60+int(time[3:5]))
minutes.sort()
ans=100000
for i in range(1,len(minutes)):
    ans=min(ans,minutes[i]-minutes[i-1])
ans=min(ans,minutes[0]+60*24-minutes[-1])
print(ans)