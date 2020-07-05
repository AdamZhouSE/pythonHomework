nums=int(input())
arr=list(map(int,input().split(" ")))
used=[]
for j in range(nums-1,-1,-1):
    if arr[j] not in used:
        used.insert(0,arr[j])
print(len(used))
print(*used)