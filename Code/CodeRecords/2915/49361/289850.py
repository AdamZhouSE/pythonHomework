n = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
maxNum = 0
num = 0
res = []
for i in range(n):
    if i == 0:
        res.append(arr[i])
        maxNum = max(maxNum, res.__len__())
        continue
    if arr[i] <= res[0] * 2:
        res.append(arr[i])
        maxNum = max(maxNum, res.__len__())
    else:
        while res.__len__() > 0:
            if arr[i] > res[0] * 2:
                del res[0]
            else:
                break
        res.append(arr[i])
        maxNum = max(maxNum, res.__len__())
print(maxNum)
