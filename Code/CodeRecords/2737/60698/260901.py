# 13
arr = eval(input())
n = len(arr)
result = []
for i in range(0, len(arr)):
    if arr.count(arr[i]) > n // 3:
        result.append(arr[i])
result = list(set(result))
print(result)
