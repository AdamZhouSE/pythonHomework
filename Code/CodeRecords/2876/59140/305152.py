n = int(input())
arr = [int(x) for x in input().split(" ")]
res=0
for i in range(1, n - 1):
    if arr[i - 1] == arr[i + 1] == 1 and arr[i] == 0:
        arr[i + 1] = 0
        res+=1
print(res)