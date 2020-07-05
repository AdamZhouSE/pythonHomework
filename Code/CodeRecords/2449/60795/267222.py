arr=[int(n) for n in input().split(',')]
target=int(input())
index=-1
for i in range(0,len(arr)):
    if arr[i]==target:
        index=i
        break
print(index)