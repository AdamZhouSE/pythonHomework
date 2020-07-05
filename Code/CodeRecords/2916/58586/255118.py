n=int(input())
arr=list(map(int,input().split(" ")))
d={4:0,8:1,15:2,16:3,23:4,42:5}
count=0
used=[0]*n
for round in range(n//6):
    idx=0
    for i in range(n):
        if used[i]==0 and d[arr[i]]==idx:
            used[i]=1
            idx+=1
        if idx==6:
            count+=1
            break
print(n-count*6)