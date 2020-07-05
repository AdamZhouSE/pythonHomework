n=int(input())
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort(reverse=True)
happy=1
time=0
for i in range(n):
    for j in range(i+1,n):
        time=time+num[j]
    if num[i]>=time:
        happy=happy+1
    time=0
print(happy)