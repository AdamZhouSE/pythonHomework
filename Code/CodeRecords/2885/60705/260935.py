def number_of_divisible(arr: list) -> int:
    count = 0
    for i in range(0, len(arr)):
        if arr[i] % 3 == 0:
            count += 1
    return count


def dfs(arr: list, maximum: int):
    num = number_of_divisible(arr)
    if num > maximum:
        maximum = num
    if len(arr) > 2:
        i = 0
        while i < len(arr):
            a = arr.pop(i)
            j = 0
            while j < len(arr):
                b = arr.pop(j)
                arr.insert(0, a+b)
                maximum = dfs(arr, maximum)
                arr.remove(a+b)
                arr.insert(j, b)
                j += 1
            arr.insert(i, a)
            i += 1
    return maximum


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        length = int(input())
        l = list(map(int, input().split(" ")))
        print(dfs(l, 0))
