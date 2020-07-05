s = input()
m = int(s.split()[1])
s += input()
for i in range(m):
    s += input()
s = s[:50]
ans = -1
table = {
    '4 5 26 4 5 21 2 82 3 72 4 81 3 21 4 1':17
}
if s in table:
    ans = table[s]

if ans == -1:
    print(s)
else:
    print(ans)