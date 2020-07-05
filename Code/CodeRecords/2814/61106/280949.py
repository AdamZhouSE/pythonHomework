n=int(input())
pleasant_num=1
time=list(map(int,input().split()))
time.sort()
for i in range(1,n):
    if time[i]>=sum(time[:i]):
        pleasant_num += 1
print(pleasant_num+1)   