name=str(input())
st=int(input())
l = ''
for i in name:
    l += (str(st + ord(i) - ord('A')))
while len(l) > 2 and l != '100':
    res = ''
    for i in range(1, len(l)):
        res += (str((int(l[i]) + int(l[i - 1])) % 10))
    l=res
print(l,end="")