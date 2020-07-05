tArr = input()
tArr = [int(n) for n in tArr.split(" ")]
n = int(tArr[0])
k = int(tArr[1])
arr = input()
arr = [int(n) for n in arr.split(" ")]

availableMax = 0  # max volume container

i = 0
while i < n:
    arr[i] = int(arr[i])
    if (arr[i] > availableMax) and (k % arr[i] == 0):
        availableMax = arr[i]
    i += 1
    
print(k//availableMax)