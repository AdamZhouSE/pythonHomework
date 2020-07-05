arr=input()
arr=arr[1:len(arr)].split(",")
time=[]
for i in arr:
    time.append(int(i[1:3])*60+int(i[4:6]))
time.sort()
mintime=1440
for i in range(len(time)-1):
    mintime=min(mintime,time[i+1]-time[i])
mintime=min(mintime,time[0]-time[len(time)-1]+24*60)
print(mintime)