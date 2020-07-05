num = int(input())
m = input().split(" ")
n = list(map(int, m))
ans = [0, 0]
for i in range(num):
    if len(n) == 1:
        ans[i % 2] = ans[i % 2] + n[0]
        break
    if (n[0] >= n[len(n) - 1]):
        ans[i % 2] = ans[i % 2] + n[0]
        del (n[0])
    else:
        ans[i % 2] = ans[i % 2] + n[len(n) - 1]
        del (n[len(n) - 1])
print(' '.join(map(str,ans)))
