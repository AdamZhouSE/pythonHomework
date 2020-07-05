n = int(input())
b = str(bin(n))
s = list(b[2:])
ans = []
tmp = 0
for i in s:
    if i == '0':
        tmp += 1
    else:
        ans.append(tmp)
        tmp = 0
if s.count('1') < 2:
    print(0)
else:
    print(max(ans)+1)