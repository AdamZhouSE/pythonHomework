n = int(input())
h = [x for x in range(1,n + 1)]
v = [x for x in range(1,n + 1)]
days = ''
for i in range(0,n * n):
    s = input().split(' ')
    hi = int(s[0])
    vi = int(s[1])
    if(hi in h and vi in v):
        days = days + str(i + 1) + ' '
        h.remove(hi)
        v.remove(vi)
print(days[:-1])