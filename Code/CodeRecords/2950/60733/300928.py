import sys

a = input()
n = len(a)
s = 0
ans = 0
if n & 1 == 1:
    print("-1")
    sys.exit()
for i in range(n):
    if a[i] == '2':
        s = s + 1
    if a[i] == "5":
        s = s - 1
    if s < 0:
        print("-1")
        sys.exit()
    ans = max(s, ans)
print(ans)
