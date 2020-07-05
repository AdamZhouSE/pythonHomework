def f(s,k):
    if len(s)>k:
        first=s[:k]
        second=s[k:]
        first.reverse()
        return first+f(second,k)
    else:
        s.reverse()
        return s

a=int(input().strip())
for i in range(a):
    line=input().strip()
    length=int(line.split()[0])
    K=int(line.split()[1])
    t=[x for x in input().strip().split()]
    print(' '.join(f(t,K)),end=' ')
    print()
    