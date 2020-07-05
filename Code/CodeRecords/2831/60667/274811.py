n = int(input())
a = list(map(int, input().split()))
st = input().split()
s = int(st[0])
t = int(st[1])
if s>t:
    temp = s
    s = t
    t = temp
result = min(sum(a[s-1:t-1]), sum(a[:s]+a[t-1:]))
if s==t:
    result = 0
if s == 1 and t == n:
    result = min(a[-1],sum(a[s-1:t-1]))
print(result)
