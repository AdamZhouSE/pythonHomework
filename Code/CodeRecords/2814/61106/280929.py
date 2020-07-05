n=int(input())
pleasant_num=1
time=[map(int,input().split())]
time.sort()
for i in range(1,n):
    if time[i]<=sum(time[:i-1]):
        pleasant_num += 1
print(pleasant_num)   