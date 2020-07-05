arr = list(map(int, input()[1:-1].split(",")))
n = int(input())
res = -1
for i in range(0, len(arr)):
    if n == arr[i]:
        res = i
print(res)
