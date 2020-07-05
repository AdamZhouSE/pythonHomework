a = eval(input())
a.sort()
s = 0
for i in range(1, len(a)):
    s = max(a[i]-a[i-1], s)
print(s)