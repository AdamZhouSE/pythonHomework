n = int(input())
a = [int(i) for i in input().split()]
ans = 1
j = -1
for i in range(n):
    if a[i] == 1:
        if j != -1:
            ans *= (i - j)
        j = i
print(ans)