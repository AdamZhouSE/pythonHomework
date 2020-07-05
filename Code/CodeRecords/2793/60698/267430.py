# 33
nc = input().split()
n = int(nc[0])
c = int(nc[1])
arr = input().split()
arr = list(map(int, arr))
count = 1
for i in range(0, len(arr) - 1):
    if arr[len(arr) - 1 - i] - arr[len(arr) - i - 2] <= c:
        count = count + 1
    else:
        break
if c==0:
    print(0)
else:
    print(count)
       