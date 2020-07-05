line = input().split(' ')
n = int(line[0])
l = int(line[1])
r = int(line[2])
arr = [1]*n
now = 2
for i in range(l,1,-1):
    arr[n-i+1] = now
    now = now * 2
minSum = 0
for i in arr:
    minSum += i
now = 2
type = 1
for i in range(1,n):
    arr[i] = now
    if type<r-1:
        now = now * 2
        type = type + 1
#print(arr)
maxSum = 0
for i in arr:
    maxSum = maxSum + i
print(str(minSum)+" "+str(maxSum))