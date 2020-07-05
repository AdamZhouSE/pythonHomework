def transfer(arr):
    arr.sort()
    res = ''
    for i in range(len(arr)):
        res += arr[i]
    return res


result = []
for i in range(int(input())):
    a = input()
    array1 = input().split()
    array2 = input().split()
    if transfer(array1) == transfer(array2):
        result.append(1)
    else:
        result.append(0)
for i in range(len(result)):
    print(result[i])