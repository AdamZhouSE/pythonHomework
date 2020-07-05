import math
def find(n, k, arr):
    if len(arr) == 2:
        return arr[1]
    else:
        teamLen = int(math.factorial(n)/n)
        t = int(k / teamLen)
        k = k % teamLen
        if k != 0:
            t += 1
        else:
            k = teamLen
        current = arr[t]
        arr.remove(current)
        return current + find(n - 1, k , arr)


n = int(input())
k = int(input())
arr = [str(x) for x in range(n + 1)]

print(find(n, k, arr))