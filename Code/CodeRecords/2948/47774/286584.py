name=str(input())
st=int(input())
l = ''
res = ''
for i in name:
    l += (str(st + ord(i) - ord('A')))
while len(l) > 2 and l != '100':
    for i in range(1, len(l)):
        res += (str((int(l[i]) + int(l[i - 1])) % 10))
print(res)