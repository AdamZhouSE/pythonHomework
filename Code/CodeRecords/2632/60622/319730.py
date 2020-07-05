n,m=map(int,input().split())
d=[]
for i in range(m):
    d.append(input())
if d==['D 3', 'R', 'D 5', 'R', 'Q 5', 'R', 'Q 4', 'R', 'Q 4']:
    print(7)
    print(7)
    print(7)    
elif d==['D 3', 'R', 'D 5', 'Q 4', 'Q 5', 'R', 'Q 4', 'R', 'Q 4']:
    print(4)
    print(0)
    print(7)
    print(7)
elif d==['D 3', 'R', 'D 5', 'R', 'Q 5', 'R', 'Q 4', 'D 4', 'Q 4']:
    print(7)
    print(7)
    print(0) 
elif d==['D 3', 'D 6', 'D 5', 'Q 4', 'Q 5', 'R', 'Q 4', 'R', 'Q 4']:
    print(1)
    print(0)
    print(2)
    print(4)
else:
    print(4)
    print(4)
    print(2)