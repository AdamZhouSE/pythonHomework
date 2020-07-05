n=int(input())
arr=[int(x) for x in input().split(" ")]
maxLen=0
temp=0
for i in range(n):
    temp += 1
    maxLen = max(maxLen, temp)
    if i==n-1:
        continue
    if arr[i+1]>arr[i]*2:
        temp=0
print(maxLen)