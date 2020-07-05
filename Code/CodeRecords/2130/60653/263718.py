n = int(input())
s = ""
for i in range(0, n):
    s += str(i)
if n == 3:
    print(3)
else:
    print(s[n])