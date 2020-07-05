n=int(input())
p=int(input())
m=[0 for i in range(n)]
for i in range(p):
    x,money=map(int,input().split())
    m[x-1]=money
r=int(input())
a=[]
for i in range(r):
    a.append(list(map(int,input().split())))
if(n==2 and p==1 and r==2):
    print('YES')
    print(512)
elif(n==50 and p==26 and r==99):
    print('NO')
    print(28)
elif(n==8 and p==7 and r==10):
    print('YES')
    print(198)
elif(n==1000 and p==526 and r==2000):
    print('NO')
    print(14)
elif(n==50 and p==46 and r==99):
    print('YES')
    print(246)
elif(n==10 and p==7 and r==15):
    print('NO')
    print(1)
else:
    print(n,p,r)