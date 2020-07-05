t = int(input())
for i in range(t):
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    a = arr[0]
    b = arr[1]
    m = arr[2]
    ans = b // m - a // m
    if b % m == 0:
        ans += 1
    print(ans)
