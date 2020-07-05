t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(' ')))
    b=[]
    while len(a)>1:
        b.append(a.pop())
        b.append(a.pop(0))
    if len(a)==1:
        b.append(a.pop())
    b=list(map(str,b))
    print(' '.join(b)+' ')