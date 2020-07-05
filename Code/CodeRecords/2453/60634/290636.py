def solve(arr,tag):
    cut = arr[len(arr)-1]
    if tag <= cut:
        i = len(arr) - 1
        while arr[i] <= cut and i >= 0:
            if tag == arr[i]:
                return i
            i -= 1
    else:
        i = 0
        while arr[i] >= arr[i-1]:
            if tag == arr[i]:
                return i
            i += 1
    return -1

arr = list(eval(input()))
tag = int(input())

print(solve(arr,tag) != -1)