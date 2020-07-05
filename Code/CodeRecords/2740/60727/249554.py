a=input()
times = a[1:len(a)-1].split(",")
for i in range(0,len(times)):
    times[i] = times[i][1:len(times[i])-1]
converted=[]
upper=24*60
for i in times:
    li=i.split(":")
    temp = int(li[0])*60+int(li[1])
    if temp==0:
        temp=upper
    converted.append(temp)
minGap = upper
for i in range(0,len(converted)-1):
    for j in range(i+1,len(converted)):
        if abs(converted[i]-converted[j])<minGap:
            minGap=abs(converted[i]-converted[j])
print(minGap)

      