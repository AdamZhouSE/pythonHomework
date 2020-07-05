n=int(input())
ans = 0;
a = [0, 1, 1, -2];
b = [1, 2, 6, 7];
if (n >= 5):
    ans = n + 1 + a[n % 4];
if (n < 5):
    ans = b[n - 1];
print(ans)

