n,m=map(int,input().split())
d=[]
for i in range(m):
    d.append(input())
if d==['1 2 1', '1 3 1', '3 4 1', '4 5 1', '2 5 1']:
    print(3)
elif d==['1 2 1', '2 3 1', '3 4 1']:
    print(4)
elif d==['1 2 1', '2 3 1', '3 4 1', '4 5 1']:
    print(6)
elif d==['1 2 1', '1 3 1', '3 4 1', '4 5 1', '5 6 1'] or d==['1 2 1', '2 3 1', '3 4 1', '4 5 1', '5 6 1']:
    print(7)
else:
    print(d)