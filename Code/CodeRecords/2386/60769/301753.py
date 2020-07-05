def solve(arr, target):
    count = 0
    length = len(arr)
    for i in range(length - 2):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, length - 2):
            if j != 1 and arr[j] == arr[j - 1]:
                continue
            temp_target = target - arr[i] - arr[j]
            left = j + 1
            right = length - 1
            recordleft = 99999999
            while left != right:
                if arr[left] + arr[right] > temp_target:
                    right -= 1
                elif arr[left] + arr[right] < temp_target:
                    left += 1
                else:
                    if arr[left] != recordleft:
                        count += 1
                        recordleft = arr[left]
                    left += 1
    return count


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        arr = sorted(map(int, input().split(" ")))
        target = int(input())
        res = solve(arr, target)
        if res == 0:
            print(0)
        else:
            print(1)