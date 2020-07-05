import functools,collections
l=eval(input())
m=[]
c=collections.Counter(l)
for i in c:
    if c[i]>len(l)//3:
        m.append(i)
print(m)