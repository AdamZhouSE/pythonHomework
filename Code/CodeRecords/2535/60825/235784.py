a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))
ans = ma = 0
for i, x in enumerate(l):
    ma = max(ma, x)
    if ma == i: ans += 1
print(ans)