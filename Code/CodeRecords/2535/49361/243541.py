arrays = input().replace("[", "").replace("]", "").split(",")
arr = []
for each in arrays:
    each = int(each)
    arr.append(each)
result = 0
tmp = arr.copy()
tmp.sort()
maxVal = 0
for i in range(len(arr)):
    if arr[i] > maxVal:
        maxVal = arr[i]
    if tmp[i] == maxVal:
        result += 1
        maxVal = 0
print(result)