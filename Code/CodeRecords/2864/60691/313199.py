N = 1000
n = eval(input())
mx = 0
cnt = [0]*N
f = [0]*N
line = input().split(' ')
x = 0
index = 0
for i in range(1,n+1):
    x = int(line[index])
    index = index + 1
    mx = max(mx,x)
    cnt[x]+=x
f[1] = cnt[1]
for i in range(2,mx+1):
    f[i] = max(f[i-1],f[i-2]+cnt[i])
print(f[mx])
