def solve(arr,tag):
    i = 0
    while arr[i] < tag and i < len(arr)-1:
        j = i + 1
        while j < len(arr) and arr[j] + arr[i] <= tag:
            if arr[i] + arr[j] == tag:
                return [i+1,j+1]
            j += 1
        i += 1


arr = list(eval(input()))
tag = int(input())

print(solve(arr,tag))










































