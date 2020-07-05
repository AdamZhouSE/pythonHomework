s1 = list("".join(input().split(" ")))
s1.sort()
s1 = "".join(s1)
s2 = list("".join(input().split(" ")))
s2.sort()
s2 = "".join(s2)
ans = "YES"
for i in s2:
    if not s1.count(i):
        ans = "NO"
        break
print(ans, end="")