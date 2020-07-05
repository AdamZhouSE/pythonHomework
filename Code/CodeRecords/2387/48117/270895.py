nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
s = input().split(' ')
for i in range(n):
    s[i] = int(s[i])

ans = s
for j in range(m):
    op = input().split(' ')
    if op[0] == '1':
        reverse = True
    else:
        reverse = False
    l = int(op[1]) - 1
    r = int(op[2])
    target = sorted(ans[l:r], reverse=reverse)
    ans = ans[0:l] + target + ans[r:]

q = int(input()) - 1
print(ans[q])
