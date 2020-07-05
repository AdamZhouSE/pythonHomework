def search(ls: list) -> list:
    table = {}
    arr = []
    res = []
    for i in range(len(ls)):
        table[ls[i][0]] = i
        arr.append(ls[i][0])
    arr.sort()
    for i in ls:
        index = binary_search(arr, i[1])
        if index == -1:
            res.append(-1)
        else:
            res.append(table.get(index))
    return res


def binary_search(arr: list, target: int) -> int:
    if target > arr[-1]:
        return -1
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return arr[left]


n = int(input())
lst = []
for k in range(n):
    temp = input().split(',')
    temp = list(map(int, temp))
    lst.append(temp)
print(search(lst))