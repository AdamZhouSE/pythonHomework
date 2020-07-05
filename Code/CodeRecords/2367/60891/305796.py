k = int(input())
ans = -1
tmp = ''
for i in range(6):
    tmp += '1'
    n = int(tmp)
    if n % k == 0:
        ans = len(tmp)
        break
print(ans)
