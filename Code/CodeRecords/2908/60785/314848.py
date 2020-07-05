n=int(input())
l=[]
for ff in range(n):
    l.append(list(input()))
for i in l:
    i.sort()
    i=''.join(i)

print(l)
