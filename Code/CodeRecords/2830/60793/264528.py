temp = list(map(int, input().split()))
b, k = temp[0], temp[-1]
a = list(map(int, input().split()))
n = 0
for i in range(0, k):
    n += a[i] * b ** (k - i - 1)
if n % 2 == 0:
    print('odd')
else:
    print('even')