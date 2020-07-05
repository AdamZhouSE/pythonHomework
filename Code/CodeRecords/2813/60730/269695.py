n,c,m=eval(input()),{},[]
for i in range(n):a,b=input().split(' ');c[a]=c.get(a,0)+int(b);m.append([a,c[a]])
n=max(c.values())
for i ,j in m:
    if c[i]==n and int(j)>=n:print(i);break