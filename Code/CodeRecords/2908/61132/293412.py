import functools

n=int(input())
l=[]
for i in range(n):
    l.append(sorted(list(input().replace(' ',''))))
print(l)
l[0]=[l[0]]
l=list(functools.reduce(lambda x,y:x if y in x else [x[0],y],l))
print(str(len(l)),end='')