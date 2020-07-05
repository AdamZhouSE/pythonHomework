n=int(input())
l=[]
for ff in range(n):
    l.append(list(input()))
for i in l:
    i.sort()
    a=''.join(i)

print(a)
