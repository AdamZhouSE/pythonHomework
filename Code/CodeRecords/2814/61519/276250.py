n=int(input())
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort()
time=0
for i in range(1,n):
    for j in range(i):
        time=time+num[j]
    if num[i]<time:
        for k in range(i+1,n):
            if num[k]>=time:
                tem=num[i]
                num[i]=num[k]
                num[k]=tem
                break
    time=0
for i in range(1,n):
    for j in range(i):
        time=time+num[i]
    if num[i]<time:
        print(i+1)
        break