n = int(input())
if n <= 1:
    print("A")
elif n == 2:
    print("ABA")
else:
    a = [""] * n
    a[1] = "ABA"
    zm = ['C', 'D', 'E', 'F', 'G', 'H']
    ans = a[1]
    for i in range(0, n-2):
        ans += zm[i]
        ans += a[i+1]
        a[i+2] = ans
    print(ans)