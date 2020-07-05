n = eval(input())
arr = input().split()
for i in range(0,len(arr)):
    arr[i] = int(arr[i])
arr = sorted(arr)
cnt = 0
want = []
for j in range(1,n+1):
    want.append(j)
for k in range(0,len(arr)):
    cnt += abs(want[k]-arr[k])
print(cnt)
