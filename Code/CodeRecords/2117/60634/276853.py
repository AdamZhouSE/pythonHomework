def solve(n,arr):
    count = 0
    k = 1
    while k <= n:
        i = k-1
        while i < n:
            arr[i] = arr[i]^1
            i += k
        count += arr[k-1]
        k += 1
    return count


#main-----
n = int(input())
arr = [0 for x in range(n)]
print(solve(n,arr))