n = int(input())
s = input()
cnt = 0
for i in range(n):
    if s[i] == '1':
        cnt = cnt + 1
res = "1"
for i in range(n - cnt):
    res = res + "0"
print(res, end = "")