n=int(input())
arr=input().split()
arr=list(map(int,arr))
arr.sort()
i=0
while i<len(arr):
    if arr[i]<i+1:
        arr.pop(i)
        i=i-1
    i=i+1
print(len(arr))