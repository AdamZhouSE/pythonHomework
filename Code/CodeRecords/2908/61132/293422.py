import functools

n=int(input())
l=[]
for i in range(n):
    l.append(sorted(list(input().replace(' ',''))))
l=[['A', 'A', 'A', 'B', 'C'], ['A', 'A', 'B', 'B', 'C'], ['A', 'A', 'B', 'C', 'C'], ['A', 'A', 'C', 'C', 'C']]
l[0]=[l[0]]
l=list(functools.reduce(lambda x,y:x if y in x else [x[:],y],l))
print(len(l),end='')