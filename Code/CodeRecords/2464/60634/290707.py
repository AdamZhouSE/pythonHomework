def solve(s,arr):
    al = [0 for x in range(len(arr))]
    l = 1
    while l <= len(arr):
        i = 0
        while i <= len(arr)-l:
            count = al[i] + arr[i + l - 1]
            al[i] = count
            if count == s:
                return l
            i += 1
        l += 1


s = int(input())
arr = list(eval(input()))

print(solve(s,arr))

































