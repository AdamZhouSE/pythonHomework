n=int(input())
pleasant_num=1
time=list(map(int,input().split()))
time.sort()
result=[]
for i in range(n):
    if time[i]>=sum(result):
        result.append(time[i])
print(len(result))