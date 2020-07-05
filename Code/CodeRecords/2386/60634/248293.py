def find(l, r, sum, arr, rest):
    if rest == 1:
        while l < r:
            if sum == int(arr[l]):
                return True
            l += 1
        return False
    else:
        nextSum = sum - int(arr[l])
        result = False
        while not result and l <= r - rest:
            result = result or find(l + 1, r, nextSum, arr, rest - 1)
            l += 1
        return result


problems = int(input())
for x in range(problems):
    size = int(input())
    array = input().split(" ")
    X = int(input())

    if find(0, size, X, array, 4):
        print(1)
    else:
        print(0)