m, ns = map(int, input().split(' '))
account = list(map(int, input().split(' ')))
ans = []
for n in range(ns):
    l, r = map(int, input().split(' '))
    ans.append(str(min(account[l - 1:r])))
print(' '.join(ans) + ' ', end='')
