n=int(input())
time=input().split(" ")
time=list(int(a) for a in time)
time=sorted(time)
people=0
sumtime=0
for i in range(0,n):
    if(time[i]>=sumtime):
        people=people+1
        sumtime=sumtime+time[i]
print(people)
