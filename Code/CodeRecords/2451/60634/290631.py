def solve(arr,tag):
    l = 0
    r = len(arr) - 1
    while True:
        if arr[l] >= tag:
            return l
        else:
            l += 1
        if arr[r] == tag:
            return r
        elif arr[r] < tag:
            return r + 1
        else:
            r -= 1

arr = list(eval(input()))
tag = int(input())

print(solve(arr,tag))