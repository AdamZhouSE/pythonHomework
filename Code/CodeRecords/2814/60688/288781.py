persons=0
sumt=0
n=int(input())
time=input().split(" ")
time=list(int(a) for a in time)
time=sorted(time)
for i in range(0,n):
    if(time[i]>=sumt):
        persons=persons+1
        sumt=sumt+time[i]
print(persons)
