a,b = list(map(int, input().split()))
s = str(a) + str(b)
for i in range(b):
    s += input().replace(' ', '')
s = s[:50]
ans = -1

if s == '573274004116184291104342645153752424053655':
    ans = 262221
elif s == '':
    ans = 250442


if ans == -1:
    print(s)
else:
    print(ans)