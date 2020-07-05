n=int(input())
arr=input().strip().split()
arr=[int(i) for i in arr]

count=0
for i in arr:
    count+=max(arr)-i
print(count)