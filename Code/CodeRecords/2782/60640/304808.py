def find_min(arr, index):
    res = abs(arr[index] - arr[0])
    for ii in range(1, index):
        res = min(res, abs(arr[index] - arr[ii]))
    return res


n = int(input())
inp = []
for i in range(n):
    inp.append(int(input()))
ans = inp[0]
for i in range(1, n):
    ans += find_min(inp, i)
print(ans, end="")
