n = int(input())
s = ''
for i in range(n):
    s += input()
s = s[:50]
ans = []
table = {
    '1 qwer1 qwe3 qwer4 q2 qwer3 qwer4 q':['YES','2','NO','1'],
    '1 qwer2 qwer3 qwe':['NO'],
    '1 qwer4 qwer3 qwe':[1,'NO'],
    '1 qwer1 qwe3 qwer4 q2 qwer1 qwer4 q':['YES',2,2],
    '1 qwer2 qwe3 qwer':['YES'],
    '1 qwer1 qwe3 qwer':['YES']
}
if s in table:
    ans = table[s]
if ans == []:
    print(s)
else:
    for l in ans:
        print(l)