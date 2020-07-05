# 7
k,m = input().split()
k = int(k)
m = int(m)
l = [1]
while(len(l) <=k):
    for i in range(len(l)):
        if 2*l[i] + 1 not in l:
            l.append(2*l[i] + 1 )
        if 4*l[i] + 5 not in l:
            l.append(4*l[i] + 5 )
    l = list(set(l))
    l.sort()
l = l[:k]
s = []
for i in range(len(l)):
    s.append(str(l[i]))
print(''.join(s))