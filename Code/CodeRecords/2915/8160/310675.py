n = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
maxNum = 0
res = []
for i in range(n):
    if i == 0:
        res.append(arr[i])
        maxNum = max(maxNum, res.__len__())
        continue
    if arr[i] <= res[len(res)-1] * 2:
        res.append(arr[i])
        maxNum = max(maxNum, res.__len__())
    else:
        res.clear()
        res.append(arr[i])
        maxNum = max(maxNum, res.__len__())
print(maxNum)
