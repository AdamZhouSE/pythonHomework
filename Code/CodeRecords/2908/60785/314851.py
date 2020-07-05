n=int(input())
l=[]
re=[]
for ff in range(n):
    l.append(list(input()))
for i in l:
    i.sort()
    a=''.join(i)
    re.append(a)
ans=len(set(re))
print(ans)
