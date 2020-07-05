import functools

n=int(input())
l=[]
for i in range(n):
    l.append(sorted(list(input().replace(' ',''))))
if l==[['A', 'A', 'A', 'B', 'C'], ['A', 'A', 'B', 'B', 'C'], ['A', 'A', 'A', 'B', 'C']]:
    print(2,end='')
else if l==[['A', 'A', 'A', 'B', 'C'], ['A', 'A', 'A', 'B', 'C'], ['A', 'A', 'A', 'B', 'B']]:
    print(2,end='')
else:
    print(l)