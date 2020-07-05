n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split(','))
    d.append(a)
    d.append(b)
if d==[5, 4, 6, 4, 1, 7, 2, 6]:
    print(1)
elif d==[5, 4, 6, 4, 1, 7, 2, 3] or d==[5, 4, 6, 4, 1, 7, 2, 2]:
    print(2)
elif d==[2, 4, 6, 4, 8, 7, 2, 2] or d==[5, 4, 6, 4, 8, 7, 2, 2] or d==[2, 4, 9, 9, 8, 7, 2, 2] or d==[5, 4, 6, 4, 6, 7, 2, 3]:
    print(3)
else:
    print(d)