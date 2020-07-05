def findASet(i,arr):
    current = arr[i]
    result = [current]
    i += 1
    while i < len(arr):
        if arr[i]%current == 0:
            current = arr[i]
            result.append(current)
        i += 1
    return result


def solve(arr):
    result = []
    i = 0
    while i < len(arr):
        temp = findASet(i,arr)
        if len(temp) > len(result):
            result = temp
        i += 1
    return result
    

#main-----
arr = input().split(',')
for x in range(len(arr)):
    arr[x] = int(arr[x])
arr.sort()


print(solve(arr))

