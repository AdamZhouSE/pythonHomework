arr=[int(n) for n in input().split(',')]
index=0
for i in range(0,len(arr)-1):
    if arr[i+1]<arr[i]:
        index=i+1
        break
if arr[0]<arr[index]:
    index=0
print(arr[index])
