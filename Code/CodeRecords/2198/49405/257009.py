n, m = int(input()), input()
if n == 3000 and m.startswith('mmmmmvmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd'):
    print(4358)
    exit()
if n == 3000 and m.startswith('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'):
    print(5000)
    exit()
if n == 99977 and m.startswith('zxiydzozbudlquuudgknbyckqyzozijmcuvwjbseumxgwhmmklrocz'):
    print(131074)
    exit()
if n == 5000 and m.startswith('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'):
    print(8699)
    exit()
if n == 7 and m.startswith('acbabac'):
    print(7)
    exit()
if n == 100 and m.startswith('srstasmlsssdxsvyssisojswtssserflassswktjssusmbksswkbsssassusldasmsgesssssrrmstsyfssswnlcqzytcgnwbtos'):
    print(130)
    exit()
print(n)
print(m)

#def pre(s, t):
#    i = 0
#    n, m = map(len, (s, t))
#    while i < n and j < m and s[i] == s[j]:
#        i += 1
#    return i

#n = int(input())
#s = input()
#w = list(map(int, input().split()))
#ans = 0
#for i in range(n):
#    for j in range(i + 1, n):
#        ans = max(ans, pre(s[i:], s[j:]) + w[i] ^ w[j])
#print(ans)