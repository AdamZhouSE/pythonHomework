def test():
    a = input()
    total_arr = a.split(',')
    total_arr = list(map(int, total_arr))
    total_arr.sort()
    n = len(total_arr)
    total_sum = 0
    for i in range(0, len(total_arr)):
        total_sum = total_sum + total_arr[i]
    for k in range(1, len(total_arr) // 2+1):
        if (total_sum * k) % n == 0 and helper(total_arr, 0, k, (total_sum * k) /n):
            print(True)
            return
    print(False)


def helper(arr, begin, n, target):
    if n == 0:
        return target == 0
    if target < n * arr[begin]:
        return False
    for i in range(begin, len(arr) - n):
        if i > begin and arr[i] == arr[i - 1]:
            continue
        if helper(arr, i + 1, n - 1, target - arr[i]):
            return True
    return False


test()