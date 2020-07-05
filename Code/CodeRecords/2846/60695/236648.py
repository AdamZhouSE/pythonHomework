n = int(input())
s = sorted(input().split(" "))
news = [None]*n
news[0] = int(s[0])
r = 0
for i in range(1, n):
    if int(s[i]) != int(s[i-1]) and int(s[i]) != 0:
        news[i] = int(s[i])
for i in range(0, n):
    if news[i] != 0 and not news[i] is None:
        r += 1
print(r)