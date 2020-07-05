arr1 = [int(i) for i in input().split(',')]
arrlen1 = len(arr1)
arrv1 = 0
for i in range(arrlen1):
    arrv1 += ((-2) ** i) * arr1[arrlen1 - i - 1]
arr2 = [int(i) for i in input().split(',')]
arrlen2 = len(arr2)
arrv2 = 0
for i in range(arrlen2):
    arrv2 += ((-2) ** i) * arr2[arrlen2 - i - 1]
n = arrv1 + arrv2
ans = []
while n != 0:
    if (n - 1) % 2 == 0:
        ans.append(1)
        n -= 1
    else:
        ans.append(0)
    n //= (-2)
ans = ans[::-1]
print('[', end='')
print(ans[0], end='')
for i in range(1, len(ans)):
    print(', ', end='')
    print(ans[i], end='')
print(']')