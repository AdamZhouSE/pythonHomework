def solve(arr,tag):
    l = 0
    r = len(arr) - 1
    while l <= r:
        if arr[l] == tag and arr[r] == tag:
            return [l,r]
        if arr[l] != tag:
            l += 1
        if arr[r] != tag:
            r -= 1
    return [-1,-1]
    
arr = list(eval(input()))
tag = int(input())
print(solve(arr,tag))