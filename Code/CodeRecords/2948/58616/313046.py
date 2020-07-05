# 洛谷P1898
s = input()
ST = int(input())
l = ""
for i in s:
    l += (str(ord(i) + ST - ord('A')))
while len(l) > 2 and l != "100":
    s = ""
    for i in range(1, len(l)):
        s += (str((int(l[i]) + int(l[i - 1])) % 10))
    l = s
print(int(l), end = '')