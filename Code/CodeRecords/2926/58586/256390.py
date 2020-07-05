nums=int(input())
arr=list(map(int,input().split(" ")))
used=[0]*100
for i in arr:
    used[i-1]+=1
print(max(used))