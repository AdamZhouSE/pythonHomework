k,m = input().split()
k = int(k)
m = int(m)

s = input()
sl = list(s)
t = []
for i in sl:
    t.append(i)
n = int(input())

for i in range(n):
    ai, bi, ci = input().split()
    ai = int(ai) 
    bi = int(bi) 
    ci = int(ci)
    st = ''.join(t)
    temp = st[ai:bi]
    t = list(st)
    t.insert(ci, temp)
    

for i in range(k):
    print(t[i], end='')