n=int(input())
times=input().split(" ")
num=[]
for i in range(n):
    times[i]=int(times[i])
times.sort()
num.append(times[0])
for i in range(1,n):
    if times[i]>=sum(num):
        num.append(times[i])
print(len(num))