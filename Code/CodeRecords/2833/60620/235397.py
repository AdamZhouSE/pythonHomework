n=int(input())
a=sum(map(int,input().split()))
b=sorted(map(int,input().split()))
v=sum(b[-2:])
if(v>=a):
    print('YES')
else:
    print('NO')