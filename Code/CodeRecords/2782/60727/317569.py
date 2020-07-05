n, arr, res = eval(input()), [], []
for i in range(0, n):
    arr.append(eval(input()))
for i in range(1, n):
    val = max(arr)
    for j in range(0, i):
         val = min(abs(arr[i] - arr[j]), val)
    res.append(val)
print(sum(res) + arr[0], end="")