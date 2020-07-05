maxn = 1010
used = [False]*maxn
a = [[0]*maxn]*maxn
match = [0]*maxn

def find(x,n):
    for i in range(n):
        if not used[i] and a[x][i]:
            used[i] = True
            if not match[i] or find(match[i],n):
                match[i] = x
                return True
    return False

li = input().split()
n = int(li[0])
m = int(li[1])
for i in range(1,m+1):
    li = input().split()
    x = int(li[0])
    y = int(li[1])
    a[i][x] = a[i][y] = 1
ans = 0
res = 1
for i in range(1,m+1):
    used = [False] * maxn
    if find(i,n):
        ans += 1
    else:
        res = i - 1
        break
print(res)
