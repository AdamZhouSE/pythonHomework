times=eval(input())
minutes=[]
for t in times:
    h=int(t[0])*10+int(t[1])
    m=int(t[3])*10+int(t[4])
    minutes.append(h*60+m)
    if h==0:
        minutes.append(h*60+m+1440)

minutes=sorted(minutes)
min_dis=1440
for i in range(len(minutes)-1):
    min_dis=min(min_dis,minutes[i+1]-minutes[i])
print(min_dis)