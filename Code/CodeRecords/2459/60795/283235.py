arr=[int(n) for n in input().split(' ')]
num,delay=arr[0],arr[1]
list=[int(n) for n in input().split(' ')]
time=[]
for i in range(0,num):
    at=[]
    at.append(i+1)
    at.append(list[i])
    time.append(at)
for i in range(0,num):
    for j in range(i+1,num):
        if time[i][1]<time[j][1]:
            time[i],time[j]=time[j],time[i]
for i in range(0,num):
    for j in range(i+1,num):
        if time[i][1]==time[j][1]:
            if time[i][0]<time[j][0]:
                time[i],time[j]=time[j],time[i]
sum,result=0,[]
for i in range(0,num):
    result.append(0)
count=0
while count<num:
     now=delay+count+1
     pos=-1
     for i in range(0,len(time)):
         if now>=time[i][0]:
             tem=abs(now-time[i][0])*time[i][1]
             sum=sum+tem
             pos=i
             count=count+1
             result[time[i][0]-1]=now
             break
     del time[pos]
print(sum)

for i in range(0,num):
    print(result[i],end=" ")