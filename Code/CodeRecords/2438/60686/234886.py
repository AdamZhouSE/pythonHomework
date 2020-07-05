arr = input().split(",")
arr[0] = arr[0][1]
result = []
arr[len(arr) - 1] = arr[len(arr) - 1][0:1]
numOfZero = arr.count('0')
for i in range(0, numOfZero):
    result.append(0)
for j in range(0, arr.count('1')):
    result.append(1)
for k in range(0, arr.count('2')):
    result.append(2)
print(result)